import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv('../datasets/sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month_name()
df['year'] = df['date'].dt.year

# Monthly sales trends
monthly_sales = df.groupby(['year','month'])['sales'].sum().unstack()

plt.figure(figsize=(12,6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trends')
plt.ylabel('Sales ($)')
plt.xlabel('Month')
plt.grid(True)
plt.savefig('../images/monthly_sales.png')
plt.show()

# Product performance
product_perf = df.groupby('product')['sales'].sum().sort_values()

plt.figure(figsize=(10,6))
product_perf.plot(kind='barh')
plt.title('Total Sales by Product')
plt.xlabel('Sales ($)')
#plt.savefig('../images/product_performance.png')
plt.show()
