import requests
from urllib.parse import quote

topic = input("Enter a topic: ")

topic = quote(topic)

url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

headers = {
    "User-Agent": "WikipediaCLI/1.0"
}

response = requests.get(url, headers=headers)

data = response.json()

print("\nTitle:", data["title"])
print("\nSummary:", data["extract"])
print("\nRead more:", data["content_urls"]["desktop"]["page"])