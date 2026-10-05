import requests
import json
import time

url = input("Enter API URL: ")

try:
    start_time = time.time()

    response = requests.get(url, timeout=10)

    end_time = time.time()

    response_time = end_time - start_time

    print("\nStatus Code:", response.status_code)
    print("Response Time:", round(response_time, 3), "seconds")

    response.raise_for_status()

    data = response.json()

    print("\nResponse:")
    print(json.dumps(data, indent=4))

except requests.exceptions.RequestException as e:
    print("\nRequest failed:", e)

except ValueError:
    print("\nThe API did not return valid JSON.")