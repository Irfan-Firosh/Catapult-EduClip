import pathlib
import textwrap

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
def similar_request(subject):
    request_text = f'''For the following inputs, a small sentence or fragment, can you generate similar sentences or keywords from it? Can you give responses that are very closely related to the given prompt? For example, for the given prompt "What is remainder theorem", the given outputs from you would be:
- "Using modulo arithmetic to find remainders."
- "Applying the concept of modulo to determine residues."
- "Understanding modular arithmetic and its relationship to remainders."
- "Employing modular arithmetic for remainder calculations."
- "Utilizing modular arithmetic to solve remainder problems."
- "Finding residues using modular arithmetic."
- "Exploring modular arithmetic in the context of the remainder theorem."
- "Applying modular arithmetic principles to polynomial remainders."
- "Using modulo operations to determine remainders efficiently."
- "Employing modular arithmetic techniques for remainder theorem applications." The input is {subject}
'''
    response = model.generate_content(request_text)
    return response.text.split('\n')
print(similar_request("what is an integral"))