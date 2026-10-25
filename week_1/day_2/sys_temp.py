import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY NOT FOUND")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "suggest me a food delivery app name"

message_sys={
    "role": "system",
    "content": "you are professional social media manager"
}

message={
    "role":role,
    "content":prompt
}

messages=[message_sys,message]

responce = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)

print("#############################################################")
    
print(responce.choices[0].message.content)