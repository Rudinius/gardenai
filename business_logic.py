from api_call import get_response_openai
from data_connector import filter_dataframe
import json

def append_assistant_message(response, chat_history):
    """
        Utility funcition to extract the message 
        and role and append it to the chat history dictionary
    """
    # Extract for app relevant content of response
    role = response.choices[0].message.role
    content = response.choices[0].message.content

    # Append new answer of assistant to message stack
    chat_history.append({"role": role, "content": content})

def business_logic(chat_history, df_data):
    """
        Function that handles the business logic. It will call the 'get_response_openai' function.
        Based on the response of that function, it will call the function 'get_plants' and update the 
        'chat_history' object.
        Arguments:
            chat_history (dict)
        Returns:
            error (str or None)
    """

    try:
        # Call function for openai api
        response = get_response_openai(chat_history)
    
        # Check if the tools have been called
        if response.choices[0].finish_reason == "tool_calls":
            
            arguments = response.choices[0].message.tool_calls[0].function.arguments

            # The arguments are in str, so they have to be converted json
            df_filtered = filter_dataframe(df_data, json.loads(arguments))

            # Convert to a list
            plant_selection = list(df_filtered["common_name"].values)


            # Create an intermediate chat_history object
            chat_history_intermediate = chat_history.copy()

            # Add the json response to the the intermediate chat history dictionary
            chat_history_intermediate.append({"role": "assistant", "content": arguments})
            
            chat_history_intermediate.append({"role": "system", 
                                              "content": f"This is a list of possible native plants, \
                                                based on the user information. Provide this list back \
                                                to the user in a structured way: {plant_selection}"})

            # Call the openai api again to create a user friendly response
            try:
                # Call the api again with tool_chouice set to none to force a text response
                response = get_response_openai(chat_history_intermediate, tool_choice="none")  

                append_assistant_message(response, chat_history)

                return None 

            except Exception as error:
                # Handling unexpected errors
                print(f"Unexpected error: {error}")

                # Here,the last messages gets removes from chat history.
                # This prevents the chat history from getting bigger by user inputs in case of errors
                chat_history.pop()

                return("Something went wrong. Have look at the terminal outputs")

        # No tool has been called, normal text response
        else:

            append_assistant_message(response, chat_history)

            return None

    except Exception as error:
        # Handling unexpected errors
        print(f"Unexpected error: {error}")

        # Here,the last messages gets removes from chat history.
        # This prevents the chat history from getting bigger by user inputs in case of errors
        chat_history.pop()

        return("Something went wrong. Have look at the terminal outputs")
