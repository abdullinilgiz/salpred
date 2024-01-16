import streamlit as st

LOCATIONS = [
    'Москва',
    'Московская область',
    'Санкт-Петербург',
    'Ленинградская область',
    'Оренбургская область',
    'Саратов',
    'Тюмень',
    'Екатеринбург',
    'Воронеж',
    'Казань',
    'Краснодар',
]

SCHEDULES = [
    'полный рабочий день',
    'сменный график',
    'вахта',
    'свободный график',
    'частичная занятость',
]

EDUCATIONS = [
    'любое',
    'среднее профессиональное',
    'высшее',
    'среднее',
    'неполное высшее',
]

st.title("Демо-версия сервиса предсказания зарплат")

position = st.text_input("Профессия")
st.write(f'Ваша профессия - :red[**{position}**]')

education = st.radio('Образование', EDUCATIONS)

location = st.selectbox('Регион или город федерального значения', LOCATIONS)
st.write(f'Выбраный регион -  :green[**{location}**]')

schedule = st.radio('Выберите график работы:', SCHEDULES)
st.write(f'Вы выбрали - :blue[**{schedule}**]')

str_skills = st.text_input("Введите до 10 навыков, через запятую", value='')
skills = str_skills.split(", ")
st.write(f'Выбранные навыки - :blue[**{skills}**]')