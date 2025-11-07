# Retail-Sales-Insights Analysis & Dashboard
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12,6)

# -------------------------
# 0️⃣ Folders Setup
# -------------------------
if not os.path.exists('dashboard'):
    os.makedirs('dashboard')

if not os.path.exists('insights'):
    os.makedirs('insights')

# -------------------------
# 1️⃣ Load dataset
# -------------------------
df = pd.read_csv('data/retail_sales_india.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# -------------------------
# 2️⃣ Revenue & Profit Analysis
# -------------------------
city_revenue = df.groupby('Store City')['Revenue'].sum().sort_values(ascending=False)
city_profit = df.groupby('Store City')['Profit'].sum().sort_values(ascending=False)
category_revenue = df.groupby('Product Category')['Revenue'].sum().sort_values(ascending=False)

# Profit Margin %
df['Profit Margin %'] = (df['Profit'] / df['Revenue']) * 100
category_profit_margin = df.groupby('Product Category')['Profit Margin %'].mean().sort_values(ascending=False)

# -------------------------
# 3️⃣ Monthly & Yearly Trends
# -------------------------
monthly_revenue = df.groupby(['Year','Month'])['Revenue'].sum().reset_index()
plt.figure(figsize=(14,6))
sns.lineplot(data=monthly_revenue, x='Month', y='Revenue', hue='Year', marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend(title='Year')
plt.savefig('dashboard/monthly_revenue_trend.png', bbox_inches='tight')
plt.show()

yearly_revenue = df.groupby('Year')['Revenue'].sum()
plt.figure(figsize=(8,5))
sns.barplot(x=yearly_revenue.index, y=yearly_revenue.values, palette='Blues_d')
plt.title('Yearly Revenue Trend')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.savefig('dashboard/yearly_revenue.png', bbox_inches='tight')
plt.show()

# -------------------------
# 4️⃣ Top Products & Categories
# -------------------------
top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Product Name')
plt.savefig('dashboard/top_products.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=category_revenue.values, y=category_revenue.index, palette='magma')
plt.title('Revenue by Product Category')
plt.xlabel('Revenue')
plt.ylabel('Category')
plt.savefig('dashboard/category_revenue.png', bbox_inches='tight')
plt.show()

# -------------------------
# 5️⃣ Discount Analysis
# -------------------------
category_discount = df.groupby('Product Category')['Discount %'].mean().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=category_discount.values, y=category_discount.index, palette='coolwarm')
plt.title('Average Discount % per Category')
plt.xlabel('Discount %')
plt.ylabel('Category')
plt.savefig('dashboard/avg_discount_category.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Discount %', y='Revenue', hue='Product Category', alpha=0.7)
plt.title('Discount % vs Revenue')
plt.xlabel('Discount %')
plt.ylabel('Revenue')
plt.savefig('dashboard/discount_vs_revenue.png', bbox_inches='tight')
plt.show()

# -------------------------
# 6️⃣ Pivot Table for Dashboard
# -------------------------
pivot = df.pivot_table(index='Store City', columns='Product Category', values='Revenue', aggfunc='sum')

# -------------------------
# 7️⃣ Write Insights to File
# -------------------------
insights_text = f"""
# Retail Sales Insights - India

## Key Findings

1. Top Revenue Cities: {', '.join(city_revenue.index[:3])}
2. Top Profit Cities: {', '.join(city_profit.index[:3])}
3. Top Revenue Category: {category_revenue.idxmax()} with total revenue {category_revenue.max():,.2f}
4. Highest Profit Margin Category: {category_profit_margin.idxmax()} with avg margin {category_profit_margin.max():.2f}%
5. Month with highest revenue (combined across years): {monthly_revenue.loc[monthly_revenue['Revenue'].idxmax(), 'Month']}
6. Year with highest total revenue: {yearly_revenue.idxmax()} with revenue {yearly_revenue.max():,.2f}
7. Discounts slightly increase revenue for Fashion category.
"""

with open('insights/README.md', 'w') as f:
    f.write(insights_text)

print("✅ Dashboard charts saved in 'dashboard/' and insights written to 'insights/README.md'")

