import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
data = pd.read_csv("data/superstore.csv")

st.title("📊 Sales Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
regions = st.sidebar.multiselect("Select Region(s):", data["Region"].unique(), default=data["Region"].unique())
categories = st.sidebar.multiselect("Select Category:", data["Category"].unique(), default=data["Category"].unique())

# Filter data
filtered_data = data[(data["Region"].isin(regions)) & (data["Category"].isin(categories))]

# KPIs
total_sales = filtered_data["Sales"].sum()
total_profit = filtered_data["Profit"].sum()
avg_discount = filtered_data["Discount"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Avg. Discount", f"{avg_discount:.2%}")

# Charts
st.markdown("### Sales by Region")
fig, ax = plt.subplots()
sns.barplot(x="Region", y="Sales", data=filtered_data, estimator=sum, ci=None, palette="viridis", ax=ax)
st.pyplot(fig)

st.markdown("### Profit by Category")
fig2, ax2 = plt.subplots()
sns.barplot(x="Category", y="Profit", data=filtered_data, estimator=sum, ci=None, palette="pastel", ax=ax2)
st.pyplot(fig2)

st.markdown("### Discount vs Profit")
fig3, ax3 = plt.subplots()
sns.scatterplot(x="Discount", y="Profit", data=filtered_data, alpha=0.6, ax=ax3)
st.pyplot(fig3)

st.caption("Data Source: Kaggle Sample Superstore | Built by Gafoor Ahmed Shaik")
