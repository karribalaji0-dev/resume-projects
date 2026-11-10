# Portfolio Projects

Two small projects built to practice web development and Python data analysis. All records in the demos are fictional.

## 1. ApplyTrack — job application tracker

A responsive browser app for adding, editing, searching, filtering, and sorting job applications. It tracks status and follow-up dates, shows summary counts, and supports JSON backup and restore.

- [Open the app source](ApplyTrack.html)
- [ApplyTrack guide and resume bullets](ApplyTrack-README.md)
- Open `ApplyTrack.html` in a modern browser to use it. Data stays in local browser storage and does not sync across devices.

## 2. SalesLens — sales analytics dashboard

A Streamlit and pandas dashboard with date, region, and category filters, sales metrics, charts, and filtered CSV download. Revenue is calculated after discount; this sample does not include costs and does not report profit.

- [SalesLens folder](SalesLens/)
- [SalesLens setup guide and resume bullets](SalesLens/README.md)

To run SalesLens, install Python 3.10 or newer, open a terminal in `SalesLens`, then run:

```text
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Resume wording

The project-specific READMEs include sample bullets. Personalize the projects and make sure you can explain the code before adding them to a resume.
