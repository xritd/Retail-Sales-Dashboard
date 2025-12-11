import pandas as pd

# 1. Load data
df = pd.read_csv('sales_data.csv')

# 2. Quick look
print(df.head())
print(df.info())

# 3. Basic cleaning
df = df.dropna()              
df = df.drop_duplicates()           
df['OrderDate'] = pd.to_datetime(df['OrderDate']) 

df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# 5. Simple summaries
monthly_sales = df.groupby(df['OrderDate'].dt.to_period('M'))['TotalSales'].sum()
region_sales = df.groupby('Region')['TotalSales'].sum()
product_sales = df.groupby('Product')['TotalSales'].sum()

# 6. Save cleaned data for Power BI and SQL
df.to_csv('sales_cleaned.csv', index=False)

# 7. Save summaries
region_sales.to_csv('summary_region.csv')
product_sales.to_csv('summary_product.csv')

print("Data file cleaned and stored.")