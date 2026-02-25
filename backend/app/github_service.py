import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# -------------------------------
# Function 1: Get Repo Metadata
# -------------------------------
def get_repo_metadata(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch repo metadata")

    data = response.json()

    return {
        "created_at": data["created_at"],
        "pushed_at": data["pushed_at"],
        "fork": data["fork"],
        "stargazers_count": data["stargazers_count"],
        "forks_count": data["forks_count"]
    }

# --------------------------------
# Function 2: Get All Commits
# --------------------------------
def get_all_commits(owner: str, repo: str):
    commits = []
    page = 1

    while True:
        url = f"{BASE_URL}/repos/{owner}/{repo}/commits?page={page}&per_page=100"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch commits")

        data = response.json()

        if not data:
            break

        commits.extend(data)
        page += 1

    return commits

# --------------------------------
# Function 3: Get Commit Details
# --------------------------------
def get_commit_details(owner: str, repo: str, sha: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits/{sha}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "additions": data["stats"]["additions"],
        "deletions": data["stats"]["deletions"],
        "total": data["stats"]["total"]
    }