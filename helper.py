#import langchain
from openai import OpenAI
import os
from dotenv import load_dotenv

#ask for user input from command line
request = input("Write your request:")

#read test app 
with open("app.py", 'r') as file:
    code = file.read()
    
#import system prompt
# Get the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the text file
file_path = os.path.join(script_dir, "HelperFiles", "helper_prompt.txt")

# Read the text file
with open(file_path, 'r') as file:
    system_prompt = file.read()

# Load dotenv
load_dotenv()


openai_key = os.getenv("OPENAI_API_KEY")

request_with_info = f"{request} {code}"

client = OpenAI(
    api_key = openai_key,
    )
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": request_with_info},
  ]
)
output = completion.choices[0].message.content

print(output)
# Open the file in write mode.
with open('test_app.py', 'w') as f:
  # Write the data to the file.
  f.write(output)
# Close the file.
f.close()
