# 🔗 Website Link Checker

A simple Python-based **Website Link Checker** that scans a webpage, extracts its links, and checks the HTTP status code of each link.

Built as part of my Python project series to practice **web scraping, HTTP requests, HTML parsing, and error handling**.

---

## ✨ Features

* 🌐 Accepts any website URL
* 🔍 Extracts links from the webpage
* 🔄 Converts relative URLs into absolute URLs
* 🚫 Skips non-web links such as `mailto:`, `javascript:`, and anchors
* 📡 Sends a request to each extracted link
* 📊 Displays the HTTP status code
* 🛡️ Handles failed requests without crashing
* ⏱️ Uses request timeouts to prevent the program from hanging

---

## 🛠️ Technologies Used

* **Python**
* **Requests** — for sending HTTP requests
* **BeautifulSoup4** — for parsing HTML
* **urllib.parse** — for handling and joining URLs

---

## 📂 Project Structure

```text
website_link_checker/
│
├── main.py
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd website_link_checker
```

Install the required libraries:

```bash
py -m pip install requests beautifulsoup4
```

---

## ▶️ Usage

Run the program:

```bash
py main.py
```

Enter a website URL when prompted:

```text
Enter website URL: https://www.youtube.com/
```

The program will scan the page and check the extracted links.

### Example

```text
Enter website URL: https://www.youtube.com/

Total links: 14

https://www.youtube.com/ → 200
https://www.youtube.com/about/ → 200
https://www.youtube.com/creators/ → 200
https://www.youtube.com/t/privacy → 200
https://www.youtube.com/new → 200
```

---

## 🧠 How It Works

The project follows a simple pipeline:

```text
          Website URL
               │
               ▼
        Send HTTP Request
               │
               ▼
           Get HTML
               │
               ▼
        BeautifulSoup
               │
               ▼
       Find <a> Elements
               │
               ▼
        Extract href URLs
               │
               ▼
    Convert Relative URLs
        to Absolute URLs
               │
               ▼
       Send Request to
        Each Link
               │
               ▼
        Print Status Code
```

---

## 📚 What I Learned

While building this project, I practiced:

* Making HTTP requests with `requests`
* Understanding HTTP status codes
* Parsing HTML with BeautifulSoup
* Finding HTML elements with `find_all()`
* Extracting attributes using `.get()`
* Working with relative and absolute URLs
* Using `urljoin()`
* Handling network errors with `try/except`
* Using request timeouts
* Understanding real-world limitations of automated web requests

---

## ⚠️ Important Note

A status code does not always tell us whether a link would work perfectly for a human visitor.

For example, some websites may block automated requests and return non-standard responses.

One example encountered during testing was:

```text
LinkedIn → 999
```

`999` is not a standard HTTP status code and can be used by LinkedIn to reject automated requests. Therefore, such a response should not automatically be interpreted as a broken link.

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
requests
beautifulsoup4
```

Install them with:

```bash
py -m pip install -r requirements.txt
```

---

## 🎯 Project Goal

The goal of this project was not to build a production-grade web crawler, but to understand the fundamentals behind how a link checker works.

It combines **web scraping + HTTP requests + URL handling + error handling** into one practical Python project.

---

## 👨‍💻 Author

**Himanshu**

Built with Python 🐍

Part of my journey of building practical Python projects and improving my development skills.

---

⭐ If you found this project useful, feel free to star the repository!
