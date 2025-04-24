import os
from github import Github

def fetch_repo_metadata(repo_url: str):
    """Fetch repo metadata, README, license, and open issues."""
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    # Parse URL: https://github.com/kleervoyans/mash
    parts = repo_url.rstrip("/").split('/')
    owner, name = parts[-2], parts[-1]
    repo = g.get_repo(f"{owner}/{name}")

    # Metadata
    description = repo.description or ""
    clone_url = repo.clone_url
    license_info = repo.get_license().license.name if repo.get_license() else "No license"

    # README
    try:
        readme = repo.get_readme().decoded_content.decode()
    except Exception:
        readme = ""

    # Issues
    issues = repo.get_issues(state='open')
    known_issues = []
    for issue in issues[:5]:  # top 5
        known_issues.append(f"- [{issue.title}]({issue.html_url})")

    return {
        "name": name,
        "owner": owner,
        "description": description,
        "clone_url": clone_url,
        "license": license_info,
        "readme": readme,
        "known_issues": "\n".join(known_issues),
    }