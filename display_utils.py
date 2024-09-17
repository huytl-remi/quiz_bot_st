import streamlit as st

def display_course(course):
    if course is None:
        st.error("No course data available to display.")
        return

    st.header(course.get('course_title', 'Untitled Course'))

    with st.expander("Course Summary", expanded=True):
        st.write(course.get('course_summary', 'No summary available.'))

    with st.expander("Learning Objectives", expanded=True):
        objectives = course.get('learning_objectives', [])
        if objectives:
            for obj in objectives:
                st.markdown(f"- {obj}")
        else:
            st.write("No learning objectives specified.")

    for i, module in enumerate(course.get('modules', []), 1):
        with st.expander(f"Module {i}: {module.get('module_title', 'Untitled Module')}"):
            for point in module.get('key_points', []):
                st.markdown(f"- **{point.get('point', 'No point specified')}**")
                st.markdown(f"{point.get('explanation', 'No explanation provided')}")
                st.caption(f"Reference: '{point.get('reference', 'No reference provided')}'")

def display_interactive_quiz(quiz, module_number):
    if quiz is None:
        st.error("No quiz data available to display.")
        return

    st.subheader(f"Quiz for Module {module_number}")

    # Initialize session state for user answers and question status if not already present
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'question_status' not in st.session_state:
        st.session_state.question_status = {}

    for j, question in enumerate(quiz.get('quizzes', []), 1):
        with st.expander(f"Question {j}", expanded=True):
            st.write(question.get('question', 'No question provided'))

            # Create a unique key for each question
            question_key = f"q_{module_number}_{j}"

            # Radio button for answer selection
            options = [choice['text'] for choice in question.get('choices', [])]
            user_answer = st.radio("Select your answer:", options, key=question_key)

            # Store user's answer in session state
            st.session_state.user_answers[question_key] = user_answer

            if st.button(f"Check Answer {j}"):
                correct_answer = next(choice['text'] for choice in question['choices'] if choice['is_correct'])
                if user_answer == correct_answer:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer is: {correct_answer}")

                st.write("Explanation:")
                st.info(question.get('explanation', 'No explanation provided'))

                # Mark the question as answered
                st.session_state.question_status[question_key] = True

            # Only show the reference if the question has been answered
            if st.session_state.question_status.get(question_key, False):
                st.caption(f"Reference: '{question.get('reference', {}).get('text', 'No reference provided')}'")
