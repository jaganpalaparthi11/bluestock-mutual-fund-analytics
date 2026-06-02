import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Remove invalid amounts
df = df[df["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nSaved Successfully!")