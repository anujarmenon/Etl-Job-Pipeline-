import pandas as pd
import sqlite3

# Reads the cleaned data produced by clean.py
df = pd.read_csv("cleaned_jobs.csv")

# Connects to (or creates) a SQLite database file
conn = sqlite3.connect("jobs.db")

# Writes the DataFrame into a table called 'jobs', replacing it if it already exists
df.to_sql("jobs", conn, if_exists="replace", index=False)

# Quick check: counts how many rows actually made it into the database
count = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]
print(f"Success! Loaded {count} rows into jobs.db (table: jobs)")

conn.close()