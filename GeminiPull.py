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

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
def user_request(subject):
    question_text = f"Generate questions for {subject} do NOT give the answers, NO SPACE BETWEEN EACH QUESTION do NOT GENERATE LATEX NO TITLE JUST QUESTIONS. "
    question = model.generate_content(question_text)
    with open(f"{path}question.txt", "w") as file:
        file.write(question.text)
   
    answer = model.generate_content(f'{question.text} NO LINE BETWEEN EACH ANSWER and NOT IN LATEX no title')
    with open(f"{path}answer.txt", "w") as file:
        file.write(answer.text)

    # Return the path to the created .txt file
def generate(prompt):
    response = user_request("Give me one eigen vector problem")

generate("Eigen Values")
# Replace 'YOUR_APP_ID' with your actual Wolfram Alpha AppID

# Write the content to a file or display the image
#with open("wolfram_result.png", "wb") as f:
    #f.write(image_content)
