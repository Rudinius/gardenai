import os
from openai import OpenAI
from openai import APIError

# Get API key from environment variables
API_KEY = os.environ.get("GARDENAI_API_KEY", "If ENVVAR not set, paste API key here")
client = OpenAI(api_key=API_KEY)

tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_garden_info",
            "description": """Retrieve the information provided by the user about the state,
                the soil type, amount of sun in the garden, the preferred type of plant, 
                and the preferred life-cycle of the plant""",
            "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                        "type": "string",
                        "enum": ["", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", 
                                 "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", 
                                 "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", 
                                 "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", 
                                 "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
                                 "WI", "WY"],
                        "description": """The state the user lives in. For example Michigan is MI. 
                            Nothing mentioned is an empty string ''"""
                    },
                    "habit": {
                        "type": "string",
                        "enum": ["", "tree", "herb", "shrub", "grass/grass-like", 
                                 "vine", "cactus/succulent", "fern"],
                        "description": """The type of plant the user is looking for regarding the 
                            the type of plant like tree or herb. 
                            Nothing mentioned is an empty string ''""",
                    },
                    "duration": {
                        "type": "string",
                        "enum": ["", "perennial", "annual", "biennial"],
                        "description": """The type of plant, the user is looking for regarding the
                            the live duration of the plant. 
                            Nothing mentioned is an empty string ''""",
                    },
                    "sun": {
                        "type": "string",
                        "enum": ["", "sun", "shade", "part-shade"],
                        "description": """The amount of sun in the garden. For example 
                            a sunny garden is sun. Nothing mentioned is an empty string ''"""
                    },
                    "water": {
                        "type": "string",
                        "enum": ["", "dry", "moist", "wet"],
                        "description": """The soil type of the garden. For example 
                            if the soil is dry, moist or wet. Nothing mentioned is an empty string ''"""
                    },
                    "other": {
                        "type": "string",
                        "description": """If the user provides any additional information
                            for example if the user likes to have plant with fruits or
                            a preference in color of the blossoms"""
                    },
                },
                "required": ["state", "habit", "duration", "sun", "water"]
            },
        }
    },
]

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