import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#st.title('Ramniranjan jhunjhunwala college')
st.set_page_config(
    page_title='multipage app'
)
st.header('Srinivasa Ramanujan', divider=True)
col1, col2 = st.columns(2)
with st.sidebar:
    st.link_button('Know more','https://en.wikipedia.org/wiki/Srinivasa_Ramanujan')

with col1:
    st.image('download.webp')
with col2:
    st.text('Srinivasa Ramanujan Aiyangar[a] (22 December 1887 – 26 April 1920) was an Indian mathematician. Often regarded as one of the greatest mathematicians of all time, though he had almost no formal training in pure mathematics, he made substantial contributions to mathematical analysis, number theory, infinite series, and continued fractions, including solutions to mathematical problems then considered unsolvable.')

st.divider()



