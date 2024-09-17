import json
import streamlit as st

def generate_quiz(response, num_questions):
    try:
        # Log the raw response for debugging
        # st.write("Raw AI response for quiz:", response)

        # Clean up the response string
        response = response.strip()

        # Attempt to find and extract JSON from the response
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start != -1 and json_end != -1:
            json_str = response[json_start:json_end]

            # Remove any leading/trailing whitespace and newlines
            json_str = json_str.strip()

            quiz_data = json.loads(json_str)

            # Validate the quiz data structure
            if not all(key in quiz_data for key in ['module_title', 'quizzes']):
                raise ValueError("Missing required fields in quiz data")

            # Ensure we have the correct number of questions
            quiz_data['quizzes'] = quiz_data['quizzes'][:num_questions]
            while len(quiz_data['quizzes']) < num_questions:
                quiz_data['quizzes'].append({
                    "question": "Additional question placeholder",
                    "choices": [
                        {"text": "Option A", "is_correct": False},
                        {"text": "Option B", "is_correct": False},
                        {"text": "Option C", "is_correct": False},
                        {"text": "Option D", "is_correct": True}
                    ],
                    "explanation": "Placeholder explanation",
                })

            return quiz_data
        else:
            raise ValueError("No valid JSON found in the response")
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse JSON for quiz. Error: {str(e)}")
        st.write("Problematic JSON string:", json_str)
    except ValueError as e:
        st.error(f"Invalid quiz data structure: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred while generating quiz: {str(e)}")

    return None
