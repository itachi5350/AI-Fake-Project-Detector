def parse_github_url(repo_url: str):
    parts = repo_url.strip().replace("https://github.com/", "").split("/")
    if len(parts) < 2:
        raise ValueError("Invalid GitHub URL")
    owner = parts[0]
    repo = parts[1]
    return owner, repo