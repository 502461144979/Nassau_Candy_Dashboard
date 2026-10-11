
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Nassau Candy Profitability Dashboard",
    page_icon="🍬",
    layout="wide",
)

DATA_FILE = "nassau_candy_dashboard_data.csv"

# ------------------------------------------------------------
# Premium visual theme
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #163A5F;
        --muted: #54718D;
        --line: #D9E6F2;
        --canvas: #F2F8FD;
        --blue: #5B9BD5;
        --blue-dark: #245580;
        --blue-light: #E3F1FC;
        --white: #FFFFFF;
        --teal: #4F9D9A;
        --orange: #E9A23B;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        font-size: 16px;
    }

    .stApp {
        background: var(--canvas);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: var(--canvas);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    h1, h2, h3 {
        font-family: 'Manrope', sans-serif;
        color: var(--blue-dark) !important;
        font-weight: 800;
    }

    h1 {
        font-size: 32px !important;
    }

    h2 {
        font-size: 24px !important;
    }

    h3 {
        font-size: 19px !important;
    }

    p, li, label {
        font-size: 16px;
        line-height: 1.65;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: var(--blue-light) !important;
        border-right: 1px solid #C7DDED;
    }

    [data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        background: var(--blue-light) !important;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: var(--ink) !important;
    }

    [data-testid="stSidebar"] input {
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
        background: var(--white) !important;
        border-color: #B7D0E5 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: var(--white) !important;
        border-color: #B7D0E5 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] input {
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] label {
        color: var(--ink) !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] input {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        background: var(--white) !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] > div {
        background: var(--white) !important;
        border: 1px solid #B7D0E5 !important;
        border-radius: 8px !important;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] button {
        color: #000000 !important;
        background: var(--white) !important;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] svg {
        color: #000000 !important;
        fill: #000000 !important;
    }

    [data-baseweb="calendar"] button,
    [data-baseweb="calendar"] button div,
    [data-baseweb="calendar"] button span {
        color: var(--ink) !important;
    }

    [data-testid="stSidebar"] [data-baseweb="slider"] div[role="slider"] {
        background: var(--blue) !important;
    }

    /* KPI cards */
    [data-testid="stMetric"] {
        background: var(--white);
        border: 1px solid var(--line);
        border-top: 4px solid var(--blue);
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 3px 12px rgba(36, 85, 128, 0.08);
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
        font-size: 14px;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: var(--blue-dark) !important;
        font-family: 'Manrope', sans-serif;
        font-size: 28px;
        font-weight: 800;
    }

    /* Dashboard hero */
    .nassau-hero {
        background: linear-gradient(
            120deg,
            #EAF4FC 0%,
            #D6EAF9 60%,
            #C3E0F5 100%
        );
        padding: 30px;
        border: 1px solid #C7DDED;
        border-radius: 18px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(36, 85, 128, 0.10);
    }

    .nassau-kicker {
        color: var(--blue-dark) !important;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .nassau-title {
        color: var(--blue-dark) !important;
        font-family: 'Manrope', sans-serif;
        font-size: 32px;
        font-weight: 800;
        margin: 10px 0;
    }

    .nassau-subtitle {
        color: #294F70 !important;
        font-size: 16px;
        line-height: 1.7;
    }

    .nassau-pill {
        display: inline-block;
        background: var(--white);
        color: var(--blue-dark) !important;
        padding: 6px 12px;
        border: 1px solid #C7DDED;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        margin-top: 10px;
    }

    /* Captions and tables */
    [data-testid="stCaptionContainer"] p {
        color: var(--muted) !important;
        font-size: 14px;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        background: var(--white);
        border: 1px solid var(--line);
        border-radius: 10px;
        overflow: hidden;
    }

    /* Tabs */
    [data-baseweb="tab-list"] {
        gap: 10px;
        background: var(--blue-light);
    }

    [data-baseweb="tab"] {
        font-size: 15px;
        font-weight: 600;
        color: var(--blue-dark) !important;
    }

    [data-baseweb="tab"][aria-selected="true"] {
        color: var(--blue-dark) !important;
        border-bottom-color: var(--blue) !important;
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        background: var(--blue) !important;
        color: var(--white) !important;
        border: 1px solid var(--blue) !important;
        border-radius: 8px;
        font-weight: 600;
        padding: 8px 16px;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: var(--blue-dark) !important;
        color: var(--white) !important;
        border-color: var(--blue-dark) !important;
    }

    hr {
        border-color: var(--line) !important;
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }

        .nassau-title {
            font-size: 25px;
        }

        h1 {
            font-size: 27px !important;
        }

        h2 {
            font-size: 21px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Load and validate data
# ------------------------------------------------------------
@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)

    required_columns = [
        "Order Date", "Ship Date", "Division", "Product Name",
        "Sales", "Cost", "Gross Profit", "Units"
    ]

    missing = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            "The CSV is missing required columns: "
            + ", ".join(missing)
        )

    for column in ["Order Date", "Ship Date"]:
        data[column] = pd.to_datetime(
            data[column],
            errors="coerce",
            dayfirst=True,
        )

    for column in ["Sales", "Cost", "Gross Profit", "Units"]:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce",
        )

    data = data.dropna(
        subset=["Order Date", "Division", "Product Name"]
    )

    data["Gross Margin (%)"] = np.where(
        data["Sales"] > 0,
        data["Gross Profit"] / data["Sales"] * 100,
        np.nan,
    )

    data["Profit per Unit"] = np.where(
        data["Units"] > 0,
        data["Gross Profit"] / data["Units"],
        np.nan,
    )

    return data


