import streamlit as st
import pandas as pd



st.title("Reading a CSV file")

data = pd.read_csv("netflix_titles.csv")

st.write(data)
