from flask import Flask, render_template, request, Response
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import csv
import io

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    title = None
    headings = []
    paragraphs = []
    links = []
    images = []
    statistics = {}
    description = None
    author = None
    language = None
    canonical = None
    error = None

    if request.method == "POST":
        url = request.form["url"].strip()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Page title
            title = soup.title.string.strip() if soup.title else "No title found"

            # Headings
            for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                text = heading.get_text(strip=True)

                if text:
                    headings.append({
                        "tag": heading.name,
                        "text": text
                    })

            # Paragraphs
            for paragraph in soup.find_all("p"):
                text = paragraph.get_text(" ", strip=True)

                if text:
                    paragraphs.append(text)

            # Links
            for link in soup.find_all("a", href=True):
                text = link.get_text(" ", strip=True)
                href = link["href"]

                if href:
                    full_url = urljoin(url, href)

                    links.append({
                        "text": text or "No text",
                        "url": full_url
                    })

            # Images
            for image in soup.find_all("img"):

                image_url = None

                # Normal src
                if image.get("src"):
                    image_url = image["src"]

                # Lazy-loaded image
                elif image.get("data-src"):
                    image_url = image["data-src"]

                # srcset
                elif image.get("srcset"):
                    image_url = image["srcset"].split(",")[-1].strip().split(" ")[0]

                if image_url:
                    full_url = urljoin(url, image_url)

                    images.append({
                        "url": full_url,
                        "alt": image.get("alt", "No alt text")
                    })

            statistics = {
                "links": len(links),
                "images": len(images),
                "headings": len(headings),
                "paragraphs": len(paragraphs)
            }

            # Meta information

            # Description
            description_tag = soup.find("meta", attrs={"name": "description"})
            if description_tag:
                description = description_tag.get("content")

            # Author
            author_tag = soup.find("meta", attrs={"name": "author"})
            if author_tag:
                author = author_tag.get("content")

            # Language
            language = soup.html.get("lang") if soup.html else None

            # Canonical URL
            canonical_tag = soup.find("link", rel="canonical")
            if canonical_tag:
                canonical = urljoin(url, canonical_tag.get("href", ""))

        except requests.RequestException as e:
            error = f"Could not access website: {e}"

    return render_template(
        "index.html",
        title=title,
        headings=headings,
        paragraphs=paragraphs,
        links=links,
        images=images,
        statistics=statistics,
        description=description,
        author=author,
        language=language,
        canonical=canonical,
        error=error
    )

@app.route("/export/json", methods=["POST"])
def export_json():

    data = request.get_json()

    return Response(
        json.dumps(data, indent=4),
        mimetype="application/json",
        headers={
            "Content-Disposition": "attachment; filename=scraped_data.json"
        }
    )

@app.route("/export/csv", methods=["POST"])
def export_csv():

    data = request.get_json()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(["Type", "Text", "URL"])

    for link in data.get("links", []):
        writer.writerow([
            "Link",
            link.get("text", ""),
            link.get("url", "")
        ])

    for image in data.get("images", []):
        writer.writerow([
            "Image",
            image.get("alt", ""),
            image.get("url", "")
        ])

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=scraped_data.csv"
    )

    return response

if __name__ == "__main__":
    app.run()