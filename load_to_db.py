import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/nav_history_clean.csv")
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Save to SQLite
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")
print("fact_nav rows:", len(nav))
print("fact_transactions rows:", len(transactions))
print("fact_performance rows:", len(performance))