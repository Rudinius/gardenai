import streamlit as st
from data_connector import load_data
from business_logic import business_logic

# Function placeholders for API calls
def submit_handler():

    # Append the user input to the chat history dictionary
    st.session_state["chat_history"].append({
        "role": "user",
        "content": f"{st.session_state['user_input']}"
        })
    
    # Pass the chat history and data to the business logic 
    # Errors get returned 
    error = business_logic(st.session_state["chat_history"], st.session_state["df_data"])

    # If error, it will be added to error session state
    # If no error, error session state will be cleared
    if error:
        st.session_state["error"].append(error)
    else:
        st.session_state["error"] = []

# Handles the callback of reset button
def reset_handler():

    # Delete all session state
    # This way even the data gets cleared and reloaded. This might be inefficient for big data sets
    for key in st.session_state.keys():
        del st.session_state[key]

    # Set session state to initial value
    st.session_state["chat_history"] = chat_history

# Set up the Streamlit layout
def main():
    # Headline text of the website
    st.title("Native Plant Garden Advisor")

    # Short description text
    st.write("""This conversational AI will help to select a list of native plants 
             based on user input. Only data from the states of Michigan and Alabama are available.""")

    chatbox = st.container(height=300)

    # Creating columns for button placement
    col1, col2 = st.columns([0.80, 0.20])

    with col1:
        st.chat_input("Provide the AI agent with your information...", 
                      on_submit=submit_handler, key="user_input")

    with col2:
        st.button("Reset", on_click=reset_handler)

    # Print messages in chat history stack
    for chat_message in st.session_state["chat_history"]:
        if chat_message["role"] != "system":
            chatbox.chat_message(chat_message["role"]).write(chat_message["content"])

    # Print error messages to the message stack
    # Error messages are not added to the chat history stack
    if st.session_state["error"]:
        for i, error_message in enumerate(st.session_state["error"]):
            chatbox.chat_message(name="Error", avatar="🦖").write(f"({i+1}): {error_message}")

    # Disclaimer text at the bottom of the website
    st.write("Disclaimer: The data used in this app has been taken from Native Plant Information Network, NPIN (2013).\
             \nPublished on the Internet https://www.wildflower.org/collections/ [accessed March 16, 2024]. \
             \nLady Bird Johnson Wildflower Center at The University of Texas, Austin, TX.")


if __name__ == "__main__":

    # Initial value of chat history
    chat_history = [
        {
            "role": "system",
            "content": """
                Your task is to ask information regarding the garden of the user. 
                You will provide the received information as a structured list back to the user.
                You will keep asking the user for additional information.
                Present the user with a plant selection based on the provided data. 
                Use only plants from the provided data source within the context.
                Do not use information of plants from outside the context.
                If the user lives in a state other than Michigan or Alabama, mention to the user, that 
                only information about plants of states Michigan or Alabama can be provided.
            """
        },
        {
            "role": "assistant",
            "content": """
            Hello! I am your AI assistant. Please provide me with information about your garden. 
            With this information, I will help you select a native plant for growing in your garden. 
            Specifically, I would like to know about:

            - The state that you are located in (only Michigan or Alabama are supported)
            - The soil type of your garden e.g., 'dry', 'moist', or 'wet'.
            - The sun intensity of your garden e.g., 'sunny', 'partly-shaded', or 'shaded'.
            - The kind of plant you are looking for e.g., 'tree', 'herb', 'shrub', 'grass or grass-like', 'vine', 'cactus or succulent', or 'fern'.
            - The life-cycle of the plant you are looking for e.g., 'perennial', 'annual', or 'biennial'.

            The more information you provide me, the better I can assist you in selecting a specific plant.
            """
        }]

    # Check if the dictionary exists in session state
    if "df_data" not in st.session_state:
        # Initialize the dictionary
        # Load the data
        st.session_state["df_data"] = load_data("./data/", "native_plants_AL_MI_v_1.csv")

    # Check if the dictionary exists in session state
    if "chat_history" not in st.session_state:
        # Initialize the dictionary
        st.session_state["chat_history"] = chat_history

    # Check if the dictionary exists in session state
    if "error" not in st.session_state:
        # Initialize the dictionary
        st.session_state["error"] = []

    main()
