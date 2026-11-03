#!/usr/bin/env python3
"""Generate self-hosted GitHub profile SVG cards using the GitHub API."""
import json
import os
import urllib.request
import urllib.error
import html
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = "KamalEsakki"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path("dist")
OUT.mkdir(exist_ok=True)

BG = "#020617"
PANEL = "#0b1220"
GREEN = "#34d399"
MUTED = "#94a3b8"
TEXT = "#e2e8f0"
GRID = "#1e293b"


def api(url, method="GET", payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    if data:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def svg_start(width, height, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">
<rect width="100%" height="100%" rx="14" fill="{BG}" stroke="#14532d"/>
<text x="26" y="38" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="19" font-weight="700">{html.escape(title)}</text>'''


def save(name, content):
    (OUT / name).write_text(content + "\n</svg>", encoding="utf-8")


profile = api(f"https://api.github.com/users/{USER}")
repos = api(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")
public_repos = profile.get("public_repos", len(repos))
followers = profile.get("followers", 0)
stars = sum(repo.get("stargazers_count", 0) for repo in repos)
forks = sum(repo.get("forks_count", 0) for repo in repos)

# Contribution calendar is obtained from GraphQL. The other cards still build
# if GitHub does not expose this field to the workflow token.
today = datetime.now(timezone.utc).date()
start = today - timedelta(days=364)
query = """query($login:String!, $from:DateTime!, $to:DateTime!) {
  user(login:$login) {
    contributionsCollection(from:$from, to:$to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""
calendar = None
try:
    result = api("https://api.github.com/graphql", "POST", {
        "query": query,
        "variables": {
            "login": USER,
            "from": start.isoformat() + "T00:00:00Z",
            "to": today.isoformat() + "T23:59:59Z"
        }
    })
    calendar = result.get("data", {}).get("user", {}).get("contributionsCollection", {}).get("contributionCalendar")
except Exception as exc:
    print(f"Contribution calendar unavailable; generating other cards: {exc}")

contributions = calendar.get("totalContributions", 0) if calendar else 0
stats = svg_start(760, 190, "GitHub Overview")
stats += f'<text x="26" y="70" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">PUBLIC REPOSITORIES</text>'
stats += f'<text x="26" y="112" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="31" font-weight="700">{public_repos}</text>'
stats += f'<text x="215" y="70" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">TOTAL STARS</text>'
stats += f'<text x="215" y="112" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="31" font-weight="700">{stars}</text>'
stats += f'<text x="405" y="70" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">FOLLOWERS</text>'
stats += f'<text x="405" y="112" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="31" font-weight="700">{followers}</text>'
stats += f'<text x="585" y="70" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">CONTRIBUTIONS / YEAR</text>'
stats += f'<text x="585" y="112" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="31" font-weight="700">{contributions}</text>'
stats += f'<text x="26" y="162" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="11">Updated automatically by GitHub Actions</text>'
save("github-stats.svg", stats)

language_totals = {}
for repo in repos:
    if repo.get("fork"):
        continue
    try:
        languages = api(repo["languages_url"])
        for language, amount in languages.items():
            language_totals[language] = language_totals.get(language, 0) + amount
    except Exception as exc:
        print(f"Skipping languages for {repo.get('name')}: {exc}")

top = sorted(language_totals.items(), key=lambda item: item[1], reverse=True)[:8]
total_bytes = sum(language_totals.values()) or 1
lang_svg = svg_start(760, 300, "Most Used Languages")
y = 75
for language, amount in top:
    pct = amount / total_bytes * 100
    label = html.escape(language)
    lang_svg += f'<text x="26" y="{y}" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="13">{label}</text>'
    lang_svg += f'<text x="710" y="{y}" text-anchor="end" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">{pct:.1f}%</text>'
    lang_svg += f'<rect x="26" y="{y+12}" width="684" height="9" rx="4.5" fill="{GRID}"/>'
    lang_svg += f'<rect x="26" y="{y+12}" width="{684*pct/100:.2f}" height="9" rx="4.5" fill="{GREEN}"/>'
    y += 27
if not top:
    lang_svg += f'<text x="26" y="85" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="13">No language data available yet</text>'
save("top-languages.svg", lang_svg)

if calendar:
    days = [day for week in calendar.get("weeks", []) for day in week.get("contributionDays", [])]
    heat = svg_start(900, 190, "Contribution Activity — Last 12 Months")
    heat += f'<text x="26" y="60" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="11">{contributions} contributions in the last year</text>'
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    x0, y0, cell, gap = 28, 82, 10, 4
    for index, day in enumerate(days):
        col, row = divmod(index, 7)
        count = day.get("contributionCount", 0)
        level = 0 if count == 0 else 1 if count < 3 else 2 if count < 6 else 3 if count < 10 else 4
        x, y = x0 + col * (cell + gap), y0 + row * (cell + gap)
        date_label = html.escape(day.get("date", ""))
        heat += f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{colors[level]}"><title>{date_label}: {count} contributions</title></rect>'
    heat += f'<text x="28" y="174" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">Less</text>'
    for i, color in enumerate(colors):
        heat += f'<rect x="{72+i*17}" y="165" width="11" height="11" rx="2" fill="{color}"/>'
    heat += f'<text x="166" y="174" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">More</text>'
    save("github-activity.svg", heat)
else:
    heat = svg_start(760, 100, "Contribution Activity")
    heat += f'<text x="26" y="72" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="13">Contribution calendar data is temporarily unavailable.</text>'
    save("github-activity.svg", heat)

print("Generated profile SVG cards:", ", ".join(p.name for p in OUT.glob("*.svg")))
