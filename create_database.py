from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Force creation by connecting
with engine.connect():
    pass

print("SQLite Database Created Successfully!")