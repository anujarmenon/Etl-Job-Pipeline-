import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")

# Which locations have the most job postings?
top_locations = pd.read_sql("""
    SELECT location, COUNT(*) AS job_count
    FROM jobs
    GROUP BY location
    ORDER BY job_count DESC
    LIMIT 10
""", conn)
print("Top 10 locations by job count:")
print(top_locations)

# Average salary by category
avg_salary = pd.read_sql("""
    SELECT category, ROUND(AVG(salary_max), 0) AS avg_max_salary
    FROM jobs
    WHERE salary_max > 0
    GROUP BY category
    ORDER BY avg_max_salary DESC
""", conn)
print("\nAverage max salary by category:")
print(avg_salary)

# How many postings have no listed salary?
missing_salary = pd.read_sql("""
    SELECT COUNT(*) AS jobs_without_salary
    FROM jobs
    WHERE salary_max = 0
""", conn)
print("\nJobs without a listed salary:")
print(missing_salary)

conn.close()