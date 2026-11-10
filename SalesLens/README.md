# SalesLens

SalesLens is a small interactive analytics dashboard built with Streamlit and pandas. It uses the included synthetic orders dataset and lets a viewer filter by region, product category, and date. The dashboard recalculates revenue, orders, units, and average order value, shows time/category/region charts, and downloads the filtered rows.

## Run it

Install Python 3.10 or newer. In a terminal opened in this folder, run:

```text
python -m venv .venv
```

Activate the environment:

```text
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install dependencies and launch the dashboard:

```text
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The browser opens the dashboard. Stop it with Ctrl+C in the terminal.

## Project files

- `app.py` — dashboard, filtering, metrics, charts, and CSV download
- `sales.csv` — fictional sample order records
- `requirements.txt` — Python packages needed to run it

## Metric definition

Revenue = quantity × unit price × (1 − discount). This sample does not include cost, so revenue should not be described as profit. All dataset records are synthetic.

## Resume bullets (use only after you can explain the code)

- Built a filterable sales analytics dashboard in Python with Streamlit and pandas, including revenue KPIs, date/region/category filters, and interactive charts.
- Added a downloadable filtered CSV and documented the revenue calculation and synthetic data assumptions.
