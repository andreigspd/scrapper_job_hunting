from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

quotes_love = soup.find_all()

file = open("scraped_quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["QUOTE", "AUTHOR"])

for quote, author in zip(quotes, authors):
    writer.writerow([quote.text, author.text])

file.close()