from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import parse_github_url
from app.github_service import get_repo_metadata, get_all_commits

app = FastAPI()

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/extract")
def extract_data(request: RepoRequest):
    owner, repo = parse_github_url(request.repo_url)

    metadata = get_repo_metadata(owner, repo)
    commits = get_all_commits(owner, repo)

    return {
        "metadata": metadata,
        "total_commits": len(commits)
    }