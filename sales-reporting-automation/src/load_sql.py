"""
=============================================================================
Automated Database Loader: Python to MySQL Pipeline
Module: src/load_sql.py
Project: Business Intelligence & Sales Reporting Automation
=============================================================================
"""

import os
import sys
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# Resolve project paths
ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "processed" / "sales_clean.csv"
CANCELLATIONS_PATH = ROOT / "data" / "processed" / "sales_cancellations.csv"


def get_db_engine():
    """Builds SQLAlchemy engine using environment variables with safe defaults."""
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    database = os.getenv("MYSQL_DB", "sales_analytics")

    if not user or password is None:
        print("[!] ERROR: MySQL credentials not detected in environment variables.")
        print("    Please set them before running this script in Windows PowerShell:")
        print('      $env:MYSQL_USER="root"')
        print('      $env:MYSQL_PASSWORD="your_mysql_password"')
        print('      $env:MYSQL_HOST="localhost"')
        print('      $env:MYSQL_PORT="3306"')
        print('      python src/load_sql.py')
        sys.exit(1)

    connection_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(connection_url, echo=False)


def load_data_to_mysql(batch_size=10000, truncate_first=True):
    print("=" * 70)
    print("MYSQL DATA LOADER: AUTOMATED PIPELINE REFRESH")
    print("=" * 70)

    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Prepared data not found at: {CSV_PATH}\n"
            "Please run 'python src/clean_data.py' first."
        )

    engine = get_db_engine()

    # Step 1: Test Connection & Ensure Schema Exists
    print("[1/4] Connecting to MySQL server...")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DATABASE();"))
        current_db = result.scalar()
        print(f"      Connected successfully to database: '{current_db}'")

        if truncate_first:
            print("      Ensuring clean slate (truncating existing sales_clean table)...")
            conn.execute(text("TRUNCATE TABLE sales_clean;"))
            conn.commit()

    # Step 2: Read Prepared CSV
    print(f"[2/4] Reading cleaned sales dataset from: {CSV_PATH.name} ...")
    df = pd.read_csv(CSV_PATH)
    total_records = len(df)
    print(f"      Total records to load: {total_records:,}")

    # Step 3: Stream Records into MySQL Table in Batches
    print(f"[3/4] Streaming records into 'sales_clean' in batches of {batch_size:,}...")
    loaded_count = 0
    for start_idx in range(0, total_records, batch_size):
        chunk = df.iloc[start_idx : start_idx + batch_size]
        chunk.to_sql(
            name="sales_clean",
            con=engine,
            if_exists="append",
            index=False,
            method="multi"
        )
        loaded_count += len(chunk)
        pct = (loaded_count / total_records) * 100
        sys.stdout.write(f"\r      Progress: {loaded_count:,} / {total_records:,} ({pct:.1f}%)")
        sys.stdout.flush()

    print("\n      [OK] Bulk insert completed successfully!")

    # Step 4: Verification Queries
    print("[4/4] Running automated post-load verification queries...")
    with engine.connect() as conn:
        count_res = conn.execute(text("SELECT COUNT(*) FROM sales_clean;")).scalar()
        rev_res = conn.execute(text("SELECT ROUND(SUM(line_revenue), 2) FROM sales_clean;")).scalar()
        date_range = conn.execute(text("SELECT MIN(invoice_date), MAX(invoice_date) FROM sales_clean;")).fetchone()

    print("=" * 70)
    print("DATABASE LOAD VERIFICATION REPORT")
    print("=" * 70)
    print(f"  * Total Rows Verified in MySQL : {count_res:,} (Expected: {total_records:,})")
    print(f"  * Total Verified Sales Revenue : £{rev_res:,.2f}")
    print(f"  * Earliest Transaction Date    : {date_range[0]}")
    print(f"  * Latest Transaction Date      : {date_range[1]}")
    print("=" * 70)
    print("[SUCCESS] Data pipeline is ready for Power BI dashboard consumption.")


if __name__ == "__main__":
    load_data_to_mysql()
