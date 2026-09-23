    # GitHub Repository Analyzer

A Python-based CLI tool that analyzes public GitHub repositories using the GitHub REST API.

The project accepts a GitHub repository URL and retrieves useful information such as repository statistics, programming languages, contributors, recent commits, issues, and pull requests.

## Features

* 🔍 Analyze any public GitHub repository
* ⭐ Display stars, forks, watchers, and open issues
* 💻 Show the repository's primary programming language
* 📊 Calculate language percentages
* 👥 Display top contributors
* 📝 Display recent commits
* 🐛 Display open issues
* 🔀 Display open pull requests
* 📈 Generate basic repository activity indicators
* ⚠️ Handle invalid repositories and API request errors

## Technologies Used

* Python
* Requests
* GitHub REST API
* JSON
* URL Parsing

## Project Structure

```text
github_repository_analyzer/
│
├── app.py
├── github_api.py
├── analyzer.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-repository-analyzer.git
```

### 2. Navigate to the project

```bash
cd github-repository-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python app.py
```

Enter a public GitHub repository URL when prompted:

```text
Enter GitHub repository URL: https://github.com/python/cpython
```

The analyzer will then retrieve and display the repository information.

## Example

```text
=============================================
       GITHUB REPOSITORY ANALYZER
=============================================

Repository : cpython
Owner      : python
Stars      : ...
Forks      : ...
Language   : Python

=============================================
           LANGUAGE STATISTICS
=============================================

Python          90.0%
C                8.0%
HTML             2.0%

=============================================
              ANALYSIS
=============================================

Contributors : ...
Open Issues  : ...
Open PRs     : ...
Recent Commits Fetched : 10
```

The exact values depend on the repository and its current GitHub activity.

## How It Works

The application extracts the repository owner and name from the GitHub URL.

It then uses GitHub's REST API to retrieve:

1. Repository information
2. Programming language statistics
3. Contributors
4. Recent commits
5. Issues
6. Pull requests

The collected data is processed and displayed through the command line.

## Error Handling

The application handles common situations such as:

* Invalid GitHub URLs
* Repositories that cannot be found
* Failed API requests
* Missing language data
* Empty contributor or commit data

## API

This project uses the public GitHub REST API.

No GitHub token is required for the basic version of this project.

## Future Improvements

Possible improvements include:

* GitHub API authentication
* API pagination
* Commit frequency analysis
* Contributor activity analysis
* Repository health metrics
* Data visualization
* Flask web dashboard
* Historical repository statistics
* Export analysis to JSON or CSV

## Learning Goals

This project was built to practice:

* Working with REST APIs
* Sending HTTP requests with Python
* Processing JSON responses
* Parsing URLs
* Working with nested API data
* Data analysis
* Error handling
* Organizing Python projects into modules

## License

This project is open source and available for learning and personal use.
