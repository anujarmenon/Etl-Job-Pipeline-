import requests
import json

# Replace these two lines with your actual App ID and App Key from Adzuna
APP_ID = "your_app_id_here"
APP_KEY = "your_app_key_here"

country = "gb"          # Ireland
job_title = "business analyst"

url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"

params = {
    "app_id": "4331912e",
    "app_key": "874027da4a7bf270306041f694279c74",
    "results_per_page": 50,
    "what": job_title,
    "content-type": "application/json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    with open("raw_jobs.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Success! Saved {len(data.get('results', []))} job listings to raw_jobs.json")
else:
    print(f"Error: {response.status_code}")
    print(response.text)