
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

prompt1 = "hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write an essay on ML in 1000 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=50
    )

    usage = response.usage

    print(f"\nPrompt: {prompt}")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Completion tokens: {usage.completion_tokens}")
    print(f"Total tokens: {usage.total_tokens}")
    print(f"Response: {response.choices[0].message.content}")
    print(f"Finish reason: {response.choices[0].finish_reason}")

