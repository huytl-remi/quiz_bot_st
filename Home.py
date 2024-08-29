import streamlit as st
import os

def main():
    st.set_page_config(layout="wide", page_title="Course and Quiz Generator")

    st.title("Course and Quiz Generator")

    # Check if API key is set
    if "openai_api_key" not in st.session_state or not st.session_state["openai_api_key"]:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if api_key:
            st.session_state["openai_api_key"] = api_key
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("API key set successfully!")
        else:
            st.warning("Please enter your OpenAI API key to use the app.")
            return

    st.write("Welcome to the Course and Quiz Generator. This tool helps you create comprehensive course outlines and quizzes from PDF documents.")

    st.markdown("""
    ### How to use this app:
    1. 📄 Upload a PDF document
    2. 🔍 Generate a course outline
    3. 💾 Save your outline for future use
    4. ✏️ Create quizzes based on the outline
    """)

    # Initialize session state variables
    if 'course' not in st.session_state:
        st.session_state.course = None
    if 'current_module' not in st.session_state:
        st.session_state.current_module = 0

    st.markdown("---")
    st.write("Ready to start? Navigate to 'Course Outline' in the sidebar to begin!")

if __name__ == "__main__":
    main()
