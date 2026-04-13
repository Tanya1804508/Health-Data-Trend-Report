import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

h1 {
    text-align:center;
    color:#00BFFF;
}

[data-testid="metric-container"] {
    background-color:#111;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 0px 10px rgba(0,191,255,0.3);
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():

    df = pd.read_excel("healthcare_dataset.xlsx")

    bins = [0,30,60,100]
    labels = ["Young","Adult","Senior"]

    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

    df["Year"] = pd.to_datetime(df["Date of Admission"]).dt.year

    return df

df = load_data()

# ---------- TITLE ----------
st.markdown("<h1>Healthcare Data Dashboard</h1>", unsafe_allow_html=True)

# ---------- KPI ----------
col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Patients", len(df))
col2.metric("Average Age", round(df["Age"].mean(),1))
col3.metric("Average Billing", round(df["Billing Amount"].mean(),0))
col4.metric("Hospitals", df["Hospital"].nunique())

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs([
    "Overview",
    "Medical Analysis",
    "Financial Insights"
])

# ================= TAB 1 =================
with tab1:

    c1,c2 = st.columns(2)

    # gender pie
    with c1:

        fig = px.pie(
            df,
            names="Gender",
            title="Gender Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)


    # age histogram
    with c2:

        fig = px.histogram(
            df,
            x="Age",
            nbins=20,
            title="Age Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)


    c3,c4 = st.columns(2)

    # age group bar
    with c3:

        age_counts = df["Age Group"].value_counts().reset_index()

        age_counts.columns = ["Age Group","Count"]

        fig = px.bar(
            age_counts,
            x="Age Group",
            y="Count",
            title="Age Group Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)


    # admission type pie
    with c4:

        fig = px.pie(
            df,
            names="Admission Type",
            title="Admission Type"
        )

        st.plotly_chart(fig, use_container_width=True)


# ================= TAB 2 =================
with tab2:

    c1,c2 = st.columns(2)

    # medical condition frequency
    with c1:

        condition_counts = df["Medical Condition"].value_counts().reset_index()

        condition_counts.columns = ["Medical Condition","Count"]

        fig = px.bar(
            condition_counts,
            x="Medical Condition",
            y="Count",
            title="Medical Condition Frequency"
        )

        st.plotly_chart(fig, use_container_width=True)


    # billing vs condition
    with c2:

        fig = px.box(
            df,
            x="Medical Condition",
            y="Billing Amount",
            title="Billing Distribution by Condition"
        )

        st.plotly_chart(fig, use_container_width=True)


    # correlation heatmap
    corr = df[["Age","Billing Amount","Room Number"]].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)


# ================= TAB 3 =================
with tab3:

    c1,c2 = st.columns(2)

    # yearly trend
    with c1:

        yearly = df.groupby("Year")["Billing Amount"].mean().reset_index()

        fig = px.line(
            yearly,
            x="Year",
            y="Billing Amount",
            markers=True,
            title="Yearly Billing Trend"
        )

        st.plotly_chart(fig, use_container_width=True)


    # top hospitals
    with c2:

        hospital = (
            df.groupby("Hospital")["Billing Amount"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            hospital,
            x="Billing Amount",
            y="Hospital",
            orientation="h",
            title="Top 10 Hospital Billing"
        )

        st.plotly_chart(fig, use_container_width=True)


    # billing histogram
    fig = px.histogram(
        df,
        x="Billing Amount",
        nbins=30,
        title="Billing Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------- TABLE ----------
st.subheader("Dataset Preview")

st.dataframe(df.head(50))
