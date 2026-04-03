import pandas as pd

# STEP 1: Load dataset
df = pd.read_csv("ecommerce_dataset_updated.csv")

# STEP 2: Data Cleaning

#Missing values check
print("\nMissing Values:\n", df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date column
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], dayfirst=True, errors='coerce')

# STEP 3 : Create Month column
df['Month'] = df['Purchase_Date'].dt.to_period('M')
print(df)

# STEP 3: Total Revenue (Sales)

total_sales = df['Final_Price(Rs.)'].sum()
print("\nTotal Revenue:", total_sales)


# # STEP 4: Top Selling Category

top_category = df.groupby('Category')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
print("\nTop Categories:\n", top_category)


# # STEP 5: Payment Method Analysis

payment_sales = df.groupby('Payment_Method')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
print("\nPayment Method Sales:\n", payment_sales)

# # STEP 6: Discount vs Revenue

discount_analysis = df.groupby('Discount (%)')['Final_Price(Rs.)'].mean()
print("\nDiscount Impact:\n", discount_analysis)

# # STEP 7: Customer Analysis

top_users = df.groupby('User_ID')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
print("\nTop Customers:\n", top_users.head())

output_path = r"c:\\Users\Education\\Downloads\\ecommerce_dataset_updated.csv"
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned data saved at: {output_path}")