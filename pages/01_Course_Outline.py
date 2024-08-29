import streamlit as st
from openai import OpenAI
import time
from course_generation import generate_course
from display_utils import display_course
from save_load_utils import save_course, load_course, get_saved_courses
from prompts import COURSE_GENERATION_PROMPT
import os

client = OpenAI(api_key=st.session_state.openai_api_key)

def create_assistant(vector_store_id):
    assistant = client.beta.assistants.create(
        name="Course Generator",
        instructions="You are an expert in creating comprehensive course outlines based on provided documents.",
        model="gpt-4o",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )
    return assistant

def create_thread():
    return client.beta.threads.create()

def create_vector_store(file):
    vector_store = client.beta.vector_stores.create(name="Course Document")
    file_obj = client.files.create(file=file, purpose="assistants")

    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=[file]
    )

    return vector_store.id

def run_assistant(thread_id, assistant_id, user_message):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == 'completed':
            break
        time.sleep(1)

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    latest_message = messages.data[0]

    if latest_message.content[0].type == 'text':
        return latest_message.content[0].text.value
    else:
        return "Unable to retrieve message content."

def main():
    st.title("Course Outline Generator")

    # Check if API key is set
    if "OPENAI_API_KEY" not in st.session_state or not st.session_state["OPENAI_API_KEY"]:
        st.warning("Please enter your OpenAI API key on the Home page to use this feature.")
        return

    client = OpenAI(api_key=st.session_state["OPENAI_API_KEY"])

    # Initialize session state
    if 'course' not in st.session_state:
        st.session_state.course = None

    # File upload
    uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")

    if uploaded_file is not None:
        st.success("PDF successfully uploaded.")

        if 'vector_store_id' not in st.session_state:
            with st.spinner("Processing document..."):
                st.session_state.vector_store_id = create_vector_store(uploaded_file)

        if 'assistant' not in st.session_state:
            st.session_state.assistant = create_assistant(st.session_state.vector_store_id)

        if 'thread' not in st.session_state:
            st.session_state.thread = create_thread()

        # Generate course outline
        if st.button("Generate Course Outline", key="generate_button"):
            with st.spinner("Generating course outline..."):
                course_prompt = f"{COURSE_GENERATION_PROMPT}\n\nPlease create a course outline based on the uploaded document."
                course_response = run_assistant(st.session_state.thread.id, st.session_state.assistant.id, course_prompt)
                st.session_state.course = generate_course(course_response)

    # Display and save course outline
    if st.session_state.course:
        display_course(st.session_state.course)

        # Save course outline
        save_name = st.text_input("Enter a name to save this course outline:")
        if st.button("Save Course Outline") and save_name:
            save_course(st.session_state.course, save_name)
            st.success(f"Course outline saved as '{save_name}'")

    # Load saved course
    st.sidebar.header("Load Saved Course")
    saved_courses = get_saved_courses()
    if saved_courses:
        selected_course = st.sidebar.selectbox("Select a saved course outline", saved_courses)
        if st.sidebar.button("Load Course"):
            loaded_course = load_course(selected_course)
            if loaded_course:
                st.session_state.course = loaded_course
                st.rerun()  # Rerun the app to update the main area with the loaded course
            else:
                st.sidebar.error("Failed to load the selected course outline.")
    else:
        st.sidebar.info("No saved course outlines found.")

if __name__ == "__main__":
    main()
