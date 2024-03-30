import streamlit as st

path = "metadata/qna/"

st.title("Questions and Answers")


with open(f"{path}question.txt", "r") as file:
    questions = file.read()

with open(f'{path}answer.txt', "r") as file:
    answers = file.read()

st.text_area("Questions", value=questions, height=400)
st.text_area("Answer", value=answers, height=800)



