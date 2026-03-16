# Superstore Sales Data Analysis

An exploratory data analysis (EDA) project on the [Superstore dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) from Kaggle, using Python and Jupyter Notebook. The project investigates sales performance, profitability, customer behavior, and shipping patterns across a US retail superstore from 2014-2017.

---

## Questions Explored

1. What does overall sales and profit look like across the dataset?
2. Which product categories sell the most — and are they actually the most profitable?
3. Which sub-categories have high sales but negative profit?
4. Does discount percentage correlate with profit loss?
5. Which customer segment generates the most revenue and profit?
6. How do sales and profit trend over time per category?
7. Which cities and regions have the highest order volume?
8. What is the average shipping time per city, and does ship mode affect profitability?
9. Can we predict profit of a category based on discount?

---

## Getting Started

### Prerequisites
- Python 3.x
- [uv](https://github.com/astral-sh/uv) package manager
- A Kaggle account (for dataset download)

### Installation & Setup

**Step 1: Install dependencies**
```bash
pip install uv
uv sync
```

**Step 2: Download the dataset**
```bash
uv run python download_dataset.py
```
> Make sure your Kaggle API credentials are configured before running this. See [Kaggle API setup](https://github.com/Kaggle/kaggle-api#api-credentials).

**Step 3: Launch Jupyter Notebook**
```bash
uv run jupyter notebook
```

**Step 4:** Open `analysis.ipynb` and run all cells.

---

## Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation and analysis |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical visualizations |
| `plotly` | Interactive charts |
| `scikit-learn` | Linear regression model |
| `kagglehub` | Dataset download |

---

## Key Findings

### Does discount percentage correlate with profit loss?
Discounts above 30% strongly correlate with profit loss. Transactions with no discount yield the highest profits, while those with 60-80% discounts are almost entirely unprofitable.

![Discount vs Profit](/screenshots/Discount_vs_Profit.png)

---

### Which customer segment generates the most revenue and profit?
The Consumer segment leads in both sales and profit, followed by Corporate and Home Office. However, all three segments show a large gap between sales and profit volume.

![Sales and Profit by Customer Segment](/screenshots/Sales_Profit_Customer_Segment.png)

---

### How do sales and profit trend over time per category?
All three categories show overall sales growth from 2014-2017. Technology generates the highest profit spikes, Office Supplies is consistently profitable, and Furniture repeatedly dips into negative profit despite comparable sales.

![Sales and Profit Trend by Category](/screenshots/Trend_By_Category.png)

---

### Does ship mode affect profitability?
Ship mode has minimal impact on profitability — all four modes cluster within a 2% profit margin range (12-14%), with First Class slightly ahead.

![Profit Margin % by Ship Mode](/screenshots/Profit_Margin_Ship_Mode.png)

---

### Can we predict profit based on discount?
Discount alone is a weak predictor of profit (R² = 0.06 overall). The model struggles to capture the wide variance in actual profits, as seen by the scattered points deviating far from the ideal prediction line.

![Actual vs Predicted Profit](/screenshots/Profit_Prediction.png)

---

## Dataset

- **Source:** [Superstore Dataset - Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **File:** `Sample - Superstore.csv`
- **Records:** 9,994 rows, 21 columns
- **Period:** 2014-2017
- **No null values** found in the dataset.