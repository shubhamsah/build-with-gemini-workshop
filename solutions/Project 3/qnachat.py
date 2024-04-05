# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import necessary libraries
import streamlit as st
import os
import google.generativeai as genai

# Configure the Google API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a Generative Model instance
model = genai.GenerativeModel("gemini-pro")

# Initialize a new chat with "chat"
chat = model.start_chat(history=[])

# Function to get a response from Gemini
def get_gemini_response(question):
    """Get a response from the Gemini model.

    Args:
        question (str): The question to ask the model.

    Returns:
        list: A list of text chunks in the response.
    """
    response = chat.send_message(question, stream=True)
    return response

# Set the page title and header
st.set_page_config(page_title="QnA chat Demo App")
st.header("Gemini QnA chat Application")

# Initialize the chat history in the session state
if 'chat_history' not in st.session_state:
    st.session_chat['chat_history'] = []

# Get the user input
input = st.text_input("Input: ", key="input")

# Submit button
submit=st.button("Ask the question")

# Send the input to the model and get the response if the submit button is pressed and the input is not empty
if submit and input:
    response = get_gemini_response(input)

    # Add the response and query in the session chat history
    st.session_state['chat_history'].append("You", input)

    # Display the response
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append("Bot", chunk.text)

# Display the chat history
st.subheader("The Chat History is: ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
