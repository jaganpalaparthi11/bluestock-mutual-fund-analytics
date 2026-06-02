import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_cols = [
    "return_1y",
    "return_3y",
    "return_5y"
]

for col in return_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Check expense ratio anomalies
if "expense_ratio" in df.columns:

    anomalies = df[
        (df["expense_ratio"] < 0.1)
        |
        (df["expense_ratio"] > 2.5)
    ]

    print("\nExpense Ratio Anomalies:")
    print(len(anomalies))

    anomalies.to_csv(
        "reports/performance_anomalies.csv",
        index=False
    )

# Remove duplicates
df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nSaved Successfully!")