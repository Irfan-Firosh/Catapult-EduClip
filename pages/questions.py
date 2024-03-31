import streamlit as st
import os
import time
from GeminiPull import *


path = "../metadata/qna/"

def clear_downloads():
    for file in os.listdir(path):
        path = os.path.join(path, file)
        os.remove(path)


with st.spinner("Generating Question..."):
    clear_downloads()
    while not os.path.exists(f"{path}question.txt"):
        time.sleep(1)
    while not os.path.exists(f"{path}answer.txt"):
        time.sleep(1)

st.title("Questions and Answers")
with open(f"{path}question.txt", "r") as file:
    questions = file.read()

with open(f'{path}answer.txt', "r") as file:
    answers = file.read()

st.text_area("Questions", value=questions, height=400)
st.text_area("Answer", value=answers, height=800)




