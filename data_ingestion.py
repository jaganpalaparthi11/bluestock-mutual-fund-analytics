import pandas as pd
import os

# Folder containing all CSV files
folder_path = "data/raw"

print("=" * 60)
print("MUTUAL FUND ANALYTICS - DATA INGESTION REPORT")
print("=" * 60)

# Loop through all CSV files
for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        print("\n" + "=" * 60)
        print(f"FILE NAME: {file}")
        print("=" * 60)

        try:
            # Read CSV
            df = pd.read_csv(file_path)

            # Shape
            print("\nSHAPE:")
            print(df.shape)

            # Columns
            print("\nCOLUMNS:")
            print(df.columns.tolist())

            # Data Types
            print("\nDATA TYPES:")
            print(df.dtypes)

            # Missing Values
            print("\nMISSING VALUES:")
            print(df.isnull().sum())

            # Duplicate Rows
            print("\nDUPLICATE ROWS:")
            print(df.duplicated().sum())

            # First 5 Rows
            print("\nFIRST 5 ROWS:")
            print(df.head())

        except Exception as e:
            print(f"\nERROR READING FILE: {e}")

print("\n" + "=" * 60)
print("DATA INGESTION COMPLETED")
print("=" * 60)