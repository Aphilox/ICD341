import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Maize Production Dashboard",
    page_icon="🌽",
    layout="wide"
)

st.title("🌽 Maize Production Dashboard")
st.write(
    "This interactive dashboard demonstrates reproducible statistical computing "
    "using Streamlit, NumPy, pandas, and Matplotlib."
)

# -------------------------------------------------
# Sidebar controls
# -------------------------------------------------
st.sidebar.header("Simulation Settings")

seed = st.sidebar.number_input(
    "Random seed",
    min_value=1,
    max_value=10000,
    value=123,
    step=1
)

n = st.sidebar.slider(
    "Number of observations",
    min_value=20,
    max_value=500,
    value=100,
    step=10
)

mean = st.sidebar.number_input(
    "Mean production (tonnes)",
    min_value=0.0,
    max_value=20.0,
    value=5.0,
    step=0.1
)

sd = st.sidebar.number_input(
    "Standard deviation (tonnes)",
    min_value=0.1,
    max_value=5.0,
    value=1.2,
    step=0.1
)

# -------------------------------------------------
# Reproducible data generation
# -------------------------------------------------
@st.cache_data
def generate_data(seed, n, mean, sd):
    rng = np.random.default_rng(seed)
    production = rng.normal(loc=mean, scale=sd, size=n)
    return pd.DataFrame({"Maize_Production": production})

df = generate_data(seed, n, mean, sd)

# -------------------------------------------------
# Summary metrics
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Observations", len(df))
col2.metric("Mean", f"{df['Maize_Production'].mean():.2f} tonnes")
col3.metric("Std. deviation", f"{df['Maize_Production'].std():.2f} tonnes")
col4.metric("Maximum", f"{df['Maize_Production'].max():.2f} tonnes")

# -------------------------------------------------
# Histogram
# -------------------------------------------------
st.subheader("Distribution of Maize Production")

fig, ax = plt.subplots()
ax.hist(df["Maize_Production"], bins=20, edgecolor="black")
ax.set_xlabel("Production (tonnes)")
ax.set_ylabel("Frequency")
ax.set_title("Maize Production Distribution")
st.pyplot(fig)

# -------------------------------------------------
# Data table
# -------------------------------------------------
st.subheader("Generated Data")
st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# Download button
# -------------------------------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="maize_production_dashboard.csv",
    mime="text/csv"
)

# -------------------------------------------------
# Interpretation
# -------------------------------------------------
st.subheader("Interpretation")
st.write(
    f"The simulated mean maize production is approximately "
    f"{df['Maize_Production'].mean():.2f} tonnes. "
    f"The standard deviation is approximately "
    f"{df['Maize_Production'].std():.2f} tonnes. "
    "Changing the sidebar controls updates the simulation, but using the same seed "
    "reproduces the same data."
)