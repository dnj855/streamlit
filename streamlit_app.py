import streamlit as st

st.header('st.button')

if st.button('*say hello*', help="Click me!"):
  st.write('Why hello?')
else:
  st.write('Goodbye!')