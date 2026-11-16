import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api key not found....")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

message={
    "role" : "user",
    "content" : "write about streaming in breif"
}

meassages = [message]

steam = client.chat.completions.create(
    model=model , messages=meassages , stream=True
)

for chunk in steam:
    content = chunk.choices[0].delta.content
    if content:
        print(content ,end="", flush=True)