try:
    df = load_data(DATA_FILE)

except FileNotFoundError:
    st.error(
        f"Could not find `{DATA_FILE}`. "
        "Place it in the same folder as `app.py`."
    )
    st.stop()

except Exception as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()

if df.empty:
    st.error(
        "The dataset contains no usable records after date validation."
    )
    st.stop()


# ------------------------------------------------------------
# Dashboard heading
# ------------------------------------------------------------
st.markdown(
    """
    <div class="nassau-hero">
      <div class="nassau-kicker">
        Data analytics · Executive dashboard
      </div>
      <div class="nassau-title">
        🍬 Nassau Candy Distributor
      </div>
      <div class="nassau-subtitle">
        Nassau Candy Distributor · Product Line Profitability &amp;
        Margin Performance Analysis. Explore revenue, gross profit,
        product margins, division performance, profit concentration
        and monthly trends through an interactive business
        intelligence workspace.
      </div>
      <div class="nassau-pill">
        INTERACTIVE BUSINESS INTELLIGENCE
        &nbsp; · &nbsp; FILTER · ANALYZE · EXPORT
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("About this dashboard"):
    st.write(
        "Gross profit is taken from the dataset. Gross margin is "
        "calculated as Gross Profit divided by Sales, multiplied by "
        "100. Profit per unit is Gross Profit divided by Units. "
        "Financial values are shown without a currency symbol because "
        "the dataset's currency is not specified."
    )

st.divider()


# ------------------------------------------------------------
# Sidebar filters — RESET FIX
# ------------------------------------------------------------
st.sidebar.markdown("## Dashboard Filters")
st.sidebar.caption(
    "Choose a date range and filters to explore performance."
)

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

division_options = [
    "All"
] + sorted(df["Division"].dropna().unique().tolist())


# IMPORTANT:
# This callback runs before Streamlit recreates the widgets.
# Therefore, widget values can be reset safely.
def reset_filters():
    st.session_state["division_filter"] = "All"
    st.session_state["product_search_filter"] = ""
    st.session_state["date_filter"] = (min_date, max_date)
    st.session_state["margin_filter"] = 0


# Division filter
selected_division = st.sidebar.selectbox(
    "Select Division",
    options=division_options,
    key="division_filter",
)

# Product search filter
product_search = st.sidebar.text_input(
    "Search Product",
    placeholder="Enter product name...",
    key="product_search_filter",
)

# Date range filter
selected_dates = st.sidebar.date_input(
    "📅 Select Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    key="date_filter",
)

# Gross margin filter
margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=0,
    max_value=100,
    value=0,
    step=5,
    key="margin_filter",
)

# Reset button — no st.rerun() needed
st.sidebar.button(
    "🔄 Reset Filters",
    use_container_width=True,
    on_click=reset_filters,
    key="reset_filters_button",
)


# ------------------------------------------------------------
# Apply filters
# ------------------------------------------------------------
filtered_df = df.copy()

if selected_division != "All":
    filtered_df = filtered_df[
        filtered_df["Division"] == selected_division
    ]

if product_search.strip():
    filtered_df = filtered_df[
        filtered_df["Product Name"].str.contains(
            product_search.strip(),
            case=False,
            na=False,
            regex=False,
        )
    ]

if isinstance(selected_dates, (tuple, list)):
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates

        filtered_df = filtered_df[
            filtered_df["Order Date"].dt.date.between(
                start_date,
                end_date,
            )
        ]


# Filtered record count
st.sidebar.divider()
st.sidebar.write(
    f"**Filtered records:** {len(filtered_df):,}"
)

st.sidebar.caption(
    "The gross-margin threshold is applied to "
    "product-level summaries and tables."
)


# ------------------------------------------------------------
# Empty-filter handling
# ------------------------------------------------------------
if filtered_df.empty:
    st.warning(
        "No records match the selected division, product search, "
        "and date range. Change or reset the filters to see results."
    )
    st.stop()


# ------------------------------------------------------------
# Visible selected-date banner
# ------------------------------------------------------------
if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    visible_start, visible_end = selected_dates

elif isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 1:
    visible_start = visible_end = selected_dates[0]

else:
    visible_start, visible_end = min_date, max_date

st.markdown(
    f"""
    <div style="
        background:#e3f5ff;
        border:1px solid #b7e1f7;
        border-radius:13px;
        padding:12px 16px;
        margin:0 0 18px 0;
        color:#214c69;
    ">
        <span style="font-weight:800;">📅 Selected order dates</span>
        &nbsp;
        <span>
            {pd.Timestamp(visible_start).strftime("%d %b %Y")}
            —
            {pd.Timestamp(visible_end).strftime("%d %b %Y")}
        </span>
        <span style="color:#49718d;">
            &nbsp; · &nbsp; {len(filtered_df):,} matching records
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# KPI cards
# ------------------------------------------------------------
total_revenue = filtered_df["Sales"].sum()
total_profit = filtered_df["Gross Profit"].sum()
total_cost = filtered_df["Cost"].sum()
total_units = filtered_df["Units"].sum()

gross_margin = (
    total_profit / total_revenue * 100
    if total_revenue > 0
    else 0
)

st.header("Business Performance Overview")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Revenue", f"{total_revenue:,.2f}")
kpi2.metric("Total Gross Profit", f"{total_profit:,.2f}")
kpi3.metric("Gross Margin", f"{gross_margin:.2f}%")
kpi4.metric("Units Sold", f"{total_units:,.0f}")


# ------------------------------------------------------------
# Product and division summaries
# ------------------------------------------------------------
product_summary_all = (
    filtered_df.groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Cost=("Cost", "sum"),
        **{"Gross Profit": ("Gross Profit", "sum")},
        Units=("Units", "sum"),
    )
)

