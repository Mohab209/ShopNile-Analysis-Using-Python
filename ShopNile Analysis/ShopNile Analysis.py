import streamlit as st
import pandas as pd
import plotly.express as px
import os
# Set page config
st.set_page_config(page_title="ShopNile Dashboard", layout="wide")
# Title
st.title("🛍️ ShopNile Dashboard")
# Load Data
@st.cache_data
def load_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    Dim_Customers_DF = pd.read_csv(os.path.join(base_path, "clean_data", "Customers_Clean.csv"))
    Dim_Products_DF = pd.read_csv(os.path.join(base_path, "clean_data", "Products_Clean.csv"))
    Fact_Orders_DF = pd.read_csv(os.path.join(base_path, "clean_data", "Orders_Clean.csv"))
    Fact_Payments_DF = pd.read_csv(os.path.join(base_path, "clean_data", "Payments_Clean.csv"))
    return Dim_Customers_DF, Dim_Products_DF, Fact_Orders_DF, Fact_Payments_DF
# Merge DataFrames
Orders_Payments_DF = pd.merge(Fact_Orders_DF, Fact_Payments_DF, on="order_id", how="inner")
Orders_Customers_DF = pd.merge(Orders_Payments_DF, Dim_Customers_DF, on="customer_id", how="inner")
Orders_Products_DF = pd.merge(Orders_Customers_DF, Dim_Products_DF, on="product_id", how="inner")
# Category Slicer
category = st.multiselect("Choose Category",Orders_Products_DF["category"].unique())
if category:
    filtered_df = Orders_Products_DF[Orders_Products_DF["category"].isin(category)]
else:
    filtered_df = Orders_Products_DF
# KPI Cards
total_revenue = filtered_df["amount_paid"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_id"].nunique()
col1, col2, col3, col4, col5 = st.columns([0.6,0.3,1,1,1])
with col1:
    st.image("ShopNile Logo.png")
col2.metric("","")
col3.metric("Total Revenue", f"${total_revenue:,.0f}")
col4.metric("Total Orders", f"{total_orders:,}")
col5.metric("Total Customers", f"{total_customers:,}")
# Sales by Category
sales_by_category = Orders_Products_DF.groupby("category")["amount_paid"].sum().reset_index()
fig_category = px.pie(sales_by_category, values="amount_paid", names="category", title="Sales by Category", labels={"amount_paid": "Total Sales"})
st.plotly_chart(fig_category, use_container_width=True)
# Sales by City
sales_by_city = filtered_df.groupby("city")["amount_paid"].sum().reset_index().sort_values(by="amount_paid", ascending=False)
fig_city = px.bar(sales_by_city, x="city", y="amount_paid", title="Sales by City", labels={"amount_paid": "Total Sales"})
st.plotly_chart(fig_city, use_container_width=True)
# Sales by Payment Method
sales_by_payment_method = filtered_df.groupby("payment_method")["amount_paid"].sum().reset_index()
fig_payment_method = px.pie(sales_by_payment_method, values="amount_paid", names="payment_method", title="Sales by Payment Method", labels={"amount_paid": "Total Sales"})
st.plotly_chart(fig_payment_method, use_container_width=True)
# Sales Over Time
filtered_df["order_date"] = pd.to_datetime(filtered_df["order_date"])
sales_over_time = filtered_df.groupby(filtered_df["order_date"].dt.to_period("Q"))["amount_paid"].sum().reset_index()
sales_over_time["order_date"] = sales_over_time["order_date"].astype(str)
fig_sales_over_time = px.line(sales_over_time, x="order_date", y="amount_paid", title="Sales Over Time", labels={"amount_paid": "Total Sales"})
st.plotly_chart(fig_sales_over_time, use_container_width=True)
# Top 10 Products
top_products = filtered_df.groupby("product_name")["amount_paid"].sum().reset_index().sort_values(by="amount_paid", ascending=False).head(10)
fig_top_products = px.bar(top_products, x="product_name", y="amount_paid", title="Top 10 Products by Sales", labels={"amount_paid": "Total Sales"})

st.plotly_chart(fig_top_products, use_container_width=True)


