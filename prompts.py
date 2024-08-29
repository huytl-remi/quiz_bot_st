COURSE_GENERATION_PROMPT = """
Create a comprehensive micro-training course outline based on the provided document. Your response should be detailed and focus on crucial, learnable materials. Structure your output as follows:
**Output format:**
{{
  "language": "Specify the language of the input document here",
  "course_title": "Provide a descriptive title for the course",
  "course_summary": "Write a thorough overview of the entire course",
  "learning_objectives": [
    "List 3-5 specific, measurable learning objectives for the entire course"
  ],
  "modules": [
    {{
      "module_title": "Clear title for this module",
      "key_points": [
        {{
          "point": "A detailed, learnable fact or concept",
          "reference": "Exact quote of the beginning phrase of the respective material"
        }}
      ]
    }}
  ]
}}
**Guidelines:**
1. Language and Course Title:
   - Specify the language and must generate the course in the input document's language
   - Provide a clear, descriptive title for the course that accurately reflects its content.
2. Course Summary:
   - Write a thorough overview of the entire course.
   - Include key themes, skills, or knowledge areas that learners will master.
   - Provide context for why this course is important or relevant.
3. Learning Objectives:
   - List 3-5 specific, measurable learning objectives for the entire course.
   - Ensure objectives clearly state what learners should be able to do or understand after completing the course.
   - Use action verbs and make objectives as concrete and measurable as possible.
4. Modules:
   - Identify distinct modules that thoroughly cover the main topics of the document.
   - Don't limit yourself to a specific number of modules; include as many as necessary to cover all important content.
   - Ensure each module has a clear, descriptive title.
5. Key Points:
   - For each module, provide detailed and crucial information as key points.
   - Each key point should be a specific, learnable fact or concept.
   - Don't restrict the number of key points; include all important concepts that learners should understand.
   - Ensure each key point has a reference field with an exact quote of the beginning phrase of the respective material in the source document.
6. Content Depth and Consistency:
   - Maintain consistent depth and detail across all modules.
   - Use clear language appropriate for educational content.
   - Don't shy away from necessary technical terms or complex concepts if they're crucial to understanding the material.
7. Comprehensive Coverage:
   - Ensure that between the course summary, learning objectives, and module key points, all important content from the source document is covered.
8. Logical Flow:
   - Organize modules and key points in a logical sequence that facilitates learning and understanding.
9. Accuracy and Relevance:
    - Ensure all information is accurate and directly relevant to the course objectives.
    - Double-check that all references correctly match the source material.
Remember to adapt the content to fit the structured JSON format provided earlier. This approach will create a comprehensive, well-organized micro-training course outline based on the provided document.
"""

QUIZ_GENERATION_PROMPT = """
Generate a comprehensive set of {num_questions} quizzes for the "{module_title}" module based on the provided document. Focus on creating detailed, thought-provoking questions that test deep understanding of the material. Structure your output as follows:
Output format:
{{
  "module_title": "Repeat the module title here",
  "quizzes": [
    {{
      "question": "Write a detailed question based on the module content",
      "question_type": "multiple_choice OR true_false",
      "choices": [
        {{"text": "Option text", "is_correct": boolean}}
      ],
      "explanation": "Provide a comprehensive explanation of the correct answer and why other options are incorrect",
      "reference": {{
        "text": "Include an EXACT, word-for-word quote from the source document that supports the correct answer"
      }}
    }}
  ]
}}
Guidelines:
1. Ensure questions are directly related to the key points of the module and the course-level learning objectives, exploring nuances and deeper implications of the content.
2. Vary the difficulty and complexity of questions to test different levels of understanding, from basic recall to application and analysis of concepts.
3. Write clear, unambiguous questions, but don't shy away from complexity if it's necessary to fully test understanding of the material.
4. Provide detailed explanations for each question. These should not only state why the correct answer is right but also explain why each incorrect option is wrong, helping learners understand the nuances of the topic.
5. Use precise quotes from the document for references to support the correct answer. These should provide context and reinforce the explanation.
6. Alternate between multiple-choice and true/false questions to provide variety while maintaining focus on these two question types.
7. Generate exactly {num_questions} questions for this module, ensuring comprehensive coverage of all important concepts and alignment with course-level learning objectives.
8. For multiple-choice questions, provide 4 answer options. For true/false questions, ensure a balanced mix of true and false statements across the quiz set.
9. Frame some questions as scenarios or case studies to encourage critical thinking and application of knowledge.
10. Regularly refer back to the course-level learning objectives to ensure that the quizzes collectively assess all intended learning outcomes of the course.
"""
