import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("INCOREECT API KEY")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

def llm_ans(prompt):
    message={
        "role":role,
        "content": prompt
    }

    messages = [message]

    responce = client.chat.completions.create(
        model=model,
        messages=messages
    )

    ans = responce.choices[0].message.content
    return ans


bad_prompt = """
# role
you are a expert a support assistant in mobile/laptop company
# task
you have to classfy issue in category
# constrant
you have to classfy issue in one of three category return ,billing ,technical
# output format
the output should be only one word in above category
# one shot
for instance user says my mobile is not working i need refund then category shoud refund
# fallback
if the issue is other than this then answer fuck you ask related queery!............

This is user complant:
 does she loves me
"""

print(llm_ans(bad_prompt))