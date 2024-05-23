import streamlit as st
import pandas as pd
import numpy as np



st.title("Charting some data")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
st.line_chart(chart_data)
