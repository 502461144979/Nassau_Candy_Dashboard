# Nassau Candy Distributor — Product Line Profitability & Margin Performance Analysis

## 1. Project Overview

This project analyzes the sales, costs, gross profit, and gross margins of Nassau Candy Distributor to identify profitable products, compare division performance, and support data-driven business decisions.

An interactive dashboard was developed using Python and Streamlit to present key performance indicators, product profitability, division-level comparisons, Pareto analysis, and monthly trends.

## 2. Project Objectives

- Analyze overall sales, gross profit, gross margin, and units sold.
- Identify the highest- and lowest-performing products based on profitability and gross margin.
- Compare revenue, gross profit, and gross margin across divisions.
- Identify products contributing to approximately 80% of total gross profit using Pareto analysis.
- Examine monthly revenue, profit, and gross margin trends.
- Highlight products that may require further pricing or cost investigation.
- Present findings through an interactive dashboard.

## 3. Technologies Used

- **Python** — Data analysis and calculations.
- **Pandas** — Data cleaning, transformation, and aggregation.
- **NumPy** — Numerical calculations.
- **Plotly** — Interactive charts and visualizations.
- **Streamlit** — Interactive dashboard development.
- **Jupyter Notebook / Google Colab** — Exploratory data analysis.

## 4. Dataset Description

The dataset contains 10,194 records and 18 original columns covering orders, dates, locations, divisions, products, sales, units, gross profit, and cost.

Important fields include:

- Order Date
- Division
- Product Name
- Sales
- Units
- Gross Profit
- Cost

Additional analytical metrics include Gross Margin (%), Profit per Unit, Revenue Contribution (%), and Profit Contribution (%).

## 5. Data Cleaning and Preparation

The analysis includes:

- Checking missing values and duplicate records.
- Converting order and shipping dates into datetime format.
- Validating numeric sales, cost, units, and gross profit values.
- Verifying gross profit consistency using Sales − Cost.
- Creating additional profitability metrics for product and division analysis.

## 6. Key Performance Indicators

The dashboard presents the following KPIs:

- Total Revenue
- Total Gross Profit
- Gross Margin (%)
- Units Sold
- Profit per Unit
- Revenue Contribution (%)
- Profit Contribution (%)
- Product Margin and Profitability Comparisons

## 7. Dashboard Features

- Interactive filters for date range, division, product search, and minimum gross margin.
- KPI summary cards.
- Product profitability analysis.
- Division performance comparisons.
- Pareto analysis of gross profit contribution.
- Monthly sales, gross profit, and margin trends.
- Product margin risk screening.
- Detailed product and transaction tables.
- Downloadable analysis data, where available.

## 8. Key Findings

- Chocolate is the leading division by total gross profit in the analyzed dataset.
- Everlasting Gobstopper has the highest gross margin among the analyzed products.
- Kazookles has the lowest gross margin among the analyzed products.
- Wonka Bar - Scrumdiddlyumptious has the highest total gross profit among the analyzed products.
- The analysis identifies products and divisions that may benefit from further pricing, cost, and sales-volume investigation.

## 9. Business Recommendations

- Review pricing and cost structures for products with low gross margins.
- Investigate the factors behind differences in profitability across divisions.
- Monitor monthly revenue, gross profit, and gross margin trends.
- Evaluate high-margin products for suitable promotional opportunities while considering demand and sales volume.
- Use the dashboard filters to investigate specific products, divisions, and periods before making business decisions.

## 10. Project Folder Structure

```text
Nassau_Candy_Dashboard/
│
├── app.py
├── nassau_candy_dashboard_data.csv
├── requirements.txt
├── README.md
└── Nassau_Candy_Profitability_Analysis.ipynb
```

The notebook filename above is an example; use the actual filename of your saved notebook.

## 11. Installation and Execution

### Prerequisites

- Python installed on your computer.
- The project files saved in the same folder.

### Install Dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install -r requirements.txt
```

### Run the Dashboard

Execute:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to access the dashboard.

## 12. Conclusion

This project demonstrates how data analysis and interactive visualization can be used to understand product profitability, compare division performance, identify margin concerns, and support data-driven business decisions.

The dashboard provides an interactive way to explore profitability metrics and investigate areas that may require further business analysis.

## 13. Author

**Name:** [Priti Chandrakant Sonwane]  
**Internship Organization:** Unified Mentor  
**Project Domain:** Data Analytics  
**Project Title:** Product Line Profitability & Margin Performance Analysis for Nassau Candy Distributor
