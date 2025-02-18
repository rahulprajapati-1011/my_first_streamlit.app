import streamlit as st
import pandas as pd
df = pd.read_csv('Automobile.csv')
st.dataframe(df)
# bar = plt.bar(x=df['company'])
st.bar_chart(df)