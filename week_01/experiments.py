from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# creating client
client = OpenAI()  # it will automatically read the api key from env

# creating function to observe tokens
def ask(message , max_tokens = 300):
    
    # now creting response object
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=max_tokens,
        messages=message
    )
    
    # printing input and output tokens
    print(f"Input tokens: {response.usage.prompt_tokens}")
    print(f"Output tokens: {response.usage.completion_tokens}")
    
    reply = response.choices[0].message.content
    return reply

""" 
experiment 02: max token is hard cut off and difference in input and output tokens
"""
# ask([{"role": "user", "content": "Hi"}])
# ask([{"role": "user", "content": "Write a short paragraph about why sleep is important for students."}],max_tokens=20)


""" 
Experiment: 03
asking again and again gives different responses
"""
# for i in range(3):
#     result = ask([{"role": "user", "content": "Write a short paragraph about why sleep is important for students."}],max_tokens=20)
#     print(f"result number: {i + 1}: {result}")


""" 
Experiment: 04
No history the model only remembers you give it , so in order to retain memory you have to store and send it with
every api call
"""

# r1 = ask([{"role": "user", "content": "My name is Riyan."}])
# print(r1)
# r1 = ask([{"role": "user", "content": "What is my name?"}])
# print(r1)

# history = [
#     {"role": "user", "content": "My name is Riyan."},
#     {"role": "assistant", "content": "Nice to meet you, Riyan!"},
#     {"role": "user", "content": "What is my name?"},
# ]

# history = [
#     {"role": "user", "content": "My name is Riyan."},
#     {"role": "assistant", "content": "Nice to meet you, Riyan!"},
#     {"role": "user", "content": "What is my name?"},
# ]

# r1 = ask(history)
# print(r1)


""" 
Experiment: 05
The cost increases as the history increases because the input tokens size increases
that is the reason why my claude limit is reached quickly in a long conversation chat

"""

# history = []
# for text in ["Tell me a fact about space.", "Another one.", "Another one."]:
#     history.append({"role": "user", "content": text})
#     reply = ask(history, max_tokens=100)
#     history.append({"role": "assistant", "content": reply})