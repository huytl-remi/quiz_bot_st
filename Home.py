import streamlit as st
import os

def main():
    st.set_page_config(layout="wide", page_title="Course and Quiz Generator")

    # Check if API key is in session state
    if 'openai_api_key' not in st.session_state:
        st.title("Welcome to the Course and Quiz Generator")
        st.write("Please enter your OpenAI API key to get started.")
        api_key = st.text_input("OpenAI API Key", type="password")
        if st.button("Submit"):
            if api_key:
                st.session_state.openai_api_key = api_key
                os.environ["OPENAI_API_KEY"] = api_key
                st.success("API key set successfully!")
                st.rerun()
            else:
                st.error("Please enter a valid API key.")
    else:
        st.title("Course and Quiz Generator")
        st.write("Welcome to the Course and Quiz Generator. Use the sidebar to navigate between generating course outlines and quizzes.")

        st.write("How to use this app:")
        st.write("1. Go to 'Course Outline' to upload a document and generate a course outline.")
        st.write("2. After generating a course outline, you can save it for later use.")
        st.write("3. Go to 'Quiz Generation' to create quizzes based on the generated course outline.")
        st.write("4. You can load previously saved course outlines to generate quizzes without regenerating the outline.")

        # Add a button to clear the API key if needed
        if st.button("Clear API Key"):
            del st.session_state.openai_api_key
            st.success("API key cleared. Please refresh the page.")

if __name__ == "__main__":
    main()
