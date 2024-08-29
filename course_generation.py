import json
import streamlit as st

def generate_course(response):
    try:
        # Log the raw response for debugging
        # st.write("Raw AI response:", response)

        # Attempt to find and extract JSON from the response
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start != -1 and json_end != -1:
            json_str = response[json_start:json_end]
            course_data = json.loads(json_str)

            # Validate the course data structure
            if not all(key in course_data for key in ['course_title', 'course_summary', 'learning_objectives', 'modules']):
                raise ValueError("Missing required fields in course data")

            return course_data
        else:
            raise ValueError("No valid JSON found in the response")
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse JSON: {str(e)}")
    except ValueError as e:
        st.error(f"Invalid course data structure: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

    return None
