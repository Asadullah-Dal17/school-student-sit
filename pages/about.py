import streamlit as st

import utils

student = utils.Student()

data = student.get_data_from_google_sheet()
student.get_groups()
st.dataframe(student.blue_group)
# st.dataframe(data)


st.title("About")
st.write("This is About Page")
