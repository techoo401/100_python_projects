import requests
from urllib.parse import urlparse


def get_repo_info(repo_url):
    parsed_url = urlparse(repo_url)

    parts = parsed_url.path.strip("/").split("/")

    if len(parts) < 2:
        print("Invalid GitHub repository URL.")
        return

    owner = parts[0]
    repo = parts[1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url)

    if response.status_code == 404:
        print("Repository not found.")
        return

    if response.status_code != 200:
        print(f"GitHub API error: {response.status_code}")
        return

    data = response.json()

    print("\n" + "=" * 45)
    print("       GITHUB REPOSITORY ANALYZER")
    print("=" * 45)

    print(f"\nRepository : {data['name']}")
    print(f"Owner      : {data['owner']['login']}")
    print(f"Description: {data['description']}")
    print(f"Stars      : {data['stargazers_count']}")
    print(f"Forks      : {data['forks_count']}")
    print(f"Watchers   : {data['watchers_count']}")
    print(f"Open Issues: {data['open_issues_count']}")
    print(f"Language   : {data['language']}")
    print(
        f"License    : "
        f"{data['license']['name'] if data['license'] else 'None'}"
    )
    print(f"Created    : {data['created_at']}")
    print(f"Updated    : {data['updated_at']}")

    get_languages(owner, repo)

    contributors = get_contributors(owner, repo)

    commits = get_recent_commits(owner, repo)

    issues, pull_requests = get_issues_and_prs(owner, repo)

    analyze_repository(
        data,
        contributors,
        issues,
        pull_requests
    )

def get_languages(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"

    response = requests.get(url)

    if response.status_code != 200:
        print("\nUnable to fetch language statistics.")
        return

    languages = response.json()

    if not languages:
        print("\nNo language data available.")
        return

    total_bytes = sum(languages.values())

    print("\n" + "=" * 65)
    print("           LANGUAGE STATISTICS")
    print("=" * 65)

    for language, bytes_count in languages.items():
        percentage = (bytes_count / total_bytes) * 100

        bar_length = int(percentage / 2)

        bar = "█" * bar_length

        print(f"{language:<15} {bar:<40} {percentage:.1f}%")

def get_contributors(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

    response = requests.get(url)

    if response.status_code != 200:
        print("\nUnable to fetch contributors.")
        return

    contributors = response.json()

    if not contributors:
        print("\nNo contributor data available.")
        return

    print("\n" + "=" * 45)
    print("             TOP CONTRIBUTORS")
    print("=" * 45)

    for index, contributor in enumerate(contributors[:10], start=1):
        username = contributor["login"]
        contributions = contributor["contributions"]

        print(f"{index}. {username:<25} {contributions} commits")

    return contributors

def get_recent_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    if response.status_code != 200:
        print("\nUnable to fetch commits.")
        return

    commits = response.json()

    if not commits:
        print("\nNo commit data available.")
        return

    print("\n" + "=" * 45)
    print("              RECENT COMMITS")
    print("=" * 45)

    for index, commit in enumerate(commits[:10], start=1):
        message = commit["commit"]["message"].split("\n")[0]
        author = commit["commit"]["author"]["name"]
        date = commit["commit"]["author"]["date"][:10]

        print(f"\n{index}. {message}")
        print(f"   Author : {author}")
        print(f"   Date   : {date}")

    return commits

def get_issues_and_prs(owner, repo):
    issues_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    prs_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    issues_response = requests.get(issues_url)
    prs_response = requests.get(prs_url)

    print("\n" + "=" * 45)
    print("          ISSUES & PULL REQUESTS")
    print("=" * 45)

    if issues_response.status_code == 200:
        issues = issues_response.json()

        actual_issues = [
            issue for issue in issues
            if "pull_request" not in issue
        ]

        print(f"\nOpen Issues Found : {len(actual_issues)}")

        for issue in actual_issues[:5]:
            print(f"- #{issue['number']} {issue['title']}")

    else:
        print("\nUnable to fetch issues.")

    if prs_response.status_code == 200:
        pull_requests = prs_response.json()

        print(f"\nOpen Pull Requests: {len(pull_requests)}")

        for pr in pull_requests[:5]:
            print(f"- #{pr['number']} {pr['title']}")

    else:
        print("\nUnable to fetch pull requests.")

    return actual_issues, pull_requests

def analyze_repository(data, contributors, issues, pull_requests):
    print("\n" + "=" * 45)
    print("          REPOSITORY HEALTH ANALYSIS")
    print("=" * 45)

    stars = data["stargazers_count"]
    forks = data["forks_count"]
    open_issues = data["open_issues_count"]

    contributor_count = len(contributors)

    print("\nRepository Metrics")
    print("-" * 45)

    print(f"Stars              : {stars}")
    print(f"Forks              : {forks}")
    print(f"Open Issues        : {open_issues}")
    print(f"Contributors       : {contributor_count}")
    print(f"Recent PRs         : {len(pull_requests)}")

    print("\nActivity Indicators")
    print("-" * 45)

    if contributor_count >= 10:
        print("✓ Multiple contributors detected")
    elif contributor_count > 1:
        print("✓ More than one contributor")
    else:
        print("• Small contributor base")

    if forks > 0:
        print("✓ Repository has been forked")
    else:
        print("• No forks detected")

    if pull_requests:
        print("✓ Open pull requests detected")
    else:
        print("• No open pull requests in the fetched data")

    if open_issues > 0:
        print("• Open issues are currently present")
    else:
        print("✓ No open issues")

    print("\nNote:")
    print("These indicators describe repository activity.")
    print("They are not a universal measure of repository quality.")

repo_url = input("Enter GitHub repository URL: ")

get_repo_info(repo_url)