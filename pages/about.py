import streamlit as st

import utils

student = utils.Student()

data = student.get_data_from_google_sheet()
st.dataframe(data)

st.title("About")
st.write("This is About Page")
