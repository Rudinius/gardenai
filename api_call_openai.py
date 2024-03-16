import os
from openai import OpenAI
from openai import APIError

# Get API key from environment variables
API_KEY = os.environ.get("STUDYAI_API_KEY", "If ENVVAR not set, paste API key here")
client = OpenAI(api_key=API_KEY)

tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_garden_info",
            "description": "Retrieve the information provided by the user about the location\
                soil type, amount of sun and further infos",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The state the user lives in",
                    },
                    "duration": {
                        "type": "string",
                        "enum": ["NA", "Perennial", "Annual", "Biennial"],
                        "description": "The type of plant, the user is looking for regarding the\
                            the live duration of the plant",
                    },
                },
                "required": ["location", "duration"]
            },
        }
    },
]

def get_response_openai(chat_history, model="gpt-3.5-turbo"):

    try:
        response = client.chat.completions.create(
            messages=chat_history,
            tools=tools,
            model=model,
            temperature=0.2 # Temperature set to low value to have more consistent behavior
        )
        print(response)
        return response

    except APIError as e:
        # Handling errors related to openai
        print(f"An error occurred trying to get a response from openai: {e}")

def conversation(chat_history):

    try:
        response = get_response_openai(chat_history)
    
        # Check if the tools have been called
        if response.choices[0].finish_reason == "tool_calls":
            print("tool calls")
            print(response.choices[0].message.tool_calls[0].function.arguments)
        # No tool has been called, normal text response
        else:
            # Extract for app relevant content of response
            role = response.choices[0].message.role
            content = response.choices[0].message.content

            # Append new answer of assistant to message stack
            chat_history.append({"role": role, "content": content})

            return None

    except Exception as error:
        # Handling unexpected errors
        print(f"Unexpected error: {error}")

        # Here,the last messages gets removes from chat history.
        # This prevents the chat history from getting bigger by user inputs in case of errors
        chat_history.pop()

        return("Something went wrong. Have look at the terminal outputs")
