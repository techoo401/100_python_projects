import requests

username = input("Enter GitHub username: ").strip()

profile_url = f"https://api.github.com/users/{username}"
repos_url = f"https://api.github.com/users/{username}/repos"

profile_response = requests.get(profile_url)

if profile_response.status_code == 200:
    profile = profile_response.json()
    
    print("\n" + "=" * 50)
    print("                 GITHUB PROFILE")
    print("=" * 50)

    print(f"{'Username':<20}: {profile['login']}")
    print(f"{'Name':<20}: {profile['name'] or 'N/A'}")
    print(f"{'Bio':<20}: {profile['bio'] or 'N/A'}")
    print(f"{'Location':<20}: {profile['location'] or 'N/A'}")
    print(f"{'Company':<20}: {profile['company'] or 'N/A'}")
    print(f"{'Twitter':<20}: {profile['twitter_username'] or 'N/A'}")
    print(f"{'Followers':<20}: {profile['followers']}")
    print(f"{'Following':<20}: {profile['following']}")
    print(f"{'Public Repositories':<20}: {profile['public_repos']}")
    print(f"{'Account Created':<20}: {profile['created_at'][:10]}")
    print(f"{'Profile URL':<20}: {profile['html_url']}")

    repos_response = requests.get(repos_url)

    if repos_response.status_code == 200:
        repositories = repos_response.json()

        print("\n" + "=" * 50)
        print("                 REPOSITORIES")
        print("=" * 50)

        for repo in repositories:
            print(
                f"{repo['name']:<30}"
                f"⭐ {repo['stargazers_count']:<6}"
                f"🍴 {repo['forks_count']}"
            )

        total_stars = sum(repo["stargazers_count"] for repo in repositories)
        total_forks = sum(repo["forks_count"] for repo in repositories)

        most_starred = max(
            repositories,
            key=lambda repo: repo["stargazers_count"],
            default=None
        )

        languages = [
            repo["language"]
            for repo in repositories
            if repo["language"]
        ]

        if languages:
            from collections import Counter

            language_counts = Counter(languages)
            most_used_language = language_counts.most_common(1)[0][0]
        else:
            most_used_language = "N/A"

        print("\n" + "=" * 50)
        print("                 ANALYSIS")
        print("=" * 50)

        print(f"{'Total Stars':<20}: ⭐ {total_stars}")
        print(f"{'Total Forks':<20}: 🍴 {total_forks}")
        print(f"{'Most Used Language':<20}: {most_used_language}")

        if most_starred:
            print(
                f"{'Most Starred Repo':<20}: "
                f"{most_starred['name']} "
                f"(⭐ {most_starred['stargazers_count']})"
            )

        print("=" * 50)

    else:
        print("Could not fetch repositories.")

else:
    print("GitHub user not found.")