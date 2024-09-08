import streamlit as st

home_page = st.Page(
    page="./pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
about_page = st.Page(
    page="./pages/about.py",
    title="About",
    icon=":material/info:",
)

results = st.Page(
    page="./pages/results.py",
    title="Results",
    icon=":material/bar_chart:",
)

stats_page = st.Page(
    page="./pages/stats.py",
    title="Stats",
    icon=":material/insert_chart:",
)

pg = st.navigation(pages=[home_page, about_page, results, stats_page])
pg.run()
