import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Check if API key is set
if not os.getenv("OPENAI_API_KEY"):
    st.error("OpenAI API key is not set. Please check your .env file.")
    st.stop()

st.set_page_config(layout="wide", page_title="Course and Quiz Generator", page_icon="📚")

def main():
    st.title("📚 Course and Quiz Generator")

    st.markdown("""
    Welcome to the Course and Quiz Generator. This tool helps you create comprehensive course outlines and quizzes from your documents.

    ### How it works:
    1. **Upload** your document on the 'Course Outline' page
    2. **Generate** a course outline based on the document
    3. **Create** quizzes for specific modules on the 'Quiz Generation' page

    Get started by selecting a page from the sidebar!
    """)

    st.sidebar.markdown("## Navigation")
    st.sidebar.info("Select a page above to begin.")

if __name__ == "__main__":
    main()
