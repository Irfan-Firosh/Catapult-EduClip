import pathlib
import textwrap
import json
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import config

GOOGLE_API_KEY = config.GOOGLE_API_KEY 

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
def user_request(subject):
    question_text = f"Generate questions for {subject} do NOT give the answers"
    question = model.generate_content(question_text)
    #print("Response content:", response.text)
    with open("question.txt", "w") as file:
        file.write(question.text)
   
    answer = model.generate_content(question.text)
    with open("answer.txt", "w") as file:
        file.write(answer.text)

    # Return the path to the created .txt file
  
  


WOLFRAM_ALPHA_API = 'X4LJTG-5HGW5E29XA'
import requests




def execute_query(input_query, app_id):
    base_url = "http://api.wolframalpha.com/v1/simple"
    params = {
        "appid": app_id,
        "i": input_query
    }
    response = requests.get(base_url, params=params)
    return response.content
response = user_request("Give me one eigen vector problem")
print(response)
# Replace 'YOUR_APP_ID' with your actual Wolfram Alpha AppID

# Write the content to a file or display the image
#with open("wolfram_result.png", "wb") as f:
    #f.write(image_content)
