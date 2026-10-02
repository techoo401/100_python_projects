from playwright.sync_api import sync_playwright, TimeoutError
from urllib.parse import urlparse
from pathlib import Path

url = input("Enter website URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

parsed_url = urlparse(url)

domain = parsed_url.netloc.replace("www.", "")
filename = domain.replace(".", "_") + ".png"

output_folder = Path("screenshots")
output_folder.mkdir(exist_ok=True)

output_path = output_folder / filename

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        page.screenshot(
            path=output_path,
            full_page=True
        )

        browser.close()

    print(f"✅ Screenshot saved: {output_path}")

except TimeoutError:
    print("❌ The website took too long to load.")

except Exception:
    print("❌ Could not capture the website.")
    print("Please check the URL and try again.")