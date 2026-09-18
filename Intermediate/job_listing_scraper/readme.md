# Job Listing Scraper

A Python-based job listing scraper built with **Playwright** that collects job information from Indeed search results.

The scraper takes a **job category** and **location** from the user, opens Indeed in a real browser, extracts job details, opens each listing to collect its full description, and saves everything into a text file.

## Features

* 🔎 Search by job category
* 📍 Search by location
* 🏢 Extract company name
* 💼 Extract job title
* 📍 Extract job location
* 💰 Extract salary when available
* 📄 Extract full job description
* 💾 Save results to `jobs.txt`
* 🌐 Uses Playwright with Chromium
* 🍪 Handles the cookie rejection prompt

## Technologies

* Python
* Playwright
* Chromium
* Indeed

## Project Structure

```text
job_listing_scraper/
│
├── main.py
├── jobs.txt
├── requirements.txt
└── venv/
```

## Installation

Clone the repository and open the project folder.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright's Chromium browser:

```bash
python -m playwright install chromium
```

## Run

```bash
python main.py
```

Enter the requested information:

```text
Enter job category: Python Developer
Enter location: Delhi
```

The scraper will open the browser and collect the available job listings.

The results are saved in:

```text
jobs.txt
```

## Output

Each job is stored with information such as:

```text
============================================================
JOB: Junior Python Developer
COMPANY: Example Company
LOCATION: Delhi
SALARY: ₹25,000 - ₹50,000 a month

DESCRIPTION:
Full job description...
```

## Notes

* The scraper requires an internet connection.
* Indeed may display verification or CAPTCHA challenges. These should be completed manually rather than bypassed.
* Website structure can change, which may require updating the selectors used by the scraper.

## License

This project is licensed under the MIT License.
    