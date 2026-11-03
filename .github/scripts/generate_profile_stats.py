#!/usr/bin/env python3
import os, json, html, urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

USER = "KamalEsakki"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path("dist")
OUT.mkdir(exist_ok=True)
BG, PANEL, GREEN, TEXT, MUTED, GRID = "#080d17", "#0e1726", "#34d399", "#e5edf7", "#91a4b8", "#203044"
FONT = "Segoe UI,Arial,sans-serif"

def api(url, method="GET", payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    if data:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.loads(res.read().decode())

def esc(value):
    return html.escape(str(value), quote=True)

parts = []
def rect(x,y,w,h,fill=PANEL,stroke=GRID,rx=14):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>')
def txt(x,y,value,size=14,color=TEXT,weight=400):
    parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}">{esc(value)}</text>')
def line(x1,y1,x2,y2,color=GRID):
    parts.append(f'<path d="M{x1} {y1} H{x2}" stroke="{color}" stroke-width="1"/>')
def heading(x,y,value):
    txt(x,y,value,16,GREEN,700)

profile = api("https://api.github.com/users/" + USER)
repos = api("https://api.github.com/users/" + USER + "/repos?per_page=100&type=owner&sort=updated")
stars = sum(r.get("stargazers_count",0) for r in repos)
forks = sum(r.get("forks_count",0) for r in repos)
languages = {}
for repo in repos:
    if repo.get("fork"):
        continue
    try:
        for lang, count in api(repo["languages_url"]).items():
            languages[lang] = languages.get(lang,0) + count
    except Exception as exc:
        print("Language data skipped:", repo.get("name"), exc)
top = sorted(languages.items(), key=lambda x:x[1], reverse=True)[:6]
total_bytes = sum(languages.values()) or 1

calendar = None
today = datetime.now(timezone.utc).date()
start = today - timedelta(days=364)
query = """query($login:String!, $from:DateTime!, $to:DateTime!) {
 user(login:$login) { contributionsCollection(from:$from,to:$to) {
 contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } }
 } }
}"""
try:
    gql = api("https://api.github.com/graphql","POST",{
        "query":query,
        "variables":{"login":USER,"from":start.isoformat()+"T00:00:00Z","to":today.isoformat()+"T23:59:59Z"}
    })
    calendar = gql.get("data",{}).get("user",{}).get("contributionsCollection",{}).get("contributionCalendar")
except Exception as exc:
    print("Contribution calendar unavailable:", exc)
contributions = calendar.get("totalContributions",0) if calendar else 0

W,H = 1120,1370
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Kamal Esakki developer profile dashboard">')
parts.append(f'<defs><linearGradient id="top" x1="0" x2="1"><stop offset="0" stop-color="#064e3b"/><stop offset="1" stop-color="#10b981"/></linearGradient></defs><rect width="100%" height="100%" rx="20" fill="{BG}"/>')
parts.append('<rect x="0" y="0" width="1120" height="12" fill="url(#top)"/>')
txt(42,66,"T. KAMAL ESAKKI",34,TEXT,700)
txt(44,99,"BACKEND DEVELOPER  /  API ENGINEER  /  MCP ENTHUSIAST",14,GREEN,700)
txt(44,129,"B.E. Computer Science and Engineering  •  2026",13,MUTED)
txt(44,164,"Building backend services, API integrations and automation-driven applications.",14,TEXT)
rect(40,190,1040,104)
metrics = [("PUBLIC REPOSITORIES",profile.get("public_repos",len(repos))),("TOTAL STARS",stars),("FOLLOWERS",profile.get("followers",0)),("FORKS",forks),("CONTRIBUTIONS / YEAR",contributions)]
for i,(label,value) in enumerate(metrics):
    x=62+i*204
    txt(x,229,label,10,MUTED,700)
    txt(x,270,str(value),28,TEXT,700)

# Education and experience
rect(40,316,500,206); heading(62,350,"EDUCATION")
txt(62,385,"B.E. Computer Science and Engineering",15,TEXT,700)
txt(62,410,"Unnamalai Institute of Technology",13,MUTED)
txt(62,437,"2022 – 2026  •  CGPA: 7.77",12,GREEN)
line(62,455,516)
txt(62,482,"HSC / SSLC  •  St. Xavier Higher Secondary School",12,TEXT)
rect(560,316,520,206); heading(582,350,"PROFESSIONAL EXPERIENCE")
txt(582,385,"Backend Developer  /  Zeeyes AI Labs",15,TEXT,700)
txt(582,410,"Backend services • REST APIs • OAuth 2.0 • CRM integrations",12,MUTED)
txt(582,440,"Data Science Intern  /  Extazee Software Solution",14,TEXT,700)
txt(582,465,"Python • Pandas • NumPy • Data processing",12,MUTED)
txt(582,494,"Trichy  •  June 2025 – July 2025",11,GREEN)

