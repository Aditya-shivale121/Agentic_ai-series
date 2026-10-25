import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Please enter correct api key")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Do you know Aditya Shivale"

message={
    "role" :role,
    "content" :prompt
}

messages = [message]

responce =client.chat.completions.create(
    model = model ,
    messages = messages)
print(responce)

print("*************************************************")

print(responce.choices[0].message.content)
