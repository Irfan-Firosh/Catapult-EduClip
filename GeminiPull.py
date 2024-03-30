import pathlib
import textwrap
import json
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import config

path = "metadata/qna/"
GOOGLE_API_KEY = config.GOOGLE_API_KEY 

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
def user_request(subject):
    question_text = f"Generate questions for {subject} do NOT give the answers"
    question = model.generate_content(question_text)
    #print("Res"ponse content:", response.text)
    with open(f"{path}question.txt", "w") as file:
        file.write(question.text)
   
    answer = model.generate_content(question.text)
    with open(f"{path}answer.txt", "w") as file:
        file.write(answer.text)
    