# Technical stack
rect(40,544,1040,196); heading(62,579,"TECHNICAL TOOLKIT")
skill_rows = [
("BACKEND","Node.js  •  NestJS  •  Express.js  •  FastAPI  •  REST APIs"),
("LANGUAGES","Python  •  JavaScript  •  TypeScript  •  SQL  •  Java (Beginner)"),
("FRONTEND","HTML  •  CSS  •  React  •  Next.js  •  Tailwind CSS"),
("DATABASES","PostgreSQL  •  MySQL  •  MongoDB  •  TypeORM  •  SQLAlchemy"),
("INTEGRATION","JWT  •  OAuth 2.0  •  Google OAuth  •  Zoho CRM  •  HubSpot  •  MCP"),
("TOOLS & ANALYTICS","Docker  •  Git  •  Postman  •  n8n  •  Power BI  •  Excel  •  UiPath  •  GCP")
]
for i,(label,value) in enumerate(skill_rows):
    y=612+i*21
    txt(62,y,label,10,GREEN,700)
    txt(205,y,value,12,TEXT)

# Project highlights
rect(40,762,1040,250); heading(62,797,"SELECTED PROJECTS")
projects = [
("01  ZOHO CRM → HUBSPOT MIGRATION + MCP","NestJS • TypeScript • PostgreSQL • TypeORM • OAuth 2.0 • CRM APIs","CRM data migration, email-based contact matching, API integration and MCP tool integration."),
("02  STOCK SENTINEL","FastAPI • PostgreSQL • SQLAlchemy • JWT • Next.js • Docker • Finnhub","Stock monitoring application with backend APIs, authentication and dashboard visualizations."),
("03  E-COMMERCE CUSTOMER BEHAVIOR ANALYSIS","Python • Pandas • NumPy • Streamlit • Clustering • Association Analysis","Customer purchase pattern analysis, segmentation and interactive data presentation.")
]
for i,(name,stack,desc) in enumerate(projects):
    y=835+i*57
    txt(62,y,name,13,TEXT,700)
    txt(62,y+19,stack,11,GREEN)
    txt(62,y+38,desc,11,MUTED)

# Additional capabilities and current learning
rect(40,1034,500,148); heading(62,1068,"API & ENGINEERING")
for i,v in enumerate(["CRUD APIs • Request validation • Error handling","JWT authentication • OAuth 2.0 • RBAC • Webhooks","COQL • Data migration • MCP servers and tools"]):
    txt(62,1100+i*24,v,12,TEXT)
rect(560,1034,520,148); heading(582,1068,"LEARNING & TRAINING")
for i,v in enumerate(["Agentic AI • MCP architecture • n8n workflow automation","Data Analyst training: Python • SQL • Excel • Power BI","Full Stack Development internship training"]):
    txt(582,1100+i*24,v,12,TEXT)

# Contribution calendar and language stats
rect(40,1204,660,128); heading(62,1238,"CONTRIBUTION ACTIVITY  /  LAST 12 MONTHS")
if calendar:
    days=[d for w in calendar.get("weeks",[]) for d in w.get("contributionDays",[])]
    palette=["#172231","#064e3b","#047857","#10b981","#6ee7b7"]
    for idx,d in enumerate(days):
        col,row=divmod(idx,7)
        count=d.get("contributionCount",0)
        level=0 if count==0 else 1 if count<3 else 2 if count<6 else 3 if count<10 else 4
        x=62+col*10.2; y=1254+row*9.5
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="7.5" height="7.5" rx="1.5" fill="{palette[level]}"><title>{esc(d.get("date",""))}: {count} contributions</title></rect>')
    txt(62,1319,str(contributions)+" contributions in the last year",10,MUTED)
else:
    txt(62,1280,"Contribution calendar data currently unavailable",12,MUTED)
rect(720,1204,360,128); heading(742,1238,"LANGUAGE ACTIVITY")
for i,(lang,count) in enumerate(top[:4]):
    y=1260+i*17
    pct=count/total_bytes*100
    txt(742,y,lang,10,TEXT)
    txt(1054,y,f"{pct:.1f}%",10,MUTED)
    parts.append(f'<rect x="742" y="{y+4}" width="310" height="3" rx="1.5" fill="{GRID}"/><rect x="742" y="{y+4}" width="{310*pct/100:.2f}" height="3" rx="1.5" fill="{GREEN}"/>')

txt(42,1355,"GITHUB.COM/KAMALESAAKKI",10,GREEN,700)
txt(1078,1355,"GENERATED WITH GITHUB ACTIONS",9,MUTED,400)
parts.append("</svg>")
(OUT/"profile-dashboard.svg").write_text("\n".join(parts),encoding="utf-8")
print("Generated profile-dashboard.svg")
