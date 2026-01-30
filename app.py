import streamlit as st
import pandas as pd

df = pd.read_csv("cleaned_nassau.csv")
routes = pd.read_csv("route_state_kpis.csv")

st.title("Nassau Candy Shipping Intelligence")

region = st.selectbox("Select Region", df['Region'].unique())

filtered = df[df['Region']==region]

st.metric("Avg Lead Time", round(filtered['Lead_time'].mean(),2))
st.metric("Total Shipments", len(filtered))

st.bar_chart(filtered.groupby('State/Province')['Lead_time'].mean())
