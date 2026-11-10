import streamlit as st

title = st.sidebar.text_input("Enter a suitable title :")
text = st.sidebar.text_area("Enter a suitable text :")

st.title(f"{title}")
st.write(f"{text}")

option = st.radio("Select a suitable option :", ("Option 1", "Option 2", "Option 3"))

st.header(f":red[you picked] :green[{option}]")