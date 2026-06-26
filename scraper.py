from bs4 import BeautifulSoup
import requests
import csv

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Connection": "keep-alive"
}


def scrape_linkedin_jobs(keywords, location, start=0):
    file = open("scraped_quotes.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["JOB_ID", "TITLE", "COMPANY", "LOCATION", "POST DATE", "LINK"])
    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
    params = {
        "keywords": keywords,
        "location": location,
        "start": start
    }
    try:
        page_to_scrape = requests.get(url, params=params, headers=HEADERS, timeout=15)
        if page_to_scrape.status_code != 200:
            print(f"Error scraping LinkedIn: Status code {page_to_scrape.status_code}")
            file.close()
            return
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        cards = soup.find_all("li")
        for card in cards:
            # Job Title
            title = card.find("h3", class_="base-search-card__title").text.strip() if card.find("h3", class_="base-search-card__title") else "N/A"
            
            # Company name
            company = card.find("h4", class_="base-search-card__subtitle").text.strip() if card.find("h4", class_="base-search-card__subtitle") else "N/A"
            
            # Location
            location = card.find("span", class_="job-search-card__location").text.strip() if card.find("span", class_="job-search-card__location") else "N/A"
            # Link
            link = card.find("a", class_="base-card__full-link")["href"] if card.find("a", class_="base-card__full-link") else None
            if not link:
                link = card.find("a")["href"] if card.find("a") and "href" in card.find("a").attrs else None
            # Clean link    
            link = link.split("?")[0] if link else None

            # Post date
            post_date = card.find("time")["datetime"] if card.find("time") and "datetime" in card.find("time").attrs else "N/A"
           
            # Job ID
            job_id = link.rstrip("/").split("/")[-1].split("-")[-1] if link else None

            writer.writerow([job_id, title, company, location, post_date, link])
    except Exception as e:
        print(f"An error occurred: {e}")
        file.close()

    file.close()

