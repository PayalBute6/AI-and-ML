# Data Dictionary & Source Documentation

## 1. Dataset Overview

* **Dataset Title:** Online Retail Dataset
* **Source:** UCI Machine Learning Repository
* **Direct URL:** [https://archive.ics.uci.edu/dataset/352/online+retail](https://archive.ics.uci.edu/dataset/352/online+retail)
* **Domain:** Retail & E-Commerce Analytics
* **Total Raw Records:** 541,909 transaction line items
* **Time Period:** 01/12/2010 to 09/12/2011 (December 1, 2010 – December 9, 2011)
* **Company Context:** UK-based online retail business selling unique all-occasion gifts; many customers are wholesalers.

---

## 2. Field Descriptions & Data Types

| Original Column | Standardized Column | Data Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceNo` | `invoice_no` | `VARCHAR(20)` | No | 6-digit invoice code. If code begins with letter **'C'**, it represents a **cancellation / return**. |
| `StockCode` | `stock_code` | `VARCHAR(30)` | No | 5-digit product identifier or special transaction code (e.g., `POST`, `D`, `M`). |
| `Description` | `description` | `VARCHAR(255)`| Yes | Product name / item description. |
| `Quantity` | `quantity` | `INT` | No | Number of units purchased per transaction line. Negative values indicate cancellations, returns, or inventory adjustments. |
| `InvoiceDate` | `invoice_date` | `DATETIME` | No | Timestamp of transaction generation (Day, Month, Year, Hour, Minute). |
| `UnitPrice` | `unit_price` | `DECIMAL(12,4)`| No | Product unit price in British Pounds Sterling (£ / GBP). |
| `CustomerID` | `customer_id` | `VARCHAR(20)` | Yes | Unique 5-digit customer identifier. Missing values occur for guest checkouts or unregistered buyers. |
| `Country` | `country` | `VARCHAR(100)`| Yes | Geographic location / country of the customer. |
| *Calculated* | `line_revenue` | `DECIMAL(14,4)`| No | Computed as `quantity * unit_price`. Represents transaction gross line value (in GBP). |

---

## 3. Data Quality & Business Rules

### 3.1 Cancellations & Returns
* Invoices prefixed with **`C`** (e.g., `C536379`) or records with **`Quantity < 0`** represent order cancellations, customer returns, or bad debt adjustments.
* **Pipeline Rule:** In `src/clean_data.py`, these rows are separated into `data/processed/sales_cancellations.csv` for audit and returns analysis, ensuring they do not artificially distort positive sales calculations.

### 3.2 Handling Missing Customer IDs
* Approximately 25% of raw records lack a `CustomerID`.
* **Pipeline Rule:** Retained in the main sales reporting table (`sales_clean.csv`) to preserve accurate product and geographic revenue aggregates. However, customer-level grouping queries (e.g. VIP customer rankings, RFM analysis) explicitly filter out `customer_id IS NULL`.

### 3.3 Zero or Negative Unit Prices
* Transactions with `unit_price <= 0` generally correspond to damaged goods, inventory write-offs, samples, or administrative test records (e.g., descriptions like `Damaged`, `check`, `lost`).
* **Pipeline Rule:** Filtered out of standard sales revenue reporting.

### 3.4 Duplicate Transactions
* Exact duplicates across all columns are logged and removed during cleaning.

---

## 4. Analytical Scope & Disclaimers

1. **Revenue vs. Profit:** `line_revenue` is gross transaction revenue (`Quantity × UnitPrice`); it does not represent net accounting profit (costs, shipping fees, tax, and overhead are not recorded).
2. **Historical Context:** Historical transaction data from a single UK online gift retailer (2010–2011). Does not reflect contemporary retail market conditions.
