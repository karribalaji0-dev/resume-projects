# Portfolio Projects

Four beginner-friendly projects demonstrating web development, databases, and Python data tools. Demo data is fictional.

## Projects

- **ApplyTrack** — browser-based job application tracker with editable records, filters, reminders, summary counts, and JSON backup. [Source](ApplyTrack.html) · [Guide](ApplyTrack-README.md)
- **SalesLens** — Streamlit and pandas sales dashboard with filters, metrics, charts, and CSV export. [Project folder](SalesLens/) · [Guide](SalesLens/README.md)
- **HelpDesk Lite** — Flask and SQLite support-ticket website with create/edit/delete, search, priority, and status tracking.
- **CSVDoctor** — Python command-line CSV cleaner that normalizes data and writes a quality report.

[Download the complete project bundle](ResumeProjects-Expanded.zip) for HelpDesk Lite, CSVDoctor, and all other project files. Setup guides and sample resume bullets are included.

## Run SalesLens

Install Python 3.10 or newer. In a terminal inside `SalesLens`, run:

```text
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The ApplyTrack data stays in that browser on that device. HelpDesk is a local learning demo with no login; do not put real customer details in it. Check each project README for full setup steps. Personalize each project and be ready to explain the code before listing it on a resume.
