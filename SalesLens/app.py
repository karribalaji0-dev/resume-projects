"""SalesLens: an interactive sales dashboard using Streamlit and pandas."""
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="SalesLens", page_icon="📊", layout="wide")
st.title("📊 SalesLens")
st.caption("Explore a sample sales dataset, find patterns, and download your filtered view.")

DATA_FILE = Path(__file__).parent / "sales.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE, parse_dates=["order_date"])
    df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
    return df

df = load_data()
st.sidebar.header("Filters")
regions = st.sidebar.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
categories = st.sidebar.multiselect("Category", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
min_date, max_date = df["order_date"].min().date(), df["order_date"].max().date()
dates = st.sidebar.date_input("Order date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

if len(dates) == 2:
    start_date, end_date = dates
else:
    start_date = end_date = dates[0]
filtered = df[df["region"].isin(regions) & df["category"].isin(categories) & df["order_date"].dt.date.between(start_date, end_date)].copy()

if filtered.empty:
    st.info("No orders match those filters. Choose a wider date range or more categories.")
else:
    revenue = filtered["revenue"].sum()
    orders = filtered["order_id"].nunique()
    units = filtered["quantity"].sum()
    average = revenue / orders if orders else 0
    a, b, c, d = st.columns(4)
    a.metric("Revenue", f"${revenue:,.0f}")
    b.metric("Orders", f"{orders:,}")
    c.metric("Units sold", f"{units:,}")
    d.metric("Average order value", f"${average:,.2f}")

    st.subheader("Revenue over time")
    monthly = filtered.assign(order_date=filtered["order_date"].dt.to_period("M").dt.to_timestamp()).groupby("order_date")["revenue"].sum()
    st.line_chart(monthly, x_label="Month", y_label="Revenue ($)")

    left, right = st.columns(2)
    with left:
        st.subheader("Revenue by category")
        st.bar_chart(filtered.groupby("category")["revenue"].sum().sort_values(ascending=False), x_label="Category", y_label="Revenue ($)")
    with right:
        st.subheader("Revenue by region")
        st.bar_chart(filtered.groupby("region")["revenue"].sum().sort_values(ascending=False), x_label="Region", y_label="Revenue ($)")

    st.subheader("Filtered orders")
    display = filtered.sort_values("order_date", ascending=False).copy()
    display["order_date"] = display["order_date"].dt.strftime("%Y-%m-%d")
    st.dataframe(display, use_container_width=True, hide_index=True)
    st.download_button("Download filtered CSV", data=filtered.to_csv(index=False).encode("utf-8"), file_name="saleslens-filtered-orders.csv", mime="text/csv")

st.caption("Dataset is synthetic and included for learning. Revenue is quantity × unit price after discount; it is not profit.")
