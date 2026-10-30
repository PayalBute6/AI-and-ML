-- =============================================================================
-- Database Schema: Retail Sales Analytics & Reporting Automation
-- Course: MBA Business Analytics
-- Database Engine: MySQL 8.x
-- =============================================================================

-- Step 1: Create Database
CREATE DATABASE IF NOT EXISTS sales_analytics
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE sales_analytics;

-- Step 2: Main Reporting Table (Clean Positive Sales)
DROP TABLE IF EXISTS sales_clean;

CREATE TABLE sales_clean (
    sale_id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Surrogate primary key',
    invoice_no VARCHAR(20) NOT NULL COMMENT 'Transaction invoice number',
    stock_code VARCHAR(30) NOT NULL COMMENT 'Product item code',
    description VARCHAR(255) COMMENT 'Product item description',
    quantity INT NOT NULL COMMENT 'Quantity purchased (positive integers)',
    invoice_date DATETIME NOT NULL COMMENT 'Timestamp of transaction',
    unit_price DECIMAL(12, 4) NOT NULL COMMENT 'Price per unit in GBP',
    customer_id VARCHAR(20) DEFAULT NULL COMMENT 'Customer identifier (nullable for guest orders)',
    country VARCHAR(100) DEFAULT 'Unspecified' COMMENT 'Customer country',
    line_revenue DECIMAL(14, 4) NOT NULL COMMENT 'Computed line total (quantity * unit_price)',
    
    -- Performance Indexes for Dashboard & Reporting Queries
    INDEX idx_invoice_date (invoice_date),
    INDEX idx_customer_id (customer_id),
    INDEX idx_stock_code (stock_code),
    INDEX idx_country (country),
    INDEX idx_invoice_no (invoice_no)
) ENGINE=InnoDB COMMENT='Clean positive retail sales transactions for BI reporting';

-- Step 3: Staging Table for Controlled Full Pipeline Reloads
DROP TABLE IF EXISTS sales_staging;

CREATE TABLE sales_staging (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(30),
    description VARCHAR(255),
    quantity INT,
    invoice_date DATETIME,
    unit_price DECIMAL(12, 4),
    customer_id VARCHAR(20),
    country VARCHAR(100),
    line_revenue DECIMAL(14, 4)
) ENGINE=InnoDB COMMENT='Staging table for validating and loading pipeline batches';

-- Step 4: Cancellations & Returns Audit Table
DROP TABLE IF EXISTS sales_cancellations;

CREATE TABLE sales_cancellations (
    cancellation_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    invoice_no VARCHAR(20) NOT NULL,
    stock_code VARCHAR(30) NOT NULL,
    description VARCHAR(255),
    quantity INT NOT NULL COMMENT 'Negative quantity representing returns',
    invoice_date DATETIME NOT NULL,
    unit_price DECIMAL(12, 4) NOT NULL,
    customer_id VARCHAR(20),
    country VARCHAR(100),
    line_revenue DECIMAL(14, 4),
    INDEX idx_canc_date (invoice_date),
    INDEX idx_canc_customer (customer_id)
) ENGINE=InnoDB COMMENT='Separated cancellations and returns for audit analysis';