product_summary_all["Gross Margin (%)"] = np.where(
    product_summary_all["Sales"] > 0,
    product_summary_all["Gross Profit"]
    / product_summary_all["Sales"] * 100,
    np.nan,
)

product_summary_all["Profit per Unit"] = np.where(
    product_summary_all["Units"] > 0,
    product_summary_all["Gross Profit"]
    / product_summary_all["Units"],
    np.nan,
)

product_summary_all["Revenue Contribution (%)"] = (
    product_summary_all["Sales"] / total_revenue * 100
    if total_revenue > 0
    else 0
)

product_summary_all["Profit Contribution (%)"] = (
    product_summary_all["Gross Profit"] / total_profit * 100
    if total_profit > 0
    else 0
)

product_summary = product_summary_all[
    product_summary_all["Gross Margin (%)"] >= margin_threshold
].copy()


division_summary = (
    filtered_df.groupby("Division", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Cost=("Cost", "sum"),
        **{"Gross Profit": ("Gross Profit", "sum")},
        Units=("Units", "sum"),
    )
)

division_summary["Gross Margin (%)"] = np.where(
    division_summary["Sales"] > 0,
    division_summary["Gross Profit"]
    / division_summary["Sales"] * 100,
    np.nan,
)

division_summary["Revenue Contribution (%)"] = (
    division_summary["Sales"] / total_revenue * 100
    if total_revenue > 0
    else 0
)


