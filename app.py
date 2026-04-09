import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# page settings
st.set_page_config(page_title="Health Dashboard", layout="wide")

# ---------- DARK STYLE ----------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA FAST ----------
@st.cache_data
def load_data():
    df = pd.read_excel("healthcare_dataset.xlsx")

    # create age group
    bins = [0,30,60,100]
    labels = ["Young","Adult","Senior"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # create year column
    df["Year"] = pd.to_datetime(df["Date of Admission"]).dt.year

    return df

df = load_data()

# ---------- TITLE ----------
st.title("Health Data Trend Dashboard")

# ---------- DATA PREVIEW ----------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---------- KPI CARDS ----------
col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(df))
col2.metric("Average Bill", round(df["Billing Amount"].mean(),2))
col3.metric("Hospitals", df["Hospital"].nunique())

# ---------- ROW 1 ----------
col1, col2 = st.columns(2)

# Gender pie chart
with col1:
    st.subheader("Gender Distribution")

    fig1, ax1 = plt.subplots()

    df["Gender"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax1
    )

    ax1.set_ylabel("")
    st.pyplot(fig1)


# Age group bar chart
with col2:
    st.subheader("Age Group Distribution")

    fig2, ax2 = plt.subplots()

    df["Age Group"].value_counts().plot(
        kind="bar",
        ax=ax2
    )

    st.pyplot(fig2)

# ---------- ROW 2 ----------
col1, col2 = st.columns(2)

# medical condition distribution
with col1:
    st.subheader("Medical Condition Distribution")

    fig3, ax3 = plt.subplots()

    df["Medical Condition"].value_counts().plot(
        kind="bar",
        ax=ax3
    )

    st.pyplot(fig3)


# admission type distribution
with col2:
    st.subheader("Admission Type Distribution")

    fig4, ax4 = plt.subplots()

    df["Admission Type"].value_counts().plot(
        kind="bar",
        ax=ax4
    )

    st.pyplot(fig4)

# ---------- ROW 3 ----------
col1, col2 = st.columns(2)

# yearly trend
with col1:
    st.subheader("Yearly Billing Trend")

    yearly = df.groupby("Year")["Billing Amount"].mean()

    fig5, ax5 = plt.subplots()

    yearly.plot(
        marker="o",
        ax=ax5
    )

    st.pyplot(fig5)


# hospital comparison (TOP 10)
with col2:
    st.subheader("Top 10 Hospital Billing")

    top_hospitals = (
        df.groupby("Hospital")["Billing Amount"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    fig6, ax6 = plt.subplots()

    top_hospitals.sort_values().plot(
        kind="barh",
        ax=ax6
    )

    ax6.tick_params(labelsize=8)

    st.pyplot(fig6)


# ---------- ROW 4 ----------
col1, col2 = st.columns(2)

# average billing by condition
with col1:
    st.subheader("Average Billing by Condition")

    avg_bill = df.groupby("Medical Condition")["Billing Amount"].mean()

    fig7, ax7 = plt.subplots()

    avg_bill.plot(
        kind="bar",
        ax=ax7
    )

    st.pyplot(fig7)


# correlation heatmap
with col2:
    st.subheader("Correlation Heatmap")

    fig8, ax8 = plt.subplots()

    sns.heatmap(
        df[["Age","Billing Amount","Room Number"]].corr(),
        annot=True,
        ax=ax8
    )

    st.pyplot(fig8)


# ---------- DOWNLOAD BUTTON ----------
csv = df.to_csv(index=False).encode()

st.download_button(
    "Download Processed Data",
    csv,
    "health_report.csv",
    "text/csv"
)