import numpy as np
import pandas as pd
import streamlit as st

st.header('Select box')

sb = st.selectbox('Which color is your favourite ?', [
  'Blue', 'Yellow', 'Green'
])

st.write('Your favourite color is', sb.lower() + '.')