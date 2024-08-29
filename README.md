# Course and Quiz Generator

## Overview

The Course and Quiz Generator is a Streamlit-based web application that leverages OpenAI's GPT models to automatically generate comprehensive course outlines and quizzes from uploaded PDF documents. This tool is designed to assist educators, trainers, and content creators in quickly developing structured learning materials.

## Features

- PDF document upload and processing
- Automatic generation of course outlines, including:
  - Course title
  - Course summary
  - Learning objectives
  - Modules with key points
- Interactive quiz generation for specific modules
- Customizable number of quiz questions
- User-friendly interface powered by Streamlit

## Requirements

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/course-quiz-generator.git
   cd course-quiz-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a PDF document containing the course material.

4. Click "Generate Course Outline" to create a structured course outline.

5. Select a module and specify the number of quiz questions you want to generate.

6. Click "Generate Quiz" to create a quiz for the selected module.

## File Structure

- `app.py`: Main application file
- `course_generation.py`: Functions for generating course outlines
- `quiz_generation.py`: Functions for generating quizzes
- `display_utils.py`: Utility functions for displaying course and quiz data
- `prompts.py`: Stores the prompts used for AI generation
- `.env`: Contains the OpenAI API key (not tracked by git)

## Contributing

Contributions to improve the Course and Quiz Generator are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

## License

[MIT License](LICENSE)

## Acknowledgements

This project uses the OpenAI API and is built with Streamlit. Special thanks to the open-source community for providing the tools and libraries that make this project possible.
