import streamlit as st
import os
import time

path = "../metadata/qna/"

st.title("Questions and Answers")

while not os.path.exists(f"{path}question.txt"):
    time.sleep(1)

with open(f"{path}question.txt", "r") as file:
    questions = file.read()

while not os.path.exists(f"{path}answer.txt"):
    time.sleep(1)

with open(f'{path}answer.txt', "r") as file:
    answers = file.read()

st.text_area("Questions", value=questions, height=400)
st.text_area("Answer", value=answers, height=800)




