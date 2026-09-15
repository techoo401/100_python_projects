import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/everything"

categories = {
    "1": "India",
    "2": "technology",
    "3": "business",
    "4": "sports",
    "5": "entertainment",
    "6": "science",
    "7": "health"
}

print("=" * 40)
print("           📰 NEWS CLI")
print("=" * 40)

print("\n1. India")
print("2. Technology")
print("3. Business")
print("4. Sports")
print("5. Entertainment")
print("6. Science")
print("7. Health")
print("8. Exit")

choice = input("\nChoose a category: ")

if choice == "8":
    print("Goodbye! 👋")
    exit()

if choice not in categories:
    print("Invalid choice!")
    exit()

query = categories[choice]

params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": api_key
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("Something went wrong!")
    print(response.json())
    exit()

data = response.json()

if data["totalResults"] == 0:
    print("\nNo news found.")
    exit()

print(f"\n📰 Latest {query.title()} News")
print("=" * 40)

for i, article in enumerate(data["articles"], start=1):

    title = article["title"]
    source = article["source"]["name"]
    published = article["publishedAt"]
    article_url = article["url"]

    print(f"\n{i}. {title}")
    print(f"   Source: {source}")
    print(f"   Published: {published}")
    print(f"   URL: {article_url}")

print("\n" + "=" * 40)