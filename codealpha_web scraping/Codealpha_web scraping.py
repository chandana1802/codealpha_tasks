# ---------------------------------------
# Job Listing Web Scraping Program
# ---------------------------------------

import requests
from bs4 import BeautifulSoup

# Website URL (job listings)
URL = "https://realpython.github.io/fake-jobs/"

try:
    # Send request
    response = requests.get(URL)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all job cards
    job_cards = soup.find_all("div", class_="card-content")

    print("\nLIST OF JOBS:\n")

    # Open file to save data
    with open("job_listings.txt", "w", encoding="utf-8") as file:
        file.write("JOB LISTINGS\n")
        file.write("=" * 40 + "\n\n")

        for job in job_cards:
            job_title = job.find("h2", class_="title").text.strip()
            company = job.find("h3", class_="company").text.strip()
            location = job.find("p", class_="location").text.strip()

            # Print output
            print("Job Title :", job_title)
            print("Company   :", company)
            print("Location  :", location)
            print("-" * 40)

            # Save to file
            file.write(f"Job Title : {job_title}\n")
            file.write(f"Company   : {company}\n")
            file.write(f"Location  : {location}\n")
            file.write("-" * 40 + "\n")

    print("\nJob data successfully scraped and saved to 'job_listings.txt'")

except Exception as e:
    print("Error occurred:", e)
