"""
=============================================================================
Retail Sales Data Cleaning & Validation Pipeline
Module: src/clean_data.py
Project: Business Intelligence & Sales Reporting Automation
Dataset: UCI Machine Learning Repository — Online Retail (UK)
=============================================================================
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Resolve project directories
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Locate raw input file
possible_inputs = [
    RAW_DIR / "Online Retail.xlsx",
    RAW_DIR / "online_retail.xlsx",
    RAW_DIR / "Online Retail.csv",
    RAW_DIR / "online_retail.csv",
]

input_file = next((f for f in possible_inputs if f.exists()), None)


def clean_retail_data():
    print("=" * 70)
    print("RETAIL SALES DATA CLEANING & VALIDATION PIPELINE")
    print("=" * 70)

    if not input_file or not input_file.exists():
        raise FileNotFoundError(
            f"Dataset not found in: {RAW_DIR}\n"
            "Please run 'python src/download_dataset.py' or download the UCI dataset\n"
            "and place 'Online Retail.xlsx' inside data/raw/."
        )

    print(f"[1/6] Loading raw dataset: {input_file.name} ...")
    if input_file.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(input_file)
    else:
        df = pd.read_csv(input_file, encoding="ISO-8859-1")

    initial_row_count = len(df)
    print(f"      Initial Raw Records: {initial_row_count:,}")

    # Standardize column headers
    print("[2/6] Standardizing column names...")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    required_cols = {
        "invoiceno", "stockcode", "description", "quantity", 
        "invoicedate", "unitprice", "customerid", "country"
    }
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing expected columns in source data: {sorted(missing_cols)}")

    # Data Types & Formatting
    print("[3/6] Parsing data types and formatting fields...")
    df["invoiceno"] = df["invoiceno"].astype(str).str.strip()
    df["stockcode"] = df["stockcode"].astype(str).str.strip()
    df["description"] = df["description"].fillna("UNKNOWN ITEM").astype(str).str.strip()
    df["invoicedate"] = pd.to_datetime(df["invoicedate"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)
    df["unitprice"] = pd.to_numeric(df["unitprice"], errors="coerce").fillna(0.0)
    df["country"] = df["country"].fillna("Unspecified").astype(str).str.strip()

    # Format customer_id as clean string without decimal '.0'
    df["customerid"] = df["customerid"].apply(
        lambda x: str(int(x)) if pd.notnull(x) and str(x).replace(".", "").isdigit() else (None if pd.isna(x) else str(x))
    )

    # Duplicate Removal
    print("[4/6] Checking for exact duplicate records...")
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"      Removed {duplicate_count:,} exact duplicate rows.")
    else:
        print("      No exact duplicates found.")

    # Identify Cancellations & Returns
    print("[5/6] Separating cancellations and sales records...")
    is_cancellation = (
        df["invoiceno"].str.startswith("C", na=False) |
        df["invoiceno"].str.startswith("c", na=False) |
        (df["quantity"] < 0)
    )

    df_cancellations = df[is_cancellation].copy()
    cancellation_count = len(df_cancellations)
    print(f"      Identified Cancellations / Returns: {cancellation_count:,} rows")

    # Positive Sales Population
    df_sales = df[~is_cancellation].copy()

    # Filter out zero or negative unit prices (administrative/damaged stock entries)
    zero_price_mask = df_sales["unitprice"] <= 0
    zero_price_count = zero_price_mask.sum()
    if zero_price_count > 0:
        print(f"      Removed non-positive unit prices (damaged/test items): {zero_price_count:,} rows")
        df_sales = df_sales[~zero_price_mask].copy()

    # Filter out zero quantities if any remained
    df_sales = df_sales[df_sales["quantity"] > 0].copy()

    # Calculate Line Revenue (Quantity * UnitPrice)
    df_sales["line_revenue"] = (df_sales["quantity"] * df_sales["unitprice"]).round(4)
    df_cancellations["line_revenue"] = (df_cancellations["quantity"] * df_cancellations["unitprice"]).round(4)

    # Rename columns for SQL compatibility
    rename_map = {
        "invoiceno": "invoice_no",
        "stockcode": "stock_code",
        "invoicedate": "invoice_date",
        "unitprice": "unit_price",
        "customerid": "customer_id"
    }
    df_sales = df_sales.rename(columns=rename_map)
    df_cancellations = df_cancellations.rename(columns=rename_map)

    # Export Processed Datasets
    print("[6/6] Exporting prepared datasets to data/processed/ ...")
    clean_sales_path = PROCESSED_DIR / "sales_clean.csv"
    cancellations_path = PROCESSED_DIR / "sales_cancellations.csv"

    df_sales.to_csv(clean_sales_path, index=False)
    df_cancellations.to_csv(cancellations_path, index=False)

    # Quality Report Metrics
    missing_cust_sales = df_sales["customer_id"].isna().sum()
    pct_missing_cust = (missing_cust_sales / len(df_sales)) * 100
    total_revenue = df_sales["line_revenue"].sum()
    total_units = df_sales["quantity"].sum()
    distinct_invoices = df_sales["invoice_no"].nunique()
    distinct_customers = df_sales["customer_id"].dropna().nunique()
    min_date = df_sales["invoice_date"].min()
    max_date = df_sales["invoice_date"].max()

    quality_summary = pd.DataFrame([
        {"Metric": "Raw Total Rows", "Value": f"{initial_row_count:,}"},
        {"Metric": "Duplicate Rows Dropped", "Value": f"{duplicate_count:,}"},
        {"Metric": "Cancellation Rows Separated", "Value": f"{cancellation_count:,}"},
        {"Metric": "Zero/Negative Price Rows Excluded", "Value": f"{zero_price_count:,}"},
        {"Metric": "Clean Sales Records", "Value": f"{len(df_sales):,}"},
        {"Metric": "Missing Customer IDs (Sales)", "Value": f"{missing_cust_sales:,} ({pct_missing_cust:.2f}%)"},
        {"Metric": "Earliest Transaction Date", "Value": str(min_date)},
        {"Metric": "Latest Transaction Date", "Value": str(max_date)},
        {"Metric": "Total Clean Sales Revenue (GBP)", "Value": f"£{total_revenue:,.2f}"},
        {"Metric": "Total Units Sold", "Value": f"{total_units:,}"},
        {"Metric": "Distinct Invoices", "Value": f"{distinct_invoices:,}"},
        {"Metric": "Identified Unique Customers", "Value": f"{distinct_customers:,}"},
    ])

    quality_report_path = REPORTS_DIR / "data_quality_summary.csv"
    quality_summary.to_csv(quality_report_path, index=False)

    print("=" * 70)
    print("PIPELINE EXECUTION SUMMARY")
    print("=" * 70)
    for _, row in quality_summary.iterrows():
        print(f"  * {row['Metric']:<36} : {row['Value']}")
    print("-" * 70)
    print(f"  [Output 1] Clean Sales Data       : {clean_sales_path}")
    print(f"  [Output 2] Cancellations Audit    : {cancellations_path}")
    print(f"  [Output 3] Quality Summary Report : {quality_report_path}")
    print("=" * 70)

    return df_sales, df_cancellations


if __name__ == "__main__":
    clean_retail_data()
