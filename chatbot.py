def chatbot_reply(question):

    question = question.lower()

    # Data Science

    if "data science" in question:
        return """
Data Science roadmap:

1. Python
2. Pandas
3. NumPy
4. SQL
5. Statistics
6. Machine Learning
7. Deep Learning
8. Projects
"""

    # AI

    elif "ai" in question or "artificial intelligence" in question:
        return """
Artificial Intelligence combines Machine Learning,
Deep Learning, NLP, Computer Vision and Generative AI.
"""

    # Machine Learning

    elif "machine learning" in question:
        return """
Machine Learning Roadmap:

1. Python
2. Statistics
3. Pandas
4. NumPy
5. Scikit-Learn
6. Projects
"""

    # Deep Learning

    elif "deep learning" in question:
        return """
Deep Learning uses neural networks.

Popular frameworks:
- TensorFlow
- Keras
- PyTorch
"""

    # Python

    elif "python" in question:
        return """
Python is one of the most important programming
languages for AI, ML, Data Science and Web Development.
"""

    # SQL

    elif "sql" in question:
        return """
SQL is used for managing databases.

Important topics:
- SELECT
- JOIN
- GROUP BY
- HAVING
- Subqueries
"""

    # Resume

    elif "resume" in question:
        return """
Resume Tips:

✅ Add Projects
✅ Add Skills
✅ Add GitHub Link
✅ Add LinkedIn Link
✅ Keep it one page
"""

    # Interview

    elif "interview" in question:
        return """
Interview Preparation:

1. Practice Python
2. Practice SQL
3. Revise ML Concepts
4. Build Projects
5. Prepare HR Questions
"""

    # Frontend

    elif "frontend" in question:
        return """
Frontend Developer Roadmap:

HTML
CSS
JavaScript
React
Projects
Portfolio
"""

    # Backend

    elif "backend" in question:
        return """
Backend Developer Roadmap:

Python
Django
Flask
APIs
SQL
Deployment
"""

    # Data Analyst

    elif "data analyst" in question:
        return """
Data Analyst Roadmap:

Excel
SQL
Power BI
Python
Statistics
Projects
"""

    # Career

    elif "career" in question:
        return """
Popular Career Options:

• Data Scientist
• AI Engineer
• Data Analyst
• Backend Developer
• Frontend Developer
• Full Stack Developer
"""

    # Skills

    elif "skills" in question:
        return """
Top Skills in 2026:

Python
SQL
Machine Learning
Power BI
Cloud Computing
Generative AI
"""

    # Projects

    elif "project" in question:
        return """
Strong Resume Projects:

1. AI Career Mentor
2. Resume Analyzer
3. Face Recognition System
4. VisionixAI
5. Customer Churn Prediction
"""

    else:
        return """
I can help with:

• Data Science
• AI
• Machine Learning
• Python
• SQL
• Resume Building
• Interviews
• Career Guidance
• Projects

Try asking:
'How do I become a Data Scientist?'
"""