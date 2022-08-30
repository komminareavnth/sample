import streamlit as st
st.title("MY FIRST APP")
import pandas as pd
data=pd.read_csv('usedcarprice.csv')
st.dataframes(data)
