import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api key not found")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

#structed output
from pydantic import BaseModel

class Ticket(BaseModel):
    name : str
    email : str
    phone : int

schema=Ticket.model_json_schema()

responce_format={
    "type" : "json_object"
}


text = "hello my name is xyz ,my phone no is 8263 ,my email is abc@gmail.com ,address is at post xyz pune 421216"
sys_prompt = f"""
extract the user info from this and give me json
{text}
"""
prompt = "this is customer ticket please extract useful info"

sys_message ={
    "role":"system",
    "content":sys_prompt
}

message ={
    "role":role,
    "content":prompt
}

messages = [sys_message, message]

responce = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=responce_format
)
answer = responce.choices[0].message.content
print(answer)

# how to read answer

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)