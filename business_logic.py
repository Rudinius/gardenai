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
            
            message = response.choices[0].message
            function_id = response.choices[0].message.tool_calls[0].id
            arguments = response.choices[0].message.tool_calls[0].function.arguments

            # The arguments are in str, so they have to be converted json
            df_filtered = filter_dataframe(df_data, json.loads(arguments))

            # Convert to a list
            plant_selection = list(df_filtered["common_name"].values)
            num_plant_selection = len(plant_selection)

            #print(arguments)
            #print(plant_selection)
            print(num_plant_selection)

            chat_history.append(message)

            chat_history.append({
                "role": "tool", 
                "content": f"Provided user information: {arguments} \
                            Number of elements: {num_plant_selection} \
                            List of Native plants: {plant_selection}", 
                "tool_call_id": function_id
            })
            
            # If plants could be retrieved from the database
            if num_plant_selection > 0:
                
                chat_history.append({
                    "role": "system", 
                    "content": f"1. Provide the 'Provided user information' back to the user in \
                                a formated structure. If a field was not provided, e.g. the value is \
                                empty or '', list this field as 'unspecified'. \
                                2. Provide the list 'List of Native plants' back to the user as a \
                                numbered list. Provide the full list back without leaving out an item. \
                                This means, you make sure, that the final list contains exactly \
                                'Number of elements' elements. E.g. if the provided list contains 21 elements \
                                'Number of elements', the numnered list must go from 1 to number 21.",
                })
            
            # No plants could be retrieved from the database
            else:
                chat_history.append({
                    "role": "system", 
                    "content": f"1. Provide the 'Provided user information' back to the user in \
                                a formated structure. \
                                2. Notify the user, that based on its provided information \
                                no plants could be retrieved from the database." \
                })

            # Call the openai api again to create a user friendly response
            try:
                # Call the api again with tool_chouice set to none to force a text response 
                response = get_response_openai(chat_history, tool_choice="none")  

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
