import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter website URL: ")

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

except requests.RequestException as e:
    print("Could not access website:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

print("Total links:", len(links))

for link in links:
    href = link.get("href")

    if not href:
        continue

    if href.startswith(("mailto:", "javascript:", "#")):
        continue

    full_url = urljoin(url, href)

    try:
        link_response = requests.get(full_url, timeout=5)
        print(full_url, "→", link_response.status_code)

    except requests.RequestException:
        print(full_url, "→ Request failed")