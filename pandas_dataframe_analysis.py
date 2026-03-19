import pandas as pd

# --- Q1: Creating a DataFrame ---
print("--- Q1: Creating a DataFrame from Dictionary ---")
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
    "Region": ["North", "South", "East", "West", "North"],
    "Sales": [1200, 25, 45, 300, 60],
    "Quantity": [2, 10, 5, 1, 3]
}
custom_df = pd.DataFrame(data)
print(custom_df)

# --- Dataset for Questions 2-10 ---
# Load the actual provided dataset
df = pd.read_csv("Retail_dataset.csv")

# --- Q2: Data Inspection ---
print("\n--- Q2: Data Inspection ---")
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nDataset Info:")
df.info()
print("\nDataset Shape:", df.shape)

# --- Q3: Column Selection ---
print("\n--- Q3: Column Selection ---")
selected_cols = df[['Product', 'Region', 'Sales']]
print(selected_cols.head())

# --- Q4: Indexing using .loc ---
print("\n--- Q4: Indexing using .loc ---")
# 1. Row with index 10
print("Row with index 10:\n", df.loc[10])
# 2. Sales value of the row with index 20
print("\nSales value at index 20:", df.loc[20, 'Sales'])

# --- Q5: Indexing using .iloc ---
print("\n--- Q5: Indexing using .iloc ---")
# 1. First 6 rows and first 4 columns
print("First 6 rows and 4 columns:\n", df.iloc[0:6, 0:4])
# 2. Sales value from the 3rd row (index 2)
# Since Sales is the 5th column (index 4)
print("\nSales value from the 3rd row:", df.iloc[2, 4])

# --- Q6: Row Slicing ---
print("\n--- Q6: Row Slicing ---")
print("First 10 rows:\n", df.head(10))
print("\nRows 15 to 25:\n", df.iloc[15:26])

# --- Q7: Filtering Data ---
print("\n--- Q7: Filtering Data ---")
# 1. Region = "East"
east_region = df[df['Region'] == 'East']
print("Rows where Region is East (Count):", len(east_region))
# 2. Sales > 1500
high_sales = df[df['Sales'] > 1500]
print("Rows where Sales > 1500 (Count):", len(high_sales))

# --- Q8: Multiple Condition Filtering ---
print("\n--- Q8: Multiple Condition Filtering ---")
# Region is West AND Sales > 1200
west_high_sales = df[(df['Region'] == 'West') & (df['Sales'] > 1200)]
print("Rows where Region is West and Sales > 1200:\n", west_high_sales)

# --- Q9: Descriptive Statistics ---
print("\n--- Q9: Descriptive Statistics ---")
stats = df.describe()
print(stats)
print("\nMean sales value:", df['Sales'].mean())
print("Maximum quantity sold:", df['Quantity'].max())
print("Minimum sales value:", df['Sales'].min())

# --- Q10: Calculating New Columns ---
print("\n--- Q10: Calculating Total_Value ---")
# Total_Value = Sales * Quantity
df['Total_Value'] = df['Sales'] * df['Quantity']
print(df[['Product', 'Sales', 'Quantity', 'Total_Value']].head())