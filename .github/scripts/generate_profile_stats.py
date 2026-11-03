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


# A unified dark dashboard matching the requested GitHub Metrics-style layout.
dashboard = svg_start(1100, 760, "KAMAL ESAKKI  /  DEVELOPER PROFILE")
dashboard += f'<text x="28" y="68" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="27" font-weight="700">Backend Developer</text>'
dashboard += f'<text x="28" y="94" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="14">Node.js  •  NestJS  •  APIs  •  CRM Integrations  •  MCP</text>'
dashboard += f'<text x="28" y="124" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">B.E. Computer Science and Engineering  |  2026</text>'
dashboard += f'<text x="28" y="158" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">PROFILE OVERVIEW</text>'
dashboard += f'<rect x="28" y="174" width="1044" height="104" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
overview = [("PUBLIC REPOSITORIES", str(public_repos)), ("TOTAL STARS", str(stars)), ("FOLLOWERS", str(followers)), ("FORKS", str(forks)), ("YEARLY CONTRIBUTIONS", str(contributions))]
for i, (label, value) in enumerate(overview):
    x = 52 + i * 207
    dashboard += f'<text x="{x}" y="213" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">{label}</text>'
    dashboard += f'<text x="{x}" y="252" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="27" font-weight="700">{value}</text>'

# Left: technical stack and current focus.
dashboard += f'<rect x="28" y="302" width="500" height="190" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
dashboard += f'<text x="50" y="334" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700">TECHNICAL TOOLKIT</text>'
skill_groups = [
    ("BACKEND", "Node.js  •  NestJS  •  Express  •  FastAPI  •  REST APIs"),
    ("LANGUAGES", "Python  •  TypeScript  •  JavaScript  •  SQL  •  Java"),
    ("DATABASES", "PostgreSQL  •  MySQL  •  MongoDB  •  TypeORM"),
    ("INTEGRATION", "OAuth 2.0  •  JWT  •  Zoho CRM  •  HubSpot  •  MCP"),
    ("TOOLS", "Docker  •  Git  •  Postman  •  n8n  •  Power BI")
]
for i, (label, value) in enumerate(skill_groups):
    y = 365 + i * 25
    dashboard += f'<text x="50" y="{y}" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="10" font-weight="700">{label}</text>'
    dashboard += f'<text x="150" y="{y}" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="11">{html.escape(value)}</text>'

# Right: career and project highlights.
dashboard += f'<rect x="548" y="302" width="524" height="190" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
dashboard += f'<text x="570" y="334" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700">CURRENT ROLE &amp; PROJECTS</text>'
dashboard += f'<text x="570" y="365" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">Backend Developer  /  Zeeyes AI Labs</text>'
dashboard += f'<text x="570" y="388" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="11">Backend services, API engineering, OAuth and CRM integrations</text>'
project_lines = [
    "Zoho CRM → HubSpot Migration + MCP Integration",
    "Stock Sentinel  /  FastAPI + PostgreSQL + Next.js",
    "E-commerce Customer Behavior Analysis  /  Python + Streamlit"
]
for i, line in enumerate(project_lines):
    dashboard += f'<circle cx="577" cy="{421+i*22}" r="3" fill="{GREEN}"/>'
    dashboard += f'<text x="590" y="{425+i*22}" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="11">{html.escape(line)}</text>'

# Contribution calendar panel.
dashboard += f'<rect x="28" y="516" width="660" height="212" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
dashboard += f'<text x="50" y="548" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700">CONTRIBUTION ACTIVITY  /  LAST 12 MONTHS</text>'
if calendar:
    days = [day for week in calendar.get("weeks", []) for day in week.get("contributionDays", [])]
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    for index, day in enumerate(days):
        col, row = divmod(index, 7)
        count = day.get("contributionCount", 0)
        level = 0 if count == 0 else 1 if count < 3 else 2 if count < 6 else 3 if count < 10 else 4
        x, y = 50 + col * 11, 572 + row * 18
        date_label = html.escape(day.get("date", ""))
        dashboard += f'<rect x="{x}" y="{y}" width="8" height="13" rx="2" fill="{colors[level]}"><title>{date_label}: {count} contributions</title></rect>'
    dashboard += f'<text x="50" y="713" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">{contributions} contributions recorded</text>'
else:
    dashboard += f'<text x="50" y="590" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="12">Contribution calendar data unavailable from API</text>'

# Language distribution panel.
dashboard += f'<rect x="708" y="516" width="364" height="212" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
dashboard += f'<text x="730" y="548" fill="{GREEN}" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700">LANGUAGE ACTIVITY</text>'
y = 581
for language, amount in top[:5]:
    pct = amount / total_bytes * 100
    dashboard += f'<text x="730" y="{y}" fill="{TEXT}" font-family="Segoe UI,Arial,sans-serif" font-size="11">{html.escape(language)}</text>'
    dashboard += f'<text x="1048" y="{y}" text-anchor="end" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">{pct:.1f}%</text>'
    dashboard += f'<rect x="730" y="{y+8}" width="318" height="6" rx="3" fill="{GRID}"/>'
    dashboard += f'<rect x="730" y="{y+8}" width="{318*pct/100:.2f}" height="6" rx="3" fill="{GREEN}"/>'
    y += 27
dashboard += f'<text x="28" y="748" fill="{MUTED}" font-family="Segoe UI,Arial,sans-serif" font-size="10">Generated automatically with GitHub Actions  •  github.com/KamalEsakki</text>'
save("profile-dashboard.svg", dashboard)

print("Generated profile SVG cards:", ", ".join(p.name for p in OUT.glob("*.svg")))
