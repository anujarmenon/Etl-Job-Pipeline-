# End-to-End ETL Pipeline: UK Business Analyst Job Market

An end-to-end data pipeline that extracts live job posting data from the Adzuna API, cleans and transforms it with Python, loads it into a SQLite database, and visualizes insights in an interactive Power BI dashboard.

## Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) workflow from raw API data to a polished BI dashboard, built to explore trends in the UK Business Analyst job market.

## Tech Stack

- **Python** (Pandas, Requests) - data extraction and cleaning
- **SQL / SQLite** - data storage and querying
- **Power BI** - data modelling, DAX measures, and dashboard visualization
- **Git/GitHub** - version control

## Pipeline Steps

1. **Extract** (`extract.py`) - Pulls job listings from the Adzuna API (multiple pages), saves raw JSON.
2. **Clean** (`clean.py`) - Uses Pandas to flatten nested fields, remove duplicates, handle missing values, and fix date formatting.
3. **Load** (`load.py`) - Loads the cleaned data into a SQLite database (`jobs.db`).
4. **Query** (`query.py`) - Runs SQL queries directly against the database to answer questions like top locations and average salary by category.
5. **Visualize** - Power BI connects to `jobs.db` via ODBC and builds an interactive dashboard with custom DAX measures (average salary, salary range, highest salary) and a category slicer.

## Dashboard Preview

![Dashboard Screenshot](dashboard.png)

## Key Insights

- London dominates listings by volume, with the highest concentration of postings.
- IT and Accounting & Finance roles command the highest average salaries.
- Salary range across postings spans over £130K, reflecting the breadth of seniority levels in the data.

## Files

- `extract.py` - API extraction script
- `clean.py` - Data cleaning script
- `load.py` - SQLite loading script
- `query.py` - SQL analysis queries
- `jobs.db` - SQLite database
- `job_market_dashboard.pbix` - Power BI dashboard file
- `dashboard.png` - Dashboard screenshot

## Author

Anuja Raghu Menon