# ------------------------------------------------------------
# Executive Summary
# ------------------------------------------------------------
st.divider()
st.header("Executive Summary")

st.write(
    "Key findings based on the currently selected division, "
    "product search, and date filters."
)

if not division_summary.empty and not product_summary_all.empty:

    best_division_row = division_summary.loc[
        division_summary["Gross Profit"].idxmax()
    ]

    highest_margin_row = product_summary_all.loc[
        product_summary_all["Gross Margin (%)"].idxmax()
    ]

    lowest_margin_row = product_summary_all.loc[
        product_summary_all["Gross Margin (%)"].idxmin()
    ]

    summary1, summary2, summary3 = st.columns(3)

    summary1.metric(
        "Best-Performing Division",
        str(best_division_row["Division"]),
        delta=f"{best_division_row['Gross Margin (%)']:.2f}% gross margin",
    )

    summary2.metric(
        "Highest-Margin Product",
        str(highest_margin_row["Product Name"]),
        delta=f"{highest_margin_row['Gross Margin (%)']:.2f}% margin",
    )

    summary3.metric(
        "Lowest-Margin Product",
        str(lowest_margin_row["Product Name"]),
        delta=f"{lowest_margin_row['Gross Margin (%)']:.2f}% margin",
        delta_color="inverse",
    )

    summary4, summary5 = st.columns(2)

    summary4.metric("Overall Gross Margin", f"{gross_margin:.2f}%")
    summary5.metric("Total Gross Profit", f"{total_profit:,.2f}")

else:
    st.info(
        "There are not enough product or division results "
        "to build the Executive Summary."
    )


# ------------------------------------------------------------
# Product Profitability Analysis
# ------------------------------------------------------------
st.divider()
st.header("Product Profitability Analysis")

st.caption(
    f"Products shown here meet the selected minimum gross margin "
    f"of {margin_threshold}%."
)

if product_summary.empty:
    st.warning(
        f"No products meet the minimum gross margin threshold "
        f"of {margin_threshold}%. Lower the threshold in the "
        "sidebar to view products."
    )

else:
    top_products = product_summary.sort_values(
        "Gross Profit",
        ascending=False,
    ).head(10)

    fig_product = px.bar(
        top_products.sort_values("Gross Profit", ascending=True),
        x="Gross Profit",
        y="Product Name",
        orientation="h",
        title="Top Products by Gross Profit (Meeting Margin Threshold)",
        text_auto=".2f",
        color="Gross Profit",
        color_continuous_scale=[
            [0, "#d9f0ff"],
            [1, "#258bc5"],
        ],
        labels={
            "Gross Profit": "Gross Profit",
            "Product Name": "Product",
        },
    )

    fig_product.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig_product, use_container_width=True)

    st.metric(
        "Products Meeting Margin Threshold",
        f"{len(product_summary):,}",
    )


# ------------------------------------------------------------
# Division Performance Analysis
# ------------------------------------------------------------
st.divider()
st.header("Division Performance Analysis")

if division_summary.empty:
    st.info("No division data is available for the selected filters.")

else:
    div_col1, div_col2 = st.columns(2)

    with div_col1:
        fig_division_profit = px.bar(
            division_summary.sort_values(
                "Gross Profit",
                ascending=False,
            ),
            x="Division",
            y="Gross Profit",
            title="Gross Profit by Division",
            text_auto=".2f",
            color="Division",
        )

        st.plotly_chart(
            fig_division_profit,
            use_container_width=True,
        )

    with div_col2:
        fig_division_margin = px.bar(
            division_summary.sort_values(
                "Gross Margin (%)",
                ascending=False,
            ),
            x="Division",
            y="Gross Margin (%)",
            title="Gross Margin by Division",
            text_auto=".2f",
            color="Division",
        )

        st.plotly_chart(
            fig_division_margin,
            use_container_width=True,
        )


# ------------------------------------------------------------
# Profit Contribution (Pareto) Analysis
# ------------------------------------------------------------
st.divider()
st.header("Profit Contribution Analysis (Pareto)")

pareto_df = (
    filtered_df.groupby("Product Name", as_index=False)["Gross Profit"]
    .sum()
    .sort_values("Gross Profit", ascending=False)
)

total_product_profit = pareto_df["Gross Profit"].sum()

