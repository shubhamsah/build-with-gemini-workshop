from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question):
    # Load Gemini model and generate response
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


def display_response(text):
    # Display response in a subheader
    st.subheader("The Response is")
    st.write(to_markdown(text))

def main():
    # Set page title and header
    st.set_page_config(page_title="Q&A Demo")
    st.header("Gemini Application")

    # User input
    input_text = st.text_input("Input:", key="input")

    # Button to generate a response
    submit_button = st.button("Generate")

    if submit_button:
        # Get a response and display
        response = get_gemini_response(input_text)
        display_response(response)


if __name__ == "__main__":
    # Run the main function
    main()
