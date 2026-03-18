import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Customer Segmentation")

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/telco_churn.csv")  # update path if needed
    return df

df = load_data()

# -------------------- PREPROCESSING --------------------
df_clean = df.copy()

# Convert TotalCharges to numeric
df_clean["TotalCharges"] = pd.to_numeric(df_clean["TotalCharges"], errors="coerce")
df_clean.dropna(inplace=True)

# Encode categorical features
df_encoded = pd.get_dummies(df_clean, drop_first=True)

# -------------------- FEATURE SELECTION --------------------
features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X = df_encoded[features]

# -------------------- SCALING --------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Segmentation Settings")

k = st.sidebar.slider("Select Number of Clusters (K)", 2, 10, 3)

# -------------------- KMEANS --------------------
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df_clean["Cluster"] = clusters

# -------------------- PCA FOR VISUALIZATION --------------------
pca = PCA(n_components=2)
pca_components = pca.fit_transform(X_scaled)

df_clean["PCA1"] = pca_components[:, 0]
df_clean["PCA2"] = pca_components[:, 1]

# -------------------- VISUALIZATION --------------------
st.subheader("📊 Customer Segments Visualization")

fig = px.scatter(
    df_clean,
    x="PCA1",
    y="PCA2",
    color=df_clean["Cluster"].astype(str),
    title="Customer Segments (PCA Projection)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CLUSTER SUMMARY --------------------
st.subheader("📋 Cluster Summary")

cluster_summary = df_clean.groupby("Cluster")[features].mean().round(2)
st.dataframe(cluster_summary, use_container_width=True)

# -------------------- CLUSTER INSIGHTS --------------------
st.subheader("🔍 Cluster Insights")

selected_cluster = st.selectbox(
    "Select Cluster to Explore",
    sorted(df_clean["Cluster"].unique())
)

cluster_data = df_clean[df_clean["Cluster"] == selected_cluster]

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(cluster_data))
col2.metric("Avg Monthly Charges", round(cluster_data["MonthlyCharges"].mean(), 2))
col3.metric("Avg Tenure", round(cluster_data["tenure"].mean(), 1))

# -------------------- INTERPRETATION --------------------
st.markdown("### 💡 Segment Interpretation")

if selected_cluster == 0:
    st.info("🟢 This segment may represent **low-value or new customers**.")
elif selected_cluster == 1:
    st.warning("🟡 This segment may represent **moderate engagement customers**.")
else:
    st.error("🔴 This segment may represent **high-risk or high-value customers**.")

# -------------------- DISTRIBUTION --------------------
st.subheader("📈 Feature Distribution in Selected Cluster")

fig2 = px.histogram(
    cluster_data,
    x="MonthlyCharges",
    nbins=30,
    title="Monthly Charges Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------- SIDEBAR INFO --------------------
st.sidebar.info("""
🧠 This module segments customers using K-Means clustering.

- Helps identify customer groups
- Supports targeted marketing
- Improves retention strategies
""")