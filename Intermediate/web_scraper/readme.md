# 🕷️ Web Scraper

A Flask-based web scraper that extracts useful information from webpages and presents it through a clean web interface.

Enter a webpage URL and the scraper collects the page title, headings, paragraphs, links, images, metadata, and basic statistics. The scraped data can also be exported as **JSON** or **CSV** files.

---

🌐 Live Demo

🚀 Try the Web Scraper:
Web Scraper

Replace YOUR_RENDER_URL with your actual Render deployment URL.

---

## ✨ Features

* 🌐 Scrape webpages using a URL
* 🏷️ Extract page title
* 📑 Extract headings (`H1`–`H6`)
* 📝 Extract paragraphs
* 🔗 Extract links
* 🖼️ Extract images
* 🏷️ Extract image alt text
* 🔄 Convert relative URLs into absolute URLs
* 💤 Support lazy-loaded images using `data-src`
* 🖼️ Basic `srcset` image support
* 📋 Extract meta description
* ✍️ Extract author information
* 🌍 Detect webpage language
* 🔗 Extract canonical URL
* 📊 Display scraping statistics
* 📥 Export scraped data as JSON
* 📊 Export scraped data as CSV
* ⏱️ Request timeout handling
* 🚫 HTTP error handling
* 📱 Responsive web interface
* 🚀 Ready for deployment with Gunicorn

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Requests**
* **BeautifulSoup4**
* **HTML / CSS**
* **JavaScript**
* **Gunicorn**

---

## 📂 Project Structure

```text
web_scraper/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ How It Works

The application follows a simple scraping pipeline:

```text
User enters URL
       ↓
Flask receives URL
       ↓
Requests downloads webpage HTML
       ↓
BeautifulSoup parses HTML
       ↓
Information is extracted
       ↓
Results displayed in browser
       ↓
User can export data
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd web_scraper
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start the Flask application:

```bash
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Enter a webpage URL and click **Scrape Website**.

---

## 📥 Data Export

The scraper provides two export options:

### JSON

Exports the complete scraped dataset in JSON format.

```json
{
    "title": "Example Domain",
    "headings": [],
    "paragraphs": [],
    "links": [],
    "images": [],
    "statistics": {}
}
```

### CSV

Exports link and image information into a spreadsheet-friendly format.

---

## 🧠 What I Learned

This project helped me practice:

* Flask form handling
* HTTP requests with `requests`
* HTML parsing with BeautifulSoup
* CSS selectors and HTML tags
* Relative vs absolute URLs
* HTTP status/error handling
* User-Agent headers
* Jinja templates
* Passing Python data into JavaScript
* JavaScript `fetch()`
* JSON serialization
* File downloads from Flask
* CSV generation with Python
* Working with `Response`
* Basic web scraping architecture
* Deploying Flask applications with Gunicorn

---

## ⚠️ Limitations

This scraper works with HTML that is available in the initial server response.

Websites that heavily rely on **JavaScript to generate their content** may not return the same information that you see in a normal browser.

For example:

```text
Browser
   ↓
HTML + JavaScript
   ↓
Rendered page
```

while this project mainly works with:

```text
Server
   ↓
Initial HTML
   ↓
BeautifulSoup
```

Handling JavaScript-rendered websites would require a browser automation tool such as Selenium or Playwright.

---

## 🚀 Deployment

The application can be deployed using a production WSGI server such as **Gunicorn**.

Start command:

```bash
gunicorn app:app
```

Make sure `gunicorn` is included in `requirements.txt`.

---

## 📌 Project Status

**Completed ✅**

This project is part of my **100 Python Projects** journey and marks my move into more advanced Python/web-development projects.

---

## 👨‍💻 Author

**Himanshu**

Built with Python 🐍 and Flask ⚡
