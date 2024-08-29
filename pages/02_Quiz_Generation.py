import streamlit as st
from openai import OpenAI
import time
from quiz_generation import generate_quiz
from display_utils import display_interactive_quiz
from save_load_utils import load_course, get_saved_courses, update_course_with_quiz, save_course
from prompts import QUIZ_GENERATION_PROMPT
import os

def main():
    st.title("Quiz Generator")

    # Check if API key is set
    if "openai_api_key" not in st.session_state or not st.session_state["openai_api_key"]:
        st.warning("Please enter your OpenAI API key on the Home page to use this feature.")
        st.stop()

    # Initialize OpenAI client
    client = OpenAI(api_key=st.session_state["openai_api_key"])

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

    # Load saved course
    saved_courses = get_saved_courses()
    if saved_courses:
        selected_course = st.selectbox("Select a saved course outline", saved_courses)
        if st.button("Load Course"):
            loaded_course = load_course(selected_course)
            if loaded_course:
                st.session_state.course = loaded_course
                st.success("Course outline loaded successfully.")
            else:
                st.error("Failed to load the selected course outline.")
    else:
        st.warning("No saved course outlines found. Please generate and save a course outline first.")

    if 'course' not in st.session_state or st.session_state.course is None:
        st.warning("No course loaded. Please generate or load a course outline first.")
        st.stop()

    st.subheader(f"Current Course: {st.session_state.course.get('course_title', 'Untitled Course')}")

    module_names = [module['module_title'] for module in st.session_state.course.get('modules', [])]
    if not module_names:
        st.warning("No modules found in the course.")
        st.stop()

    selected_module_index = st.selectbox("Select a module for quiz generation",
                                         range(len(module_names)),
                                         format_func=lambda x: module_names[x])
    selected_module = module_names[selected_module_index]

    num_quizzes = st.number_input("Number of quiz questions to generate", min_value=1, value=5)

    if st.button("Generate Quiz"):
        if 'assistant' not in st.session_state or 'thread' not in st.session_state:
            st.error("Assistant or thread not initialized. Please go to the Course Outline page first.")
        else:
            with st.spinner(f"Generating {num_quizzes} quiz questions for {selected_module}..."):
                quiz_prompt = QUIZ_GENERATION_PROMPT.format(module_title=selected_module, num_questions=num_quizzes)
                quiz_prompt += f"\n\nPlease generate {num_quizzes} quiz questions based on the '{selected_module}' module."
                quiz_response = run_assistant(st.session_state.thread.id, st.session_state.assistant.id, quiz_prompt)
                quiz = generate_quiz(quiz_response, num_quizzes)

                if quiz:
                    st.session_state.course = update_course_with_quiz(st.session_state.course, selected_module_index, quiz)
                    save_course(st.session_state.course, st.session_state.course['course_title'])
                    st.success("Quiz generated and saved successfully!")
                else:
                    st.error("Failed to generate quiz. Please try again.")

    # Display the quiz if it exists for the selected module
    if 'quiz' in st.session_state.course['modules'][selected_module_index]:
        quiz = st.session_state.course['modules'][selected_module_index]['quiz']
        display_interactive_quiz(quiz, module_number=selected_module_index + 1)
    else:
        st.info("No quiz generated for this module yet. Click 'Generate Quiz' to create one.")

if __name__ == "__main__":
    main()
