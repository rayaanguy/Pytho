import streamlit as st
import pandas as pd 

st.title("my web app ")
st.write("welcome to my web app currently learning about data frames ")
df=pd.DataFrame({
    'table':[1,2,3,4]
    ,'second column': [10, 20, 30, 40]
})
st.write(df)
count=0
if st.button('click me'):
    count+=1
    print(f"the button has been clicked {count} times")
