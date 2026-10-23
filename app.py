
import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="SpendWise | Expense Manager",
    page_icon="💸",
    layout="wide"
)

# ---------------- DARK DASHBOARD DESIGN ----------------
st.markdown("""
<style>
    .stApp {
        background: #0b1120;
        color: #e5e7eb;
    }

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #253047;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #f8fafc;
    }

    .hero {
        background: linear-gradient(120deg, #172554, #172033, #123047);
        border: 1px solid #263b60;
        border-radius: 18px;
        padding: 26px;
        margin-bottom: 22px;
        animation: fadeIn 0.8s ease-out;
    }

    .hero h1 {
        margin: 0;
        font-size: 30px;
    }

    .hero p {
        color: #bac8dd;
        margin-bottom: 0;
    }

    .metric-card {
        background: linear-gradient(145deg, #172033, #111827);
        border: 1px solid #29364c;
        border-radius: 16px;
        padding: 20px;
        min-height: 125px;
        animation: fadeIn 0.7s ease-out;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        border-color: #38bdf8;
    }

    .metric-label {
        color: #9caec4;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 26px;
        font-weight: 700;
    }

    .metric-note {
        color: #93a4bb;
        font-size: 12px;
        margin-top: 8px;
    }

    .section-heading {
        color: #f1f5f9;
        font-size: 20px;
        font-weight: 650;
        margin-top: 24px;
        margin-bottom: 12px;
    }

    .budget-card {
        background: #111827;
        border: 1px solid #29364c;
        border-radius: 16px;
        padding: 20px;
        animation: fadeIn 1s ease-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------- SAMPLE TRANSACTIONS ----------------
transactions = [
    {"Date": "2026-10-02", "Description": "Groceries", "Category": "Food", "Type": "Expense", "Amount": 1250},
    {"Date": "2026-10-04", "Description": "Bus pass", "Category": "Transport", "Type": "Expense", "Amount": 600},
    {"Date": "2026-10-06", "Description": "Freelance work", "Category": "Income", "Type": "Income", "Amount": 4500},
    {"Date": "2026-10-08", "Description": "Mobile recharge", "Category": "Bills", "Type": "Expense", "Amount": 299},
    {"Date": "2026-10-11", "Description": "Snacks", "Category": "Food", "Type": "Expense", "Amount": 180},
    {"Date": "2026-10-14", "Description": "Books", "Category": "Education", "Type": "Expense", "Amount": 750},
    {"Date": "2026-10-17", "Description": "Pocket money", "Category": "Income", "Type": "Income", "Amount": 3000},
    {"Date": "2026-10-19", "Description": "Movie", "Category": "Entertainment", "Type": "Expense", "Amount": 400},
]

df = pd.DataFrame(transactions)
df["Date"] = pd.to_datetime(df["Date"])

# ---------------- CALCULATIONS ----------------
total_income = df.loc[df["Type"] == "Income", "Amount"].sum()
total_expenses = df.loc[df["Type"] == "Expense", "Amount"].sum()
balance = total_income - total_expenses

savings_rate = (
    (balance / total_income) * 100
    if total_income > 0
    else 0
)

monthly_budget = 5000
budget_used = (total_expenses / monthly_budget) * 100
remaining_budget = monthly_budget - total_expenses

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💸 SpendWise")
    st.caption("Personal Finance Dashboard")
    st.divider()

    st.markdown("### Navigation")
    st.radio(
        "Choose a section",
        ["Overview", "Transactions", "Budgets", "Reports"],
        index=0,
        key="navigation",
    )

    st.divider()
    st.caption("STAGE 1 · DEMO DATA")
    st.caption("Your sample data resets when the app restarts.")


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>Good day 👋</h1>
    <p>Your money at a glance. Understand your spending, plan your budget,
    and make more informed financial decisions.</p>
</div>
""", unsafe_allow_html=True)

st.caption("OCTOBER 2026  ·  SAMPLE DASHBOARD")

# ---------------- SUMMARY CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Income</div>
        <div class="metric-value">₹{total_income:,.0f}</div>
        <div class="metric-note">Money received</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Expenses</div>
        <div class="metric-value">₹{total_expenses:,.0f}</div>
        <div class="metric-note">Money spent</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Current Balance</div>
        <div class="metric-value">₹{balance:,.0f}</div>
        <div class="metric-note">Income minus expenses</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Savings Rate</div>
        <div class="metric-value">{savings_rate:.1f}%</div>
        <div class="metric-note">Balance as % of income</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- BUDGET PROGRESS ----------------
st.markdown('<div class="section-heading">Monthly Budget</div>',
            unsafe_allow_html=True)

st.markdown('<div class="budget-card">', unsafe_allow_html=True)

budget_col1, budget_col2 = st.columns(2)

with budget_col1:
    st.markdown("**October spending limit**")
    st.caption(f"₹{total_expenses:,.0f} spent out of ₹{monthly_budget:,.0f}")

with budget_col2:
    st.markdown("**Remaining budget**")
    st.markdown(f"### ₹{remaining_budget:,.0f}")

# Streamlit progress bars must stay between 0 and 1.
progress = min(total_expenses / monthly_budget, 1.0)
st.progress(progress)

if total_expenses > monthly_budget:
    st.error("Budget exceeded! Review your spending.")
elif budget_used >= 80:
    st.warning("You have used at least 80% of your budget.")
else:
    st.success("Your spending is within the budget.")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- SPENDING CHART ----------------
st.markdown('<div class="section-heading">Where Your Money Goes</div>',
            unsafe_allow_html=True)

expenses_df = df[df["Type"] == "Expense"]

category_totals = (
    expenses_df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

chart_col, recent_col = st.columns([1.2, 1])

with chart_col:
    st.markdown("**Expenses by category**")
    st.bar_chart(category_totals)

with recent_col:
    st.markdown("**Recent transactions**")
    recent = df.sort_values("Date", ascending=False).head(5).copy()
    recent["Date"] = recent["Date"].dt.strftime("%d %b")
    recent["Amount"] = recent.apply(
        lambda row: (
            f"+₹{row['Amount']:,.0f}"
            if row["Type"] == "Income"
            else f"-₹{row['Amount']:,.0f}"
        ),
        axis=1
    )
    st.dataframe(
        recent[["Date", "Description", "Amount"]],
        hide_index=True,
        use_container_width=True
    )

st.divider()
st.caption("SpendWise · Stage 1 · Sample data for demonstration only")
