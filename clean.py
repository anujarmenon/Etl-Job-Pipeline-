import json
import pandas as pd

# Loads the raw API response saved during extraction
with open("raw_jobs.json", "r") as f:
    data = json.load(f)

jobs = data["results"]

# Flattens nested fields (e.g. company, location) into a simple flat structure
rows = []
for job in jobs:
    rows.append({
        "title": job.get("title"),
        "company": job.get("company", {}).get("display_name"),
        "location": job.get("location", {}).get("display_name"),
        "salary_min": job.get("salary_min"),
        "salary_max": job.get("salary_max"),
        "category": job.get("category", {}).get("label"),
        "created": job.get("created"),
        "description": job.get("description")
    })

df = pd.DataFrame(rows)

# Removes reposted/duplicate listings
df = df.drop_duplicates(subset=["title", "company", "location"])

# Fills missing salary values with 0 instead of leaving nulls
df["salary_min"] = df["salary_min"].fillna(0)
df["salary_max"] = df["salary_max"].fillna(0)

# Converts date text into a real datetime type for later time-based analysis
df["created"] = pd.to_datetime(df["created"])

df.to_csv("cleaned_jobs.csv", index=False)
print(f"Success! Cleaned data saved to cleaned_jobs.csv with {len(df)} rows.")