# Business Intelligence and Sales Reporting Automation Using Python, SQL, and Power BI

**Course:** MBA — Business Analytics  
**Domain:** Retail & E-Commerce Analytics  
**Project Type:** Industry-Oriented, OJT-Style Applied Analytics Project  

---

## 📌 1. Project Overview

Retail decision-makers depend on reliable, automated reporting to answer mission-critical commercial questions:
- Which products and geographic markets generate the highest sales revenue?
- How does sales volume and revenue trend across months and seasons?
- What proportion of transactions are cancellations or customer returns?
- How can routine sales reports be prepared consistently with minimal manual intervention?

This project develops an end-to-end, reproducible business intelligence pipeline that:
1. **Cleans and standardizes** raw e-commerce transaction data using **Python (`pandas`, `openpyxl`)**.
2. **Stores and queries** clean records in a **MySQL relational database** using structured schemas and performance indexing.
3. **Calculates commercial KPIs** through optimized **SQL** analytical scripts.
4. **Visualizes business performance** in an interactive multi-page **Power BI dashboard** powered by custom DAX measures.

---

## 📁 2. Project Directory Structure

```
sales-reporting-automation/
├── data/
│   ├── raw/                 # Original, untouched UCI dataset (Online Retail.xlsx)
│   └── processed/           # Cleaned sales and segregated cancellations CSVs
├── docs/
│   ├── data_dictionary.md   # Field descriptions, data types, and cleaning rules
│   └── methodology.md       # Pipeline architecture, Power BI layout, & viva guide
├── notebooks/               # Exploratory data analysis (EDA) Jupyter notebooks
├── powerbi/                 # Power BI report file (.pbix) and wireframe templates
├── reports/                 # Quality audit summaries, charts, and final reports
├── sql/
│   ├── schema.sql           # MySQL database and table creation script with indexing
│   └── analysis_queries.sql # Analytical SQL queries for KPIs, trends, and validation
├── src/
│   ├── download_dataset.py  # Automated script to fetch dataset directly from UCI
│   ├── clean_data.py        # Automated data cleaning, validation, and export pipeline
│   └── load_sql.py          # Batch loader streaming processed data into MySQL
├── requirements.txt         # Python library dependencies
├── .gitignore               # Excludes virtual environments, raw data, and credentials
└── README.md                # Comprehensive project documentation
```

---

## 🛠️ 3. Technology Stack

| Layer | Technology | Primary Function |
| :--- | :--- | :--- |
| **Data Extraction & Ingestion** | Python 3.13, `urllib` | Automated dataset retrieval and archive extraction |
| **Data Cleaning & Validation** | `pandas`, `openpyxl`, `numpy` | Data type casting, duplicate removal, cancellation segregation, revenue calculation |
| **Relational Database** | MySQL Community Server 8.x | Structured storage, surrogate primary keys, and multi-column indexes |
| **Database Connector** | `SQLAlchemy`, `PyMySQL` | Automated, chunked batch loading from Python to MySQL |
| **Business Intelligence** | Microsoft Power BI Desktop, DAX | Executive KPI cards, monthly trends, Pareto charts, and data quality audits |
| **Version Control** | Git & GitHub | Code versioning, portfolio publishing, and documentation tracking |

---

## 📊 4. Dataset Information

