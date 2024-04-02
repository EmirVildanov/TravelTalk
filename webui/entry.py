import streamlit as st
from st_pages import Page, show_pages

from constants import *
from streamlit import switch_page

show_pages(
    [
        Page(PAGE_MAIN, "Главная", "🏠"),
        Page(PAGE_EXISTING_TRIPS, "Найти собеседника", "🙏"),
        Page(PAGE_CREATE_NEW_TRIP, "Создать поездку", "🌏"),
    ]
)

title_alignment="""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.title(APP_NAME)
st.header(APP_SLOGAN)
st.markdown("Добро пожаловать в мир новых знакомств и незабываемых приключений!"
            "Наша платформа предназначена для тех, кто любит путешествовать и ищет новых друзей на своем пути."
            "Мы знаем, как трудно найти единомышленников в большом мире, поэтому создали приложение, которое поможет вам встретить интересных людей,"
            "готовых поделиться своими историями и открыть новые горизонты.")
st.image("PeopleTalkingInTrain.webp")

col1, col2 = st.columns(2)
with col1:
    if st.button(label="Создать поездку"):
        switch_page(PAGE_CREATE_NEW_TRIP)
with col2:
    if st.button(label="Найти собеседника"):
        switch_page(PAGE_EXISTING_TRIPS)
