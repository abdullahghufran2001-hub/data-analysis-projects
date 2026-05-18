# =========================================================
# COMPLETE EXCEL DATA SUMMARY DASHBOARD
# USING PANDAS + PLOTLY
# =========================================================

# INSTALL LIBRARIES FIRST
# pip install pandas plotly openpyxl

# =========================================================
# IMPORT LIBRARIES
# =========================================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# LOAD EXCEL FILE
# =========================================================

file_path = r"C:/Users/user/Downloads/38134 (1).xlsx"

df = pd.read_excel(file_path)

# =========================================================
# SHOW BASIC DATA
# =========================================================

print("\n================ FIRST 5 ROWS ================\n")
print(df.head())

print("\n================ DATA INFO ================\n")
print(df.info())

print("\n================ NULL VALUES ================\n")
print(df.isnull().sum())

print("\n================ STATISTICAL SUMMARY ================\n")
print(df.describe())

# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = df.columns.str.strip()

print("\n================ COLUMN NAMES ================\n")
print(df.columns)

# =========================================================
# CONVERT DATE COLUMN
# =========================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])

# =========================================================
# CREATE MONTH COLUMN
# =========================================================

df['Month'] = df['Order Date'].dt.strftime('%Y-%m')

# =========================================================
# OVERALL SUMMARY
# =========================================================

total_sales = df['Sales Amount'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
total_orders = df['Order ID'].nunique()

print("\n================ OVERALL SUMMARY ================\n")

print(f"Total Sales      : {total_sales}")
print(f"Total Profit     : {total_profit}")
print(f"Total Quantity   : {total_quantity}")
print(f"Total Orders     : {total_orders}")

# =========================================================
# CATEGORY WISE SALES
# =========================================================

category_sales = (
    df.groupby('Product Category')['Sales Amount']
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x='Product Category',
    y='Sales Amount',
    text_auto=True,
    title='Category Wise Sales'
)

fig1.update_layout(
    title_x=0.5,
    height=500
)

fig1.show()

# =========================================================
# CATEGORY WISE PROFIT
# =========================================================

category_profit = (
    df.groupby('Product Category')['Profit']
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category_profit,
    x='Product Category',
    y='Profit',
    text_auto=True,
    title='Category Wise Profit'
)

fig2.update_layout(
    title_x=0.5,
    height=500
)

fig2.show()

# =========================================================
# CITY WISE SALES
# =========================================================

city_sales = (
    df.groupby('City')['Sales Amount']
    .sum()
    .reset_index()
)

fig3 = px.pie(
    city_sales,
    names='City',
    values='Sales Amount',
    title='City Wise Sales Distribution'
)

fig3.update_layout(
    title_x=0.5,
    height=600
)

fig3.show()

# =========================================================
# TOP 10 PRODUCTS BY SALES
# =========================================================

top_products = (
    df.groupby('Product Name')['Sales Amount']
    .sum()
    .reset_index()
)

top_products = top_products.sort_values(
    by='Sales Amount',
    ascending=False
).head(10)

fig4 = px.bar(
    top_products,
    x='Product Name',
    y='Sales Amount',
    text_auto=True,
    title='Top 10 Products by Sales'
)

fig4.update_layout(
    title_x=0.5,
    height=550
)

fig4.show()

# =========================================================
# MONTHLY SALES TREND
# =========================================================

monthly_sales = (
    df.groupby('Month')['Sales Amount']
    .sum()
    .reset_index()
)

fig5 = px.line(
    monthly_sales,
    x='Month',
    y='Sales Amount',
    markers=True,
    title='Monthly Sales Trend'
)

fig5.update_layout(
    title_x=0.5,
    height=500
)

fig5.show()

# =========================================================
# MONTHLY PROFIT TREND
# =========================================================

monthly_profit = (
    df.groupby('Month')['Profit']
    .sum()
    .reset_index()
)

fig6 = px.area(
    monthly_profit,
    x='Month',
    y='Profit',
    title='Monthly Profit Trend'
)

fig6.update_layout(
    title_x=0.5,
    height=500
)

fig6.show()

# =========================================================
# QUANTITY DISTRIBUTION
# =========================================================

fig7 = px.histogram(
    df,
    x='Quantity',
    nbins=20,
    title='Quantity Distribution'
)

fig7.update_layout(
    title_x=0.5,
    height=500
)

fig7.show()

# =========================================================
# SALES VS PROFIT
# =========================================================

fig8 = px.scatter(
    df,
    x='Sales Amount',
    y='Profit',
    color='Product Category',
    size='Quantity',
    title='Sales vs Profit'
)

fig8.update_layout(
    title_x=0.5,
    height=600
)

fig8.show()

# =========================================================
# CUSTOMER WISE SALES
# =========================================================

customer_sales = (
    df.groupby('Customer Name')['Sales Amount']
    .sum()
    .reset_index()
)

customer_sales = customer_sales.sort_values(
    by='Sales Amount',
    ascending=False
).head(10)

fig9 = px.bar(
    customer_sales,
    x='Customer Name',
    y='Sales Amount',
    text_auto=True,
    title='Top Customers by Sales'
)

fig9.update_layout(
    title_x=0.5,
    height=550
)

fig9.show()

# =========================================================
# SAVE SUMMARY REPORT
# =========================================================

summary_df = pd.DataFrame({

    'Metric': [
        'Total Sales',
        'Total Profit',
        'Total Quantity',
        'Total Orders'
    ],

    'Value': [
        total_sales,
        total_profit,
        total_quantity,
        total_orders
    ]
})

summary_df.to_excel(
    'summary_report.xlsx',
    index=False
)

print("\n================================================")
print("SUMMARY REPORT SAVED SUCCESSFULLY")
print("File Name : summary_report.xlsx")
print("================================================")

# =========================================================
# SAVE CLEAN DATA
# =========================================================

df.to_excel(
    'cleaned_data.xlsx',
    index=False
)

print("\nCleaned data saved as cleaned_data.xlsx")

# =========================================================
# END
# =========================================================
