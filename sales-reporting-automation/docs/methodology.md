# Project Methodology, Technical Architecture & Viva Guide

**Course:** MBA Business Analytics  
**Project:** Business Intelligence and Sales Reporting Automation Using Python, SQL, and Power BI  
**Domain:** Retail E-Commerce Analytics  

---

## 1. End-to-End Pipeline Architecture

```
[ Raw UCI Excel File ]
   (data/raw/Online Retail.xlsx — 541,909 rows)
             │
             ▼
[ Python Cleaning & Validation Pipeline ] (src/clean_data.py)
   ├── Standardize column names
   ├── Parse timestamps (DATETIME) & numerical types
   ├── Detect & separate Cancellations / Returns (Invoice starting with 'C' or Quantity < 0)
   ├── Exclude zero/negative unit prices (damaged items, write-offs)
   ├── Drop exact duplicate rows
   └── Calculate Line Revenue (Quantity * UnitPrice in GBP)
             │
             ├──► [ Clean Sales Data ] (data/processed/sales_clean.csv)
             ├──► [ Cancellations Audit ] (data/processed/sales_cancellations.csv)
             └──► [ Data Quality Report ] (reports/data_quality_summary.csv)
             │
             ▼
[ MySQL Relational Storage ] (sql/schema.sql & src/load_sql.py)
   ├── Structured relational schema with indexing on date, customer, product, country
   ├── Automated batch loading with transaction integrity
   └── Analytical KPI Queries (sql/analysis_queries.sql)
             │
             ▼
[ Power BI Interactive Dashboard ] (powerbi/sales_report.pbix)
   ├── Page 1: Executive Sales Overview
   ├── Page 2: Product & Geographic Deep-Dive
   └── Page 3: Data Quality & Reporting Governance
```

---

## 2. Analytical Decisions & Business Justifications

### 2.1 Separation of Cancellations & Negative Quantities
* **Problem:** Treating negative quantities as ordinary sales lines distorts unit sales, average line values, and invoice counts.
* **Decision:** Invoices starting with `'C'` or lines with `quantity < 0` are extracted into a dedicated `sales_cancellations.csv` audit table. Positive sales are isolated into `sales_clean.csv`.
* **Business Benefit:** Prevents understating gross sales revenue while enabling a distinct returns analysis stream.

### 2.2 Missing Customer IDs
* **Problem:** Approximately 25% of transactions have `customer_id = NULL`.
* **Decision:** These records are preserved in `sales_clean.csv` to ensure that total product revenue, unit counts, and country distributions reflect the true sales volume. However, customer-level queries (e.g. VIP Customer Analysis, RFM segmentation) strictly apply `WHERE customer_id IS NOT NULL`.

### 2.3 Non-Positive Unit Prices
* **Problem:** Some rows have `unit_price <= 0` with descriptions such as `Damaged`, `check`, `lost`, or `amazon adjust`.
* **Decision:** Excluded from the sales population as they represent internal inventory accounting corrections rather than revenue-generating sales transactions.

### 2.4 Gross Line Revenue vs. Profit
* **Definition:** `line_revenue = quantity * unit_price`.
* **Limitation:** This reflects gross transaction value in GBP (£). It is not net accounting profit because product acquisition cost (COGS), shipping charges, VAT, and marketing costs are not available in the dataset.

---

## 3. Power BI Dashboard Design Specifications

### Page 1 — Executive Sales Overview
* **KPI Cards:**
  * `Total Sales Value` (£)
  * `Distinct Invoices`
  * `Units Sold`
  * `Identified Customers`
  * `Average Order Value (AOV)`
* **Visuals:**
  * **Line Chart:** Monthly Sales Trend (X: `invoice_date` by Month, Y: `Total Sales Value`, Legend/Secondary: `Distinct Invoices`).
  * **Clustered Bar Chart:** Top 10 Products by Sales Revenue.
  * **Filled Map / Bar Chart:** Sales Value by Country (UK vs. International).

### Page 2 — Product & Geographic Analysis
* **Visuals:**
  * **Matrix Table:** Product Code, Product Name, Units Sold, Total Revenue, Avg Unit Price.
  * **Donut Chart:** UK vs. Rest of World Revenue Share.
  * **Bar Chart:** Top 10 International Export Markets (excluding UK).
  * **Interactive Slicers:** Date Range Slider, Country Dropdown, Product Search.

### Page 3 — Data Quality & Governance Audit
* **Audit Cards:**
  * Total Raw Rows Ingested vs. Total Cleaned Rows Loaded.
  * Cancellation Rate % (Cancelled Invoices / Total Invoices).
  * Records with Missing Customer ID % (Guest Checkouts).
