from datetime import datetime
from collections import defaultdict

GENERIC_MESSAGES = ["update", "fix", "final", "changes", "done", "test"]

def analyze_commits(commits):
    if not commits:
        return {}

    total_commits = len(commits)

    # ----------------------------
    # Extract Dates
    # ----------------------------
    commit_dates = []
    daily_commit_count = defaultdict(int)
    contributors = set()
    generic_count = 0

    for commit in commits:
        date_str = commit["commit"]["author"]["date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        commit_dates.append(date_obj)

        day_key = date_obj.date()
        daily_commit_count[day_key] += 1

        # Contributors
        if commit["author"]:
            contributors.add(commit["author"]["login"])

        # Generic commit message detection
        message = commit["commit"]["message"].lower().strip()
        if message in GENERIC_MESSAGES:
            generic_count += 1

    # ----------------------------
    # Project Duration
    # ----------------------------
    first_commit = min(commit_dates)
    last_commit = max(commit_dates)
    duration_days = (last_commit - first_commit).days or 1

    avg_commits_per_day = total_commits / duration_days

    # ----------------------------
    # Burst Detection
    # ----------------------------
    max_single_day_commits = max(daily_commit_count.values())
    burst_ratio = max_single_day_commits / total_commits

    # ----------------------------
    # Generic Message Ratio
    # ----------------------------
    generic_commit_ratio = generic_count / total_commits

    return {
        "total_commits": total_commits,
        "project_duration_days": duration_days,
        "avg_commits_per_day": round(avg_commits_per_day, 2),
        "max_single_day_commits": max_single_day_commits,
        "burst_ratio": round(burst_ratio, 2),
        "generic_commit_ratio": round(generic_commit_ratio, 2),
        "unique_contributors": len(contributors)
    }