
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import os

# Set page title
st.set_page_config(page_title="Synthetic Data Dashboard", layout="wide")

# File path (update as needed)
default_file = r"C:\Users\asus\Desktop\Masters Project & Thesis\Master Projects\Gen Ai Analytics\synthetic_customer_data.csv"

st.title("📊 Synthetic Customer Data Dashboard")
st.write("This dashboard visualizes GAN-generated synthetic customer data and allows you to download it.")

# Load dataset
if os.path.exists(default_file):
    df = pd.read_csv(default_file)
else:
    st.error("Synthetic dataset not found. Please upload a file below.")

# Upload option
uploaded_file = st.file_uploader("Upload a synthetic dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

if 'df' in locals():
    # Display dataset
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(10))

    # Summary stats
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # EDA Visuals
    st.subheader("📊 Exploratory Data Analysis")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    col1, col2 = st.columns(2)

    # Histogram
    with col1:
        st.write("### Distribution of First Numeric Column")
        if numeric_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[numeric_cols[0]], kde=True, ax=ax, color='blue')
            st.pyplot(fig)

    # Correlation Heatmap
    with col2:
        st.write("### Correlation Heatmap")
        if len(numeric_cols) > 1:
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    # Download button
    st.subheader("⬇ Download Synthetic Dataset")
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="synthetic_customer_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
