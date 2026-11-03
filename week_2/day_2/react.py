import os
from pathlib import Path
from groq import Groq
from time import sleep
from dotenv import load_dotenv
import re

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Incoreect api key")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

def get_prod_price(product):
    if product == 'iphone 17':
        return 1000
    if product == 'iphone 15':
        return 500
    else:
        return 0  

def calculator(expressino):
    try:
      return eval(expressino)
    except:
       return "calculation error"

tools = {
    "get_prod_price":get_prod_price,
    "calculator": calculator
}        

system_prompt = """
you are a shopping assistant.

you have these tools:

get_prod_price(product)
calculator(expression)

IMPORTANT:
call tools exactly like these examples:

Action: get_prod_price(product)
Action: calculator("5000 - 1000")

Never Write:
calculator(expression='5000 - 1000')

Follow these rules:

1. Decide what you have to do next.
2. call only one tool at a time.
3. after writing an action , stop immedily.
4. Never guess or invent a tool result.
5. Wait until you receive an Observation.
6. Then decide your next action.
7. When the task is complete, give the Final Answer.

Format:

Thought: what you need to do
Action: tool_name(argument)

When finished:

Final Answer: your answer
"""

def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Agent has finished
        if "Final Answer:" in answer:
            break


        # Find the Action
        match = re.search(
           r'Action:\s*(\w+)\((.*?)\)',
           answer
)

        if match:

            tool_name = match.group(1)

            tool_input = match.group(2)

            tool_input = tool_input.strip()

            tool_input = tool_input.strip('"')


            # Run the tool
            if tool_name in tools:

                tool = tools[tool_name]

                observation = tool(tool_input)

            else:

                observation = "Tool not found"


            print(
                "Observation:",
                observation
            )


            # Add LLM response to memory
            messages.append({
                "role": "assistant",
                "content": answer
            })


            # Give tool result back to LLM
            messages.append({
                "role": "user",
                "content":
                    "Observation: "
                    + str(observation)
            })
            sleep(5)



prompt="""
I have 5000 rupees. What is the price of an iphone 17?
and how much money will I have left?
"""
run_agent(prompt)