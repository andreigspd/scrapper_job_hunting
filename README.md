# scrapper_job_hunting

A small Python script that scrapes IT job postings from LinkedIn's public guest
endpoint and exports them to a CSV file.

For each job it collects the job ID, title, company, location, post date, and link.
This was an early experiment that later evolved into the
[Jobby Discord bot](https://github.com/andreigspd/jobby_discord_bot).

## Requirements

Python 3 with `requests` and `beautifulsoup4`:

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python scraper.py
```

The results are written to `scraped_quotes.csv`.
