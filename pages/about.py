import streamlit as st

import utils

student = utils.Student()
st.title("Display The Results")
st.write("This is About Page")
student.get_all_student_data()
data = student.get_data_from_google_sheet()
student.get_groups()
for row in student.data.values:

    st.write(row)

st.dataframe(student.blue_group)
