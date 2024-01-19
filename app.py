import streamlit as st

from processing.feature import (print_column_coef, get_model,
                                preprocess_features, get_salary)
from processing.feature import (
    LOCATION_INDEX, SCHEDULE_INDEX, EDUCATION_INDEX, EXP_INDEX)
from processing.graphs import get_percentage_graph


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
model = get_model()

if button_pressed:
    vacancies = preprocess_features(
        location,
        position,
        education,
        schedule,
        experience,
        skills,
        )
    predicted_salaries = get_salary(model, vacancies)

    st.write(f'Предлагаемая зарплата {int(round(predicted_salaries[0], -3))}')

    percentage_graph = get_percentage_graph(vacancies, model)
    st.pyplot(percentage_graph)
