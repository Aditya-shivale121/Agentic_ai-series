import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Invalid Api Key")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"


JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""
RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt ,user_prompt):
    sys_msg={
        "role" : "system",
        "content" : system_prompt
    }
    user_msg={
        "role" : "user",
        "content" : user_prompt
    }

    messages = [sys_msg, user_msg]

    responce = client.chat.completions.create(
        model=model,
        messages=messages

    )

    answer = responce.choices[0].message.content
    return answer


def step1_res_extract():
    sys_prompt = f"""
    you are a professional HR assistant . Your work is to extract skills from the resume.
    do not invent anythig by your self and dont return anything other than skills.
    output format:
    seperate skills by comma
"""

    user_prompt = f"""
    extract the skills from this resume
    {RESUME}
"""
    return ask_llm(sys_prompt ,user_prompt)
    
def step2_jd_extract():
    sys_prompt = f"""
    you are a professional HR assistant . Your work is to extract skills from the JD.
    do not invent anythig by your self and dont return anything other than skills.
    output format:
    seperate skills by comma
"""

    user_prompt = f"""
    extract the skills from this jd
    {JD}
"""
    return ask_llm(sys_prompt ,user_prompt)

def step3_compare(skills ,jd):
    sys_prompt = f"""
    you are a professional HR assistant . Your work is to compare the skills and jd.
    based on that give rating to candidate between 1 - 100.
    also tell his is good fit or not .dont give anything other bluff
    
"""

    user_prompt = f"""
    compare and match the skills and jd
    JD:{jd}
    skill:{skills}
"""
    return ask_llm(sys_prompt ,user_prompt)

skills = step1_res_extract()
print(skills)
sleep(2)
jd = step2_jd_extract()
print(jd)
sleep(2)
score = step3_compare(skills,jd)
print(score)


