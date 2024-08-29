# File: api_utils.py
import streamlit as st
from openai import OpenAI
import json
import re

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

def extract_json_from_string(s):
    # Find the first occurrence of '{' and the last occurrence of '}'
    start = s.find('{')
    end = s.rfind('}')

    if start != -1 and end != -1:
        # Extract the substring between '{' and '}'
        json_str = s[start:end+1]

        # Remove any markdown code block syntax
        json_str = re.sub(r'```json\s*', '', json_str)
        json_str = re.sub(r'\s*```', '', json_str)

        return json_str
    return None

def call_openai_api(messages):
    try:
        response = client.chat.completions.create(
            model="qwen2:72b",
            messages=messages
        )
        content = response.choices[0].message.content

        # Try to extract JSON from the content
        json_str = extract_json_from_string(content)

        if json_str:
            try:
                return json.loads(json_str)
            except json.JSONDecodeError as e:
                st.error(f"Error decoding JSON: {str(e)}")
                st.text("Raw content:")
                st.code(content)
                return None
        else:
            st.error("No valid JSON object found in the response")
            st.text("Raw content:")
            st.code(content)
            return None
    except Exception as e:
        st.error(f"Error calling OpenAI API: {str(e)}")
        return None