if not pareto_df.empty and total_product_profit > 0:

    pareto_df["Profit Contribution (%)"] = (
        pareto_df["Gross Profit"] / total_product_profit * 100
    )

    pareto_df["Cumulative Profit (%)"] = (
        pareto_df["Profit Contribution (%)"].cumsum()
    )

    fig_pareto = go.Figure()

    fig_pareto.add_trace(
        go.Bar(
            x=pareto_df["Product Name"],
            y=pareto_df["Gross Profit"],
            name="Gross Profit",
        )
    )

    fig_pareto.add_trace(
        go.Scatter(
            x=pareto_df["Product Name"],
            y=pareto_df["Cumulative Profit (%)"],
            name="Cumulative Profit (%)",
            yaxis="y2",
            mode="lines+markers",
        )
    )

    fig_pareto.add_hline(
        y=80,
        line_dash="dash",
        line_color="#369bd6",
        yref="y2",
        annotation_text="80% cumulative profit",
    )

    fig_pareto.update_layout(
        title="Product-wise Profit Contribution (Pareto Chart)",
        xaxis_title="Product Name",
        yaxis=dict(title="Gross Profit"),
        yaxis2=dict(
            title="Cumulative Profit (%)",
            overlaying="y",
            side="right",
            range=[0, 110],
        ),
        xaxis_tickangle=-45,
    )

    st.plotly_chart(fig_pareto, use_container_width=True)

    products_to_80 = int(
        (pareto_df["Cumulative Profit (%)"] < 80).sum() + 1
    )

    products_to_80 = min(products_to_80, len(pareto_df))

    st.write(
        f"**Products needed to reach at least 80% of gross profit:** "
        f"{products_to_80} of {len(pareto_df)} products."
    )

else:
    st.info(
        "No positive gross profit is available for Pareto analysis "
        "under the current filters."
    )


# ------------------------------------------------------------
# Cost vs Gross Profit Analysis
# ------------------------------------------------------------
st.divider()
st.header("Cost vs Gross Profit Analysis")

cost_profit_df = (
    filtered_df.groupby("Product Name", as_index=False)
    .agg(
        Cost=("Cost", "sum"),
        **{
            "Gross Profit": ("Gross Profit", "sum"),
            "Sales": ("Sales", "sum"),
        },
    )
)

cost_profit_df["Gross Margin (%)"] = np.where(
    cost_profit_df["Sales"] > 0,
    cost_profit_df["Gross Profit"]
    / cost_profit_df["Sales"] * 100,
    np.nan,
)

if not cost_profit_df.empty:

    fig_cost = px.scatter(
        cost_profit_df,
        x="Cost",
        y="Gross Profit",
        size="Sales",
        color="Gross Margin (%)",
        hover_name="Product Name",
        title="Product-wise Cost vs Gross Profit",
        color_continuous_scale=[
            [0, "#d9f0ff"],
            [0.5, "#62b9e8"],
            [1, "#176b9d"],
        ],
        size_max=40,
    )

    fig_cost.update_layout(
        xaxis_title="Total Cost",
        yaxis_title="Total Gross Profit",
    )

    st.plotly_chart(fig_cost, use_container_width=True)


# ------------------------------------------------------------
# Monthly Sales, Profit, and Margin Trends
# ------------------------------------------------------------
st.divider()
st.header("Monthly Sales, Profit, and Margin Trends")

monthly_df = filtered_df.copy()

monthly_df["Month"] = (
    monthly_df["Order Date"].dt.to_period("M").dt.to_timestamp()
)

monthly_summary = (
    monthly_df.groupby("Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        **{"Gross Profit": ("Gross Profit", "sum")},
    )
)

monthly_summary["Gross Margin (%)"] = np.where(
    monthly_summary["Sales"] > 0,
    monthly_summary["Gross Profit"]
    / monthly_summary["Sales"] * 100,
    np.nan,
)

