import streamlit as st
from streamlit_gsheets import GSheetsConnection


class Student:
    def __init__(self):
        self.data = []
        self.yellow_group = []
        self.green_group = []
        self.blue_group = []
        self.red_group = []
        self.brown_group = []
        self.white_group = []

    def get_data_from_google_sheet(self):
        url = "https://docs.google.com/spreadsheets/d/1uhf3bRb628AfLz840pN7DmKEEkhGHhfRhy-U7Imlibk/edit?usp=sharing"
        conn = st.connection("gsheets", type=GSheetsConnection)
        self.data = conn.read(spreadsheet=url)
        # st.dataframe(data)
        # print(type(self.data))
        return self.data

    def get_groups(self):
        if self.data:
            # dividing pandas dataframe into groups using group names in the column names group
            grouped_df = self.data.groupby("Group")
            self.green_group = grouped_df.get_group("Green")
            self.blue_group = grouped_df.get_group("Blue")
            self.red_group = grouped_df.get_group("Red")
            self.yellow_group = grouped_df.get_group("Yellow")
            self.brown_group = grouped_df.get_group("Brown")
            self.white_group = grouped_df.get_group("White")
        else:
            st.error("Data not found")


def main():
    st.title("Home")
    st.write("This is Home Page")


if __name__ == "__main__":
    main()
