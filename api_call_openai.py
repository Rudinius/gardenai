import os
import openai
from openai import OpenAI

# Get API key from environment variables
API_KEY = os.environ.get('STUDYAI_API_KEY', "If ENVVAR not set, paste API key here")
client = OpenAI(api_key=API_KEY)

def get_completion_from_messages(chat_history, model="gpt-3.5-turbo"):

    try:
        response = client.chat.completions.create(
            messages=chat_history,
            model=model,
            temperature=0.2
        )
        print(response)

        return response

    except openai.APIError as e:
        # Handling errors related to openai
        print(f"An error occurred trying to get a response from openai: {e}")
        #return None



#def conversation(messages, role = "system", content = "Start the conversation.", temperature = 0.5):
def conversation(chat_history):

    try:
        response = get_completion_from_messages(chat_history)
        print(response)

        role = response.choices[0].message.role
        content = response.choices[0].message.content

        # Append new answer of assistant to message stack
        chat_history.append({"role": role, "content": content})

        print(chat_history)
        
        return None

    except Exception as error:
        # Handling unexpected errors
        print(f"Unexpected error: {error}")
        chat_history.pop()

        return("Something went wrong. Have look at the terminal outputs")
