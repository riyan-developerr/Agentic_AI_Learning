from dotenv import load_dotenv,find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())                  # loads the key from .env
client = OpenAI()              # reads OPENAI_API_KEY automatically
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))   # alternative

MODEL = "gpt-4o-mini"          # change this to a current cheap model from your OpenAI dashboard

response = client.chat.completions.create(
    model=MODEL,
    max_tokens=300,
    messages=[
        {"role": "user", "content": "What is my name?."}
    ],
)

print(response.choices[0].message.content)
print("Input tokens:", response.usage.prompt_tokens)
print("Output tokens:", response.usage.completion_tokens)

# print(response)

""" 
Notes: 
property: it is a function but accessed as a variable (no paranthesis) part of an object
e.g: math.pi

"""