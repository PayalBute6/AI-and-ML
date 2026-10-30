-- =============================================================================
-- Retail Sales Analytical & Business Intelligence Queries
-- Database: sales_analytics
-- Target Table: sales_clean
-- =============================================================================

USE sales_analytics;

-- -----------------------------------------------------------------------------
-- Query 1: Overall Performance KPIs
-- Business Question: What is the overall scale, revenue, and customer base?
-- Used for: Power BI Executive Dashboard Summary KPI Cards
-- -----------------------------------------------------------------------------
SELECT 
    ROUND(SUM(line_revenue), 2)         AS total_sales_value_gbp,
    COUNT(DISTINCT invoice_no)          AS distinct_invoices,
    SUM(quantity)                       AS total_units_sold,
    COUNT(DISTINCT customer_id)         AS identified_customers,
    ROUND(AVG(line_revenue), 2)         AS average_line_value_gbp,
    ROUND(SUM(line_revenue) / COUNT(DISTINCT invoice_no), 2) AS average_order_value_gbp
FROM sales_clean;

-- -----------------------------------------------------------------------------
-- Query 2: Monthly Sales Trend
-- Business Question: How does revenue, transaction volume, and unit demand change over time?
-- Used for: Monthly Revenue & Order Volume Line/Area Charts
-- -----------------------------------------------------------------------------
SELECT 
    DATE_FORMAT(invoice_date, '%Y-%m')  AS sales_month,
    ROUND(SUM(line_revenue), 2)         AS sales_value,
    COUNT(DISTINCT invoice_no)          AS invoice_count,
    SUM(quantity)                       AS units_sold,
    COUNT(DISTINCT customer_id)         AS active_customers
FROM sales_clean
GROUP BY DATE_FORMAT(invoice_date, '%Y-%m')
ORDER BY sales_month ASC;

-- -----------------------------------------------------------------------------
-- Query 3: Top 10 Products by Sales Revenue
-- Business Question: Which products generate the highest revenue for the business?
-- Used for: Top 10 Product Bar Chart & Inventory Focus
-- -----------------------------------------------------------------------------
SELECT 
    stock_code,
    MAX(description)                    AS product_name,
    SUM(quantity)                       AS units_sold,
    ROUND(SUM(line_revenue), 2)         AS sales_value,
    ROUND(AVG(unit_price), 2)           AS avg_unit_price
FROM sales_clean
GROUP BY stock_code
ORDER BY sales_value DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 4: Geographic / Country Sales Performance
-- Business Question: What is the geographic distribution of revenue and order volume?
-- Used for: Map Visual & International Market Share Table
-- -----------------------------------------------------------------------------
SELECT 
    country,
    ROUND(SUM(line_revenue), 2)         AS sales_value,
    COUNT(DISTINCT invoice_no)          AS invoice_count,
    SUM(quantity)                       AS units_sold,
    ROUND(SUM(line_revenue) * 100.0 / (SELECT SUM(line_revenue) FROM sales_clean), 2) AS pct_total_sales
FROM sales_clean
GROUP BY country
ORDER BY sales_value DESC;

-- -----------------------------------------------------------------------------
-- Query 5: Customer Purchase Summary (Top 20 Identified Customers)
-- Business Question: Who are the top revenue-contributing accounts (Wholesale/VIP)?
-- Used for: Customer Relationship Management & Pareto (80/20) Analysis
-- -----------------------------------------------------------------------------
SELECT 
    customer_id,
    MAX(country)                        AS country,
    COUNT(DISTINCT invoice_no)          AS invoice_count,
    SUM(quantity)                       AS units_purchased,
    ROUND(SUM(line_revenue), 2)         AS sales_value,
    ROUND(AVG(line_revenue), 2)         AS avg_spend_per_line
FROM sales_clean
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY sales_value DESC
LIMIT 20;

-- -----------------------------------------------------------------------------
-- Query 6: Data Pipeline Quality & Integrity Validation
-- Business Question: Are there any nulls, corrupted dates, or invalid negative quantities?
-- Used for: Automated Quality Audit Page & Integrity Verification
-- -----------------------------------------------------------------------------
SELECT 
    COUNT(*)                            AS total_rows,
    SUM(invoice_no IS NULL)             AS missing_invoice_numbers,
    SUM(invoice_date IS NULL)           AS missing_invoice_dates,
    SUM(quantity <= 0)                  AS nonpositive_quantity_rows,
    SUM(unit_price <= 0)                AS nonpositive_price_rows,
    SUM(line_revenue IS NULL)           AS missing_revenue_rows,
    SUM(customer_id IS NULL)            AS unmapped_customer_rows,
    MIN(invoice_date)                   AS first_transaction_date,
    MAX(invoice_date)                   AS last_transaction_date
FROM sales_clean;

-- -----------------------------------------------------------------------------
-- Query 7: Peak Shopping Patterns (Day of Week Analysis)
-- Business Question: On which days do retail customers order the most?
-- -----------------------------------------------------------------------------
SELECT 
    DAYNAME(invoice_date)               AS day_of_week,
    COUNT(DISTINCT invoice_no)          AS order_volume,
    ROUND(SUM(line_revenue), 2)         AS total_sales_value
FROM sales_clean
GROUP BY DAYNAME(invoice_date), DAYOFWEEK(invoice_date)
ORDER BY DAYOFWEEK(invoice_date);
