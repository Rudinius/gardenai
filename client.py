import streamlit as st
from api_call_openai import conversation

# Initial value of chat history
chat_history = [{
    "role": "assistant",
    "content": "How can I help you"
    }]

# Check if the dictionary exists in session state
if "chat_history" not in st.session_state:
    # Initialize the dictionary
    st.session_state["chat_history"] = chat_history

# Check if the dictionary exists in session state
if "error" not in st.session_state:
    # Initialize the dictionary
    st.session_state["error"] = []

# Function placeholders for API calls
def submit_handler():

    # Append the user input to the chat history dictionary
    st.session_state["chat_history"].append({
        "role": "user",
        "content": f"{st.session_state["user_input"]}"
        })
    
    # Call the openai API 
    # Session state gets directly manipulated in funtion. 
    # Errors get returned 
    error = conversation(st.session_state["chat_history"])

    # If error, it will be added to error session state
    # If no error, error session state will be cleared
    if error:
        st.session_state["error"].append(error)
    else:
        st.session_state["error"] = []

# Handles the callback of reset button
def reset_handler():

    # Delete all session state
    for key in st.session_state.keys():
        del st.session_state[key]

    # Set session state to initial value
    st.session_state["chat_history"] = chat_history

# Set up the Streamlit layout
def main():
    # Headline text of the website
    st.title("Native Plant Garden Advisor")

    # Short description text
    st.write("Description...")

    chatbox = st.container(height=300)

    # Creating columns for button placement
    col1, col2 = st.columns([0.9, 0.1])

    with col1:
        st.chat_input("Ask the AI agent for help", on_submit=submit_handler, key="user_input")

    with col2:
        st.button('Reset', on_click=reset_handler)

    # Print messages in chat history stack
    for chat_message in st.session_state["chat_history"]:
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
    main()
