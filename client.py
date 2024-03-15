import streamlit as st

# Check if the dictionary exists in session state
if 'chat_history' not in st.session_state:
    # Initialize the dictionary
    st.session_state["chat_history"] = [{
            "role": "assistant",
            "content": "How can I help you"
        }]

# Function placeholders for API calls
def fetch_data_from_api_1():
    # Simulate an API call response
    return "Response from API 1"

def fetch_data_from_api_2():
    # Simulate an API call response
    return "Response from API 2"

chat_history = [{
    "role": "assistant",
    "content": "How can I help you"
    }]

# Set up the Streamlit layout
def main():
    # Headline text of the website
    st.title("My Streamlit App")

    # Short description text
    st.write("This is a simple Streamlit app to demonstrate basic functionality.")

    chatbox = st.container(height=300)

    # Creating columns for button placement
    col1, col2 = st.columns([0.9, 0.1])

    with col1:
        prompt = st.chat_input("Ask the AI agent for help")
        if prompt:
            st.session_state['chat_history'].append({
                "role": "user",
                "content": f"{prompt}"
            })

    with col2:
        if st.button('Reset'):
            # Reset the streamlit session state
            st.session_state["chat_history"] = [{
                "role": "assistant",
                "content": "How can I help you"
            }]

    for chat_message in st.session_state["chat_history"]:
        chatbox.chat_message(chat_message["role"]).write(chat_message["content"])

    # Disclaimer text at the bottom of the website
    st.write("Disclaimer: The data used in this app has been taken from Native Plant Information Network, NPIN (2013).\
             \nPublished on the Internet https://www.wildflower.org/collections/ [accessed March 16, 2024]. \
             \nLady Bird Johnson Wildflower Center at The University of Texas, Austin, TX.")

if __name__ == "__main__":
    main()