import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)
conversation_history = []

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})
    
    # Make the API call with the updated conversation history
    response = client.chat.completions.create(
        model=model,
        messages=conversation_history
    )
    
    # Extract the assistant's message and add it to the conversation history
    assistant_message = response.choices[0].message['content']
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message


while True:

    print('Type "exit" to end the conversation')
    user_input = input("You: ")

    if user_input == 'exit':
        print("Ending conversation. Goodbye!")
        break

    assistant_response = chat_with_gpt(user_input)
    print(f"Assistant: {assistant_response}\n")