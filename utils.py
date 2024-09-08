import streamlit as st
from streamlit_gsheets import GSheetsConnection


class Student:
    def __init__(self):
        self.data = []

    def get_data_from_google_sheet(self):
        url = "https://docs.google.com/spreadsheets/d/1uhf3bRb628AfLz840pN7DmKEEkhGHhfRhy-U7Imlibk/edit?usp=sharing"
        conn = st.connection("gsheets", type=GSheetsConnection)
        self.data = conn.read(spreadsheet=url)
        # st.dataframe(data)
        return self.data


def main():
    st.title("Home")
    st.write("This is Home Page")


if __name__ == "__main__":
    main()
