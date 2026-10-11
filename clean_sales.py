import pandas as pd

df = pd.read_csv("messy_sales.csv")

print("Original data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)

# Handle missing values
df["Product"] = df["Product"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Sales"] = df["Sales"].fillna(df["Sales"].median())

print("\nCleaned data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Export cleaned data
df.to_csv("cleaned_sales.csv", index=False)
df.to_excel("cleaned_sales.xlsx", index=False)

print("\nCleaned CSV and Excel files saved!")