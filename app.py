import streamlit as st
import matplotlib.pyplot as plt
from auth import register
from auth import login
from resume_parser import extract_text
from resume_parser import extract_skills
from ats_score import calculate_ats
from courses import courses
from interview_questions import questions
from roadmaps import roadmaps
from report_generator import generate_report
from chatbot import chatbot_reply
from chat_db import save_chat, get_history
import pickle

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🚀",
    layout="wide"
)

with open("style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

uploaded_file = None

st.markdown("""
<div style="
background: linear-gradient(135deg,#2563eb,#7c3aed);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:20px;
">

<h1>🚀 AI Career Mentor</h1>

<p style="font-size:18px;">
Analyze resumes, improve ATS scores, discover career paths,
prepare for interviews and receive personalized guidance.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
padding:20px;
border-radius:15px;
background:rgba(255,255,255,0.08);
text-align:center;
margin-bottom:20px;
">

<h3>🎯 Smart Resume Analyzer</h3>

<p>
AI-powered ATS scoring, skill-gap analysis,
career roadmap generation, interview preparation,
and resume improvement suggestions.
</p>

</div>
""", unsafe_allow_html=True)
st.sidebar.title("🚀 AI Career Mentor")
st.sidebar.caption("Career Intelligence Platform")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "Menu",
    ["Login", "Signup"]
)

# SIGNUP

if menu == "Signup":

    st.subheader("Create Account")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Signup"):

        if register(
            username,
            password
        ):

            st.success(
                "Account Created Successfully"
            )

        else:

            st.error(
                "Username Already Exists"
            )

# LOGIN

if menu == "Login":

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        st.subheader("🔐 Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True

                st.session_state.username = username

                st.success(
                    "Login Successful"
                )

            else:

                st.error(
                    "Invalid Credentials"
                )

if st.session_state.logged_in:

    uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
    )

    st.sidebar.success(
        f"Welcome {st.session_state.username}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    st.header( "🏠 Dashboard")
    col1,col2,col3,col4 = st.columns(4)
        
    st.markdown("---")

    st.subheader("📄 Upload Your Resume")
    st.markdown("---")
    st.subheader("Career Chatbot")

    question = st.text_input("Ask a Career Question")

    if st.button("Ask AI"):

        answer = chatbot_reply(question)

        st.success(answer)

        save_chat(
            st.session_state.username,
            question,
            answer
        )

    st.subheader("Chat History")

history = get_history(
    st.session_state.username
)

for user_msg, bot_msg, timestamp in history:
    st.write(f"👤 You: {user_msg}")
    st.write(f"🤖 Mentor: {bot_msg}")
    st.write("---")


if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    st.success("Resume Uploaded Successfully")

    # Skills Section

    st.subheader("🧠 Detected Skills")

    skill_text = ""

    for skill in skills:
        skill_text += f"✅ {skill}\n"

    st.text(skill_text)

    # ATS Score

    ats = calculate_ats(skills)

    st.subheader("📊 ATS Score")

    st.progress(int(ats))

    st.metric(
        "ATS Score",
        f"{int(ats)}%"
    )
    fig, ax = plt.subplots(figsize=(5,5))
    
    ax.pie(
        [ats,100-ats],
        labels=["Matched","Missing"],
        autopct="%1.1f%%"
    )
    st.pyplot(fig)

    # Role Prediction

    with open(
        "role_predictor.pkl",
        "rb"
    ) as f:

        model = pickle.load(f)

    role = model.predict(
        [" ".join(skills)]
    )[0]

    st.subheader("🎯 Recommended Job Role")

    st.success(role)

    # Dashboard Cards

    col1,col2,col3 = st.columns(3)

    col1.metric(
        "Skills Found",
        len(skills)
    )

    col2.metric(
        "ATS Score",
        f"{int(ats)}%"
    )

    col3.metric(
        "Career Role",
        role
    )

    # Skill Gap Analysis

    st.subheader("📈 Skill Gap Analysis")

    required_skills = {

        "Data Scientist":[
            "python",
            "sql",
            "machine learning",
            "pandas",
            "numpy"
        ],

        "Frontend Developer":[
            "html",
            "css",
            "javascript",
            "react"
        ],

        "Backend Developer":[
            "python",
            "django",
            "flask",
            "sql"
        ],

        "AI Engineer":[
            "python",
            "tensorflow",
            "pytorch",
            "deep learning"
        ]
    }

    missing = []

    for skill in required_skills.get(role, []):

        if skill not in skills:

            missing.append(skill)

    if missing:

        for skill in missing:

            st.warning(
                f"Missing Skill: {skill}"
            )

    else:

        st.success(
            "No Skill Gaps Found"
        )

    # Resume Suggestions

    st.subheader("💡 Resume Improvement Suggestions")

    suggestions = []

    if "github" not in skills:
        suggestions.append(
            "Add GitHub profile link."
        )

    if "sql" not in skills:
        suggestions.append(
            "Add SQL projects."
        )

    if "python" not in skills:
        suggestions.append(
            "Learn Python."
        )

    if len(skills) < 5:
        suggestions.append(
            "Add more technical skills."
        )

    if suggestions:

        for item in suggestions:

            st.info(item)

    else:

        st.success(
            "Resume looks good!"
        )

    # Courses

    st.subheader("📚 Recommended Courses")

    if role in courses:

        for course in courses[role]:

            st.write(
                "✅",
                course
            )

    # Interview Questions

    st.subheader("🎤 Interview Questions")

    if role in questions:

        for q in questions[role]:

            st.write(
                "🔹",
                q
            )

    # Career Roadmap

    st.subheader("🗺 Career Roadmap")

    if role in roadmaps:

        for step in roadmaps[role]:

            st.write(
                "➡️",
                step
            )

    generate_report(
        "career_report.pdf",role,ats,skills
    )
    with open("career_report.pdf","rb") as file:
        st.download_button(
            "Download Report",
            file,
            file_name="career_report.pdf"
        )

st.markdown("---")

st.markdown("""
<div class="footer">

AI Career Mentor © 2026

Developed by Gajula Praveena

</div>
""", unsafe_allow_html=True)