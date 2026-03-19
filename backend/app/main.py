from fastapi import FastAPI
from pydantic import BaseModel
from .utils import parse_github_url
from .github_service import get_repo_metadata, get_all_commits
from .commit_analyzer import analyze_commits
from .scoring_engine import calculate_authenticity_score
app = FastAPI()

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/extract")
def extract_data(request: RepoRequest):
    owner, repo = parse_github_url(request.repo_url)

    metadata = get_repo_metadata(owner, repo)
    commits = get_all_commits(owner, repo)

    analysis = analyze_commits(commits)
    score_data = calculate_authenticity_score(analysis)

    return {
        "metadata": metadata,
        "behavior_analysis": analysis,
        **score_data
    }