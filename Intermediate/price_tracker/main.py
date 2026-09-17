import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urlunsplit

product_name = input("Enter product name: ")
url = input("Enter URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

parts = urlsplit(url)

domain = parts.netloc.lower()

url = urlunsplit((
    parts.scheme,
    parts.netloc,
    parts.path,
    "",
    ""
))

if domain in ("amazon.in", "www.amazon.in"):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/152.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find("span", class_="a-price-whole")

    if price:

        price = int(price.text.strip().rstrip(".").replace(",", ""))

        connection = sqlite3.connect("price_tracker.db")
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            current_price INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            price INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
        """)

        cursor.execute("""
        INSERT INTO products (name, url, current_price)
        VALUES (?, ?, ?)
        """, (product_name, url, price))

        connection.commit()
        connection.close()

        print(f"Product: {product_name}")
        print(f"Price: ₹{price}")
        print("Product added successfully.")

    else:
        print("Could not find price.")

else:
    print("Website not supported.")