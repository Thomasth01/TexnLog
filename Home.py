import streamlit as st
import pandas as pd

st.title("Upload file")
st.write("The dataset should be a csv or xlsx file.")

file = st.file_uploader("Upload file", type=["csv", "xlsx"])

if st.button("Reset"):
    if "df" in st.session_state:
        del st.session_state.df

if file is not None:
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(file)

if "df" in st.session_state:
    non_numeric = st.session_state.df.select_dtypes(exclude=['number']).columns
    if non_numeric.size > 0:
        st.session_state.df.drop(non_numeric, axis=1, inplace=True)
        st.info("Non-numeric columns have been removed.")
    st.dataframe(st.session_state.df)