# 🛍️ ShopNile — Data Analysis & Business Intelligence Project

> **Your One-Stop Online Marketplace**  
> A full data pipeline project: from raw messy data to an interactive business dashboard.

---

## 📌 Project Overview

ShopNile is a comprehensive data analysis project for a fictional online marketplace. It covers the full data pipeline — from raw messy data to a fully interactive business dashboard — demonstrating real-world skills in **data cleaning**, **transformation**, and **visualization**.

---

## 📁 Project Structure

```
ShopNile/
│
├── raw_data/
│   ├── customers_messy.csv
│   ├── orders_messy.csv
│   ├── payments_messy.csv
│   └── products_messy.csv
│
├── clean_data/
│   ├── Customers_Clean.csv
│   ├── Orders_Clean.csv
│   ├── Payments_Clean.csv
│   └── Products_Clean.csv
│
├── ShopNile_Cleaning.ipynb   # Data cleaning pipeline
├── ShopNile_Analysis.py      # Streamlit dashboard
└── ShopNile_Logo.png
```

---

## 🗄️ Data Model

The project follows a **Star Schema**:

| Table | Type | Key Column | Records |
|---|---|---|---|
| Customers_Clean | Dimension | `customer_id` | 500 |
| Products_Clean | Dimension | `product_id` | 120 |
| Orders_Clean | Fact | `order_id` | 3,000 |
| Payments_Clean | Fact | `order_id` | 3,050 |

**Relationships:**
- `Orders` → `Customers` via `customer_id`
- `Orders` → `Products` via `product_id`
- `Orders` → `Payments` via `order_id`

---

## 🧹 Data Cleaning — `ShopNile_Cleaning.ipynb`

Key cleaning steps applied to all four raw datasets:

- ✅ Removed duplicate rows and fixed inconsistent primary/foreign keys
- ✅ Handled missing values through imputation or removal
- ✅ Standardized date formats across all date columns
- ✅ Corrected data type mismatches (e.g. numeric fields stored as strings)
- ✅ Fixed invalid categorical values (e.g. payment status, city names)
- ✅ Removed/capped outliers in numeric columns (price, amount_paid, income)
- ✅ Normalized text fields (name casing, trimming whitespace)

---

## 📊 Dashboard — `ShopNile_Analysis.py`

Built with **Streamlit** and **Plotly Express**.

### KPI Cards
| Metric | Description |
|---|---|
| 💰 Total Revenue | Sum of all payments |
| 📦 Total Orders | Count of unique orders |
| 👥 Total Customers | Count of unique customers |

### Charts
| Chart | Type | Description |
|---|---|---|
| Sales by Category | Pie Chart | Revenue breakdown across product categories |
| Sales by City | Bar Chart | Revenue ranked by customer city |
| Sales by Payment Method | Pie Chart | Revenue split by payment method |
| Sales Over Time | Line Chart | Quarterly revenue trend |
| Top 10 Products | Bar Chart | Highest-revenue products by name |

### Interactivity
- 🔽 **Category Slicer** — filters all charts and KPIs by product category

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Pandas | Data manipulation and cleaning |
| Jupyter Notebook | Interactive data cleaning documentation |
| Streamlit | Web-based dashboard framework |
| Plotly Express | Interactive chart rendering |

---

## 🚀 How to Run

**1. Install dependencies**
```bash
pip install streamlit pandas plotly
```

**2. Place the clean CSV files** inside a folder named `clean_data/`

**3. Run the dashboard**
```bash
streamlit run ShopNile_Analysis.py
```

**4. Open your browser and go to** → `http://localhost:8501`

---

## 📂 Dataset Overview

| Column | Table | Description |
|---|---|---|
| `customer_id` | Customers | Unique customer identifier |
| `name`, `age`, `city` | Customers | Customer demographics |
| `signup_date`, `income` | Customers | Registration and financial info |
| `product_id` | Products | Unique product identifier |
| `product_name`, `category` | Products | Product details |
| `price`, `stock` | Products | Pricing and inventory |
| `order_id` | Orders | Unique order identifier |
| `quantity`, `discount` | Orders | Order details |
| `order_date`, `payment_method` | Orders | Transaction info |
| `amount_paid`, `payment_status` | Payments | Payment details |

---
## Dashboard URL
```
https://shopnile-analysis-using-python-h9bbtrwmjconbq49mfkc8f.streamlit.app
```

*ShopNile — Data Analysis Portfolio Project*
