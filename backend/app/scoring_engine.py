def calculate_authenticity_score(analysis):
    score = 100
    flags = []

    # 🔹 Burst detection
    if analysis["burst_ratio"] > 0.5:
        score -= 25
        flags.append("High commit burst detected")

    # 🔹 Low duration
    if analysis["project_duration_days"] < 3:
        score -= 15
        flags.append("Very short project duration")

    # 🔹 Generic commits
    if analysis["generic_commit_ratio"] > 0.6:
        score -= 20
        flags.append("Too many generic commit messages")

    # 🔹 Very low commit count
    if analysis["total_commits"] < 5:
        score -= 10
        flags.append("Very few commits")

    # 🔹 Single contributor (optional)
    if analysis["unique_contributors"] == 1:
        flags.append("Single contributor project")

    # Normalize score
    score = max(score, 0)

    # Risk classification
    if score >= 80:
        risk = "Low"
    elif score >= 50:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "authenticity_score": score,
        "risk_level": risk,
        "flags": flags
    }