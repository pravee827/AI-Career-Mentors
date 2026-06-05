from PyPDF2 import PdfReader

skills_db = [
    "python",
    "java",
    "c",
    "c++",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "sql",
    "mysql",
    "mongodb",
    "power bi",
    "tableau",
    "excel",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "django",
    "flask",
    "streamlit",
    "numpy",
    "pandas",
    "opencv",
    "tensorflow",
    "keras",
    "pytorch",
    "yolo",
    "git",
    "github"
]

def extract_text(pdf_file):

    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text.lower()


def extract_skills(text):

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills