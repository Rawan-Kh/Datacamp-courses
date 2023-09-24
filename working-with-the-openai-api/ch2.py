# Find and replace
# Set your API key
openai.api_key = "____"

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
   model="gpt-3.5-turbo-instruct",
   prompt=prompt,
   max_tokens=100
)

# Extract and print the response text
print(response)

-----------
# Text summarization
# Set your API key
openai.api_key = "____"

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
   model="gpt-3.5-turbo-instruct",
   prompt=prompt,
   max_tokens=400
)

print(response["choices"][0]["text"])
---------------
# Content generation
# Set your API key
openai.api_key = "____"

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens= 100
)

print(response["choices"][0]["text"])

------------

# Classifying text sentiment
# Set your API key
openai.api_key = "____"

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=100
)

print(response['choices'][0]['text'])
--------------
# Categorizing companies
# Set your API key
openai.api_key = "____"

# Create a request to the Completion endpoint
response = openai.____.____(
  model="gpt-3.5-turbo-instruct",
  prompt=____,
  max_tokens=100,
  temperature=0.5
)

print(response['choices'][0]['text'])

----------
# The Chat Completion endpoint
# Set your API key
openai.api_key = "<OPENAI_API_TOKEN>"

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system",
     "content": "You are a helpful data science tutor."},
    {"role": "user",
     "content": "What is the difference between a for loop and a while loop?"}
  ]
)

# Extract the assistant's text response
print(response['choices'][0]['message']['content'])

-------------
# Code explanation
# Set your API key
openai.api_key = "<OPENAI_API_TOKEN>"

instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful Python programming assistant."},
    {"role": "user", "content": instruction}
  ],
  max_tokens=100
)

print(response['choices'][0]['message']['content'])

-------------
# Set your API key
openai.api_key = "<OPENAI_API_TOKEN>"

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   # Add a user and assistant message for in-context learning
   messages=[
     {"role": "system", "content": "You are a helpful Python programming tutor."},
     {"role": "user", "content": "Explain what the min() function does."},
     {"role": "assistant", "content": "The min() function returns the smallest item from an iterable."},
     {"role": "user", "content": "Explain what the type() function does."}
   ]
)

print(response['choices'][0]['message']['content'])

-----------
# Set your API key
openai.api_key = "<OPENAI_API_TOKEN>"

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100
    )
    
    # Convert the assistant's message to a dict and append to messages
    assistant_dict = dict(response["choices"][0]["message"])
    messages.append(assistant_dict)
    print("Assistant: ", response["choices"][0]["message"]["content"], "\n")

------------
