import json
import os
import streamlit as st

SAVE_DIRECTORY = "saved_courses"

def save_course(course_data, filename):
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    filepath = os.path.join(SAVE_DIRECTORY, f"{filename}.json")
    with open(filepath, 'w') as f:
        json.dump(course_data, f)

def load_course(filename):
    filepath = os.path.join(SAVE_DIRECTORY, f"{filename}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return None

def get_saved_courses():
    if not os.path.exists(SAVE_DIRECTORY):
        return []
    return [f[:-5] for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]

def delete_course(filename):
    filepath = os.path.join(SAVE_DIRECTORY, f"{filename}.json")
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

def update_course_with_quiz(course_data, module_index, quiz_data):
    if 'modules' not in course_data:
        course_data['modules'] = []

    if module_index < len(course_data['modules']):
        course_data['modules'][module_index]['quiz'] = quiz_data

    return course_data