if not monthly_summary.empty:

    trend1, trend2 = st.columns(2)

    with trend1:
        fig_monthly_revenue = px.line(
            monthly_summary,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Revenue Trend",
        )

        fig_monthly_revenue.update_layout(
            xaxis_title="Month",
            yaxis_title="Total Revenue",
        )

        st.plotly_chart(
            fig_monthly_revenue,
            use_container_width=True,
        )

    with trend2:
        fig_monthly_profit = px.line(
            monthly_summary,
            x="Month",
            y="Gross Profit",
            markers=True,
            title="Monthly Gross Profit Trend",
        )

        fig_monthly_profit.update_layout(
            xaxis_title="Month",
            yaxis_title="Total Gross Profit",
        )

        st.plotly_chart(
            fig_monthly_profit,
            use_container_width=True,
        )

    fig_margin = px.line(
        monthly_summary,
        x="Month",
        y="Gross Margin (%)",
        markers=True,
        title="Monthly Gross Margin Percentage",
    )

    fig_margin.update_layout(
        xaxis_title="Month",
        yaxis_title="Gross Margin (%)",
    )

    st.plotly_chart(fig_margin, use_container_width=True)


# ------------------------------------------------------------
# Detailed Product Profitability
# ------------------------------------------------------------
st.divider()
st.header("Detailed Product Profitability")

detailed_product = product_summary.copy().sort_values(
    "Gross Profit",
    ascending=False,
)

if detailed_product.empty:
    st.warning(
        "No products meet the current margin threshold. "
        "Lower the threshold to view the table."
    )

else:
    st.dataframe(
        detailed_product.style.format({
            "Sales": "{:,.2f}",
            "Cost": "{:,.2f}",
            "Gross Profit": "{:,.2f}",
            "Units": "{:,.0f}",
            "Gross Margin (%)": "{:.2f}%",
            "Profit per Unit": "{:,.2f}",
            "Revenue Contribution (%)": "{:.2f}%",
            "Profit Contribution (%)": "{:.2f}%",
        }),
        use_container_width=True,
        hide_index=True,
    )

    product_csv = detailed_product.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Product Profitability Table (CSV)",
        data=product_csv,
        file_name="Nassau_Candy_Product_Profitability.csv",
        mime="text/csv",
    )


# ------------------------------------------------------------
# Detailed Division Performance
# ------------------------------------------------------------
st.divider()
st.header("Detailed Division Performance")

detailed_division = division_summary.copy().sort_values(
    "Gross Profit",
    ascending=False,
)

if not detailed_division.empty:

    st.dataframe(
        detailed_division.style.format({
            "Sales": "{:,.2f}",
            "Cost": "{:,.2f}",
            "Gross Profit": "{:,.2f}",
            "Units": "{:,.0f}",
            "Gross Margin (%)": "{:.2f}%",
            "Revenue Contribution (%)": "{:.2f}%",
        }),
        use_container_width=True,
        hide_index=True,
    )


# ------------------------------------------------------------
# Business Recommendations
# ------------------------------------------------------------
st.divider()
st.header("💡 Business Recommendations")

st.caption(
    "Actionable next steps based on the current analysis "
    "and selected filters."
)

if not product_summary_all.empty:

    recommendation_product = product_summary_all.loc[
        product_summary_all["Gross Margin (%)"].idxmin()
    ]

    st.info(
        f"**Review pricing and costs for "
        f"{recommendation_product['Product Name']}.** "
        f"It has the lowest gross margin "
        f"({recommendation_product['Gross Margin (%)']:.2f}%) "
        "among products in the current filtered data. Review "
        "ingredient/material costs, other direct costs, sales "
        "volume, and customer demand before making pricing "
        "or product decisions."
    )

    rec1, rec2, rec3 = st.columns(3)

    with rec1:
        st.markdown("#### 📉 Investigate low margins")
        st.write(
            "Review cost drivers and pricing for low-margin "
            "products before deciding on changes."
        )

    with rec2:
        st.markdown("#### ⭐ Learn from top performers")
        st.write(
            "Compare high-margin products' pricing and cost "
            "structure while considering demand and volume."
        )

    with rec3:
        st.markdown("#### 📊 Monitor performance")
        st.write(
            "Track division results and monthly gross margin "
            "to identify changes that deserve further investigation."
        )

else:
    st.info(
        "Business recommendations will appear when product "
        "data is available. Adjust the filters to view products."
    )


# ------------------------------------------------------------
# Download Dashboard Data
# ------------------------------------------------------------
st.subheader("Download Dashboard Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Dashboard Data",
    data=csv_data,
    file_name="nassau_candy_dashboard_data.csv",
    mime="text/csv",
    use_container_width=True,
    key="download_dashboard_data",
)
