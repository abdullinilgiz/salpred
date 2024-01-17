import streamlit as st

from processing.feature import get_salary
from processing.feature import (
    LOCATION_INDEX, SCHEDULE_INDEX, EDUCATION_INDEX, EXP_INDEX)


LOCATIONS = LOCATION_INDEX.keys()
SCHEDULES = SCHEDULE_INDEX.keys()
EDUCATIONS = EDUCATION_INDEX.keys()
EXPERIENCES = EXP_INDEX.keys()


st.title("Cервис предсказания зарплат")

location = st.selectbox('Регион или город федерального значения', LOCATIONS)
position = st.text_input("Профессия")
education = st.radio('Образование', EDUCATIONS)
schedule = st.radio('Выберите график работы:', SCHEDULES)
experience = st.radio('Выберите опыт работы:', EXPERIENCES)


str_skills = st.text_input("Укажите ваши навыки через запятую", value='')
skills = str_skills.split(", ")


st.write(f'Выбраный регион -  :green[**{location}**]')
st.write(f'Ваша профессия - :red[**{position}**]')
st.write(f'Ваше образование - :blue[**{education}**]')
st.write(f'Вы выбрали - :blue[**{schedule}**]')
st.write(f'Ваш опыт - :blue[**{experience}**]')
st.write(f'Выбранные навыки - :blue[**{skills}**]')

button_pressed = st.button("Получить предсказание зарплаты")

if button_pressed:
    predicted_salary = get_salary(
        location,
        position,
        education,
        schedule,
        experience,
        skills,
        )

    st.write(f'Предлагаемая зарплата {int(round(predicted_salary, -3))}')
