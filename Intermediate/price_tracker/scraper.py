import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

connection = sqlite3.connect("price_tracker.db")
cursor = connection.cursor()

cursor.execute("""
SELECT id, name, url
FROM products
""")

products = cursor.fetchall()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/152.0.0.0 Safari/537.36"
}

for product_id, product_name, url in products:

    print(f"Checking: {product_name}")

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find("span", class_="a-price-whole")

    if price:

        price = int(price.text.strip().rstrip(".").replace(",", ""))

        date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
        INSERT INTO price_history (product_id, date, price)
        VALUES (?, ?, ?)
        """, (product_id, date, price))

        cursor.execute("""
        UPDATE products
        SET current_price = ?
        WHERE id = ?
        """, (price, product_id))

        print(f"Current price: ₹{price}")
        print(f"Saved: {date}")

    else:
        print("Could not find price.")

connection.commit()
connection.close()

print("Done.")