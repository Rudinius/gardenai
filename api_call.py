import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.environ.get("GARDENAI_API_KEY", "If ENVVAR not set, paste API key here")

client = OpenAI(api_key=API_KEY)

# Load the tools object from tools.json
with open('tools.json', 'r') as tools:
    tools = json.load(tools)

def get_response_openai(chat_history, tool_choice="auto"):
    """
        Function that calls the openai api
        Arguments:
            chat_history (dict)
        Return:
            response (dict)
    """

    try:
        response = client.chat.completions.create(
            messages=chat_history,
            tools=tools,
            tool_choice=tool_choice,
            model="gpt-3.5-turbo",
        )
        return response

    except APIError as e:
        # Handling errors related to openai
        print(f"An error occurred trying to get a response from openai: {e}")