* **Source:** [UCI Machine Learning Repository — Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
* **Dataset Scope:** 541,909 raw transaction records from a UK-based online gifts retailer between **December 1, 2010 and December 9, 2011**.
* **Key Fields:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.

---

## ⚙️ 5. Step-by-Step Execution Guide

### Step 5.1 — Environment Setup
```bash
# Navigate to project folder
cd sales-reporting-automation

# Create and activate a Python virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # In PowerShell (or .venv\Scripts\activate.bat in CMD)

# Install required packages
python -m pip install -r requirements.txt
```

### Step 5.2 — Dataset Download
```bash
# Automatically fetch and extract the UCI dataset into data/raw/
python src/download_dataset.py
```

### Step 5.3 — Data Cleaning & Quality Audit
```bash
# Executes data standardization, removes duplicates, segregates returns, and generates CSVs
python src/clean_data.py
```
*Outputs generated:*
- `data/processed/sales_clean.csv` — Positive sales records for reporting.
- `data/processed/sales_cancellations.csv` — Separated cancellation/return records for audit.
- `reports/data_quality_summary.csv` — Complete data hygiene audit metrics.

### Step 5.4 — Database Setup & Data Loading
1. Open **MySQL Workbench** and execute [`sql/schema.sql`](file:///f:/AI%20and%20ML/sales-reporting-automation/sql/schema.sql) to create `sales_analytics` database and indexed tables.
2. Set your MySQL credentials in PowerShell:
```powershell
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="your_password"
$env:MYSQL_HOST="localhost"
$env:MYSQL_PORT="3306"

# Load the clean dataset into MySQL
python src/load_sql.py
```

### Step 5.5 — Run Analytical Queries
Execute [`sql/analysis_queries.sql`](file:///f:/AI%20and%20ML/sales-reporting-automation/sql/analysis_queries.sql) in MySQL Workbench to answer core business questions:
- Overall performance KPIs (Total Sales, Invoices, Units, Customers, AOV).
- Month-over-month revenue and volume growth trends.
- Top 10 revenue-generating products.
- Geographic sales distribution across countries.
- Top 20 VIP/wholesale identified accounts.
- Automated data integrity audit.

### Step 5.6 — Power BI Dashboard
1. Open **Power BI Desktop**.
2. Select **Get Data → Text/CSV** and import `data/processed/sales_clean.csv` (or connect directly to MySQL).
3. Implement the DAX measures defined in [`docs/methodology.md`](file:///f:/AI%20and%20ML/sales-reporting-automation/docs/methodology.md).
4. Build the 3 dashboard pages:
   - **Page 1: Executive Sales Overview**
   - **Page 2: Product & Geographic Analysis**
   - **Page 3: Data Quality & Governance**

---

## 📈 6. Verified Pipeline Execution & KPI Results

The following benchmark metrics were verified from executing `src/clean_data.py` on the complete UCI dataset:

| Pipeline Audit Metric | Measured Value | Business Interpretation |
| :--- | :--- | :--- |
| **Total Ingested Records** | `541,909` | Complete raw historical transaction dataset |
| **Exact Duplicates Removed** | `5,268` | Duplicate order lines purged to prevent double-counting |
| **Cancellations / Returns Segregated** | `10,587` | Invoices prefixed with 'C' and negative quantities routed to audit table |
| **Zero / Negative Price Rows Purged** | `1,176` | Administrative samples, write-offs, and damaged inventory entries |
| **Clean Positive Sales Records** | `524,878` | Final dataset for SQL analytics & Power BI reporting |
| **Missing Customer IDs (Sales)** | `132,186` (25.18%) | Guest checkouts (included in product/country sales, excluded in customer KPIs) |
| **Transaction Date Range** | `2010-12-01` to `2011-12-09` | 373 days of active e-commerce retail activity |
| **Total Gross Sales Revenue** | **£10,642,110.80** | Total gross merchandise value (GMV) in British Pounds |
| **Total Units Sold** | **5,572,420** units | Total volume of physical products dispatched |
| **Distinct Sales Invoices** | **19,960** orders | Unique valid customer orders placed |
| **Identified Customer Accounts** | **4,338** buyers | Unique registered retail & wholesale clients |
| **Average Order Value (AOV)** | **£533.17** | Mean gross revenue per unique order invoice |

---

## 🎯 7. Core Business KPI Definitions

* **Gross Sales Revenue (£):** $\sum (\text{Quantity} \times \text{UnitPrice})$ for positive sales records.
* **Average Order Value (AOV):** $\frac{\text{Total Sales Revenue}}{\text{Distinct Invoices Count}} = \frac{£10,642,110.80}{19,960} = £533.17$.
* **Cancellation Rate (%):** $\frac{\text{Cancelled Invoices}}{\text{Total Invoices Received}} \times 100$.

---

## ⚠️ 7. Analytical Limitations

1. **Gross Revenue vs. Net Profit:** Product cost (COGS), shipping overhead, VAT, and marketing expenditure are not present in the dataset; line revenue reflects gross transaction value, not company net profit.
2. **Missing Customer Identifiers:** Guest checkouts (~25% of records) contribute to product and country revenue but are excluded from customer-level grouping.
3. **Historical Single-Firm Scope:** Data represents a single UK gift retailer from 2010–2011; findings illustrate real analytics pipelines but cannot be generalized to contemporary broader retail markets.

---

## 👥 Author & Academic Context

* **Program:** MBA in Business Analytics
* **Project Title:** Business Intelligence and Sales Reporting Automation
* **Course:** Business Intelligence, Data Engineering & Applied Analytics
