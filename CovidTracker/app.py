import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CovidTracker", layout="centered")

st.title("🦠 CovidTracker")
st.subheader("Visualize COVID-19 Case Trends by Country")

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])
    return df

df = load_data()

# Country selection
countries = df["Country"].unique().tolist()
country = st.selectbox("Select Country", countries)

# Filter by country
filtered = df[df["Country"] == country]

# Display stats
st.metric("Latest Confirmed", int(filtered["Confirmed"].iloc[-1]))
st.metric("Latest Deaths", int(filtered["Deaths"].iloc[-1]))
st.metric("Latest Recovered", int(filtered["Recovered"].iloc[-1]))

# Line chart
st.line_chart(filtered.set_index("Date")[["Confirmed", "Deaths", "Recovered"]])

st.markdown("📊 Data is sample. Replace with real-time dataset for accuracy.")
