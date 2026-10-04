import requests
import time

url = input("Enter website URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    start_time = time.time()

    response = requests.get(url, timeout=10)

    end_time = time.time()

    response_time = end_time - start_time

    print("\nWebsite:", url)
    print("HTTP Status:", response.status_code)
    print(f"Response Time: {response_time:.2f} seconds")

    if 200 <= response.status_code < 400:
        print("Status: UP")
    elif 400 <= response.status_code < 500:
        print("Status: UP (Client Error)")
    else:
        print("Status: DOWN (Server Error)")

except requests.exceptions.Timeout:
    print("\nStatus: DOWN")
    print("Reason: Request timed out")

except requests.exceptions.ConnectionError:
    print("\nStatus: DOWN")
    print("Reason: Could not connect to website")

except requests.exceptions.RequestException as error:
    print("\nStatus: DOWN")
    print("Reason:", error)