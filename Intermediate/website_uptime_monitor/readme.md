# Website Uptime Monitor

A simple Python CLI tool that checks whether a website is reachable and reports its HTTP status and response time.

## Features

* Accepts a website URL from the user
* Automatically adds `https://` when needed
* Checks website availability
* Displays HTTP status code
* Measures response time
* Handles timeouts and connection errors

## Requirements

* Python 3.x
* `requests`

Install the dependency:

```bash
py -m pip install requests
```

## Usage

Run the program:

```bash
python uptime_monitor.py
```

Enter a website URL when prompted:

```text
Enter website URL: google.com

Website: https://google.com
HTTP Status: 200
Response Time: 0.32 seconds
Status: UP
```

## Project Structure

```text
website_uptime_monitor/
│
├── uptime_monitor.py
└── README.md
```