* **Documentation Card:** Explanatory methodology summary, dataset date range, and pipeline refresh timestamp.

---

## 4. DAX Measures Library

Add these core measures in Power BI under `sales_clean`:

```dax
// 1. Total Gross Sales Value
Total Sales Value = SUM(sales_clean[line_revenue])

// 2. Distinct Invoices Count
Distinct Invoices = DISTINCTCOUNT(sales_clean[invoice_no])

// 3. Total Units Sold
Units Sold = SUM(sales_clean[quantity])

// 4. Identified Customer Accounts
Identified Customers = DISTINCTCOUNT(sales_clean[customer_id])

// 5. Average Line Item Value
Average Sales Line Value = AVERAGE(sales_clean[line_revenue])

// 6. Average Order Value (AOV)
Average Order Value = DIVIDE([Total Sales Value], [Distinct Invoices], 0)

// 7. Average Units Per Transaction Line
Average Units Per Line = AVERAGE(sales_clean[quantity])
```

---

## 5. Viva Voce Preparation Guide (14 Core Questions)

1. **What is the objective of your project?**  
   *Answer:* To build an automated, reproducible end-to-end business intelligence pipeline that extracts raw retail data, cleans it using Python, stores and queries it in MySQL, and visualizes KPIs in Power BI.

2. **Why use the UCI Online Retail dataset?**  
   *Answer:* It provides 541,909 real-world e-commerce transaction records spanning 1 year with timestamps, customer identifiers, product codes, unit prices, and geographic data, providing a comprehensive basis for retail analytics without privacy constraints.

3. **What is the difference between Business Intelligence (BI) and Data Science?**  
   *Answer:* BI focuses on descriptive and diagnostic analytics—understanding past and present business performance through metrics, trends, and dashboards. Data Science emphasizes predictive modeling and machine learning algorithms.

4. **Why was Python used before loading data into SQL?**  
   *Answer:* Python (via `pandas`) handles flexible unstructured transformations: stripping anomalies, standardizing irregular headers, parsing dates, filtering cancellations, removing duplicate lines, and exporting clean CSV files.

5. **Why use SQL in addition to Python?**  
   *Answer:* SQL provides enterprise-grade relational storage, indexing for fast filtering, ACID compliance, and standard declarative querying for repeatable business KPI calculations.

6. **How is Sales Revenue calculated?**  
   *Answer:* Computed for each line item as `Quantity * UnitPrice` in British Pounds (£). Total sales is the aggregation across the cleaned sales population.

7. **How did you handle records with missing Customer IDs?**  
   *Answer:* Retained them for product and geographic sales aggregations so revenue totals remain complete, but explicitly filtered them out (`WHERE customer_id IS NOT NULL`) for customer-centric metrics like top spending buyers or repeat customer counts.

8. **How were cancellations and returns identified?**  
   *Answer:* Identified by invoice numbers starting with `'C'` or `'c'`, or transactions where `quantity < 0`. These were segregated into an audit table to prevent negative values from artificially reducing gross sales.

9. **How do you validate data consistency across tools?**  
   *Answer:* By reconciling KPIs across Python, SQL, and Power BI using the exact same filters: total sales value, invoice count, and date ranges must match across all three platforms.

10. **What does reporting automation achieve?**  
    *Answer:* Replaces manual copy-pasting across Excel sheets with a scripted pipeline that can re-ingest fresh raw data, execute cleaning rules, update database tables, and refresh dashboard visuals in minutes.

11. **What are the key limitations of the dataset?**  
    *Answer:* It covers a historical 1-year window from a single UK retailer. Lacks cost of goods sold (COGS), promotional discounts, and payment methods. Findings represent historical behavior and cannot be assumed to generalize across the entire retail industry.

12. **What is the difference between a Dashboard and a Report?**  
    *Answer:* A dashboard is a high-level single-screen summary designed for rapid monitoring of core KPIs. A report provides multi-page, detailed, interactive drill-down analysis.

13. **Why did you use surrogate keys (`sale_id`) in MySQL?**  
    *Answer:* In retail transaction tables, `invoice_no` is not unique across lines because an invoice can contain multiple items. A surrogate `BIGINT AUTO_INCREMENT` primary key guarantees unique row addressability.

14. **How would you expand this project in production?**  
    *Answer:* Implement incremental ETL loading using Apache Airflow, create a Star Schema with explicit Dimension tables (`Dim_Date`, `Dim_Product`, `Dim_Customer`, `Fact_Sales`), and schedule automatic Power BI Service refreshes via an On-Premises Data Gateway.
