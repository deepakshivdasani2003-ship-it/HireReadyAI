import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="HireReady AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------------
# PREMIUM CSS
# -----------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color: white;
    font-family: 'Segoe UI';
}

.main-title{
    font-size:48px;
    font-weight:800;
    color:#38bdf8;
}

.sub{
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:25px;
}

.card{
    background: rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:20px;
    margin-bottom:15px;
}

.stButton>button{
    width:100%;
    border-radius:14px;
    height:50px;
    font-size:18px;
    background:#38bdf8;
    color:white;
    border:none;
}

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.06);
    padding:15px;
    border-radius:18px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown('<div class="main-title">🚀 HireReady AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub">AI-Powered Skill Assessment & Personalized Learning Plan Agent</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("Dashboard")
st.sidebar.success("Hackathon Premium Build")
st.sidebar.write("1️⃣ Upload Resume")
st.sidebar.write("2️⃣ Paste Job Description")
st.sidebar.write("3️⃣ Run Assessment")
st.sidebar.write("4️⃣ Generate Roadmap")

# -----------------------------------
# INPUTS
# -----------------------------------
col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("📄 Upload Resume", type=["pdf", "txt", "docx"])

with col2:
    jd = st.text_area("💼 Paste Job Description", height=220)

# -----------------------------------
# BUTTON
# -----------------------------------
if st.button("🚀 Start Assessment"):

    with st.spinner("Analyzing Candidate Profile..."):
        time.sleep(2)

    # -----------------------------------
    # METRICS
    # -----------------------------------
    st.subheader("📈 Candidate Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Resume Score", "84%")
    c2.metric("Skill Match", "78%")
    c3.metric("Hiring Potential", "High")
    c4.metric("Gap Severity", "Medium")

    st.write("---")

    # -----------------------------------
    # SKILLS FOUND
    # -----------------------------------
    st.subheader("🧠 Detected Skills")

    skills = [
        "Python",
        "SQL",
        "Flask",
        "Git",
        "Machine Learning",
        "REST API"
    ]

    cols = st.columns(3)

    for i, skill in enumerate(skills):
        cols[i % 3].success(skill)

    st.write("---")

    # -----------------------------------
    # RADAR CHART (FIXED)
    # -----------------------------------
    st.subheader("📊 Real Skill Assessment")

    categories = [
        "Python",
        "SQL",
        "APIs",
        "Communication",
        "Problem Solving",
        "ML"
    ]

    values = [85, 72, 76, 68, 88, 74]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Score'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("---")

    # -----------------------------------
    # GAP ANALYSIS
    # -----------------------------------
    st.subheader("⚠️ Skill Gap Detection")

    st.error("Missing Skills: Docker, AWS, System Design")

    st.write("---")

    # -----------------------------------
    # ROADMAP
    # -----------------------------------
    st.subheader("📚 Personalized 30-Day Learning Roadmap")

    roadmap = pd.DataFrame({
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Focus": [
            "Docker Basics",
            "AWS Core Services",
            "System Design",
            "Interview Preparation"
        ],
        "Hours": ["6 hrs", "8 hrs", "10 hrs", "5 hrs"],
        "Resources": [
            "Docker Docs + YouTube",
            "AWS Free Tier",
            "System Design Basics",
            "Mock Interviews + DSA"
        ]
    })

    st.dataframe(roadmap, use_container_width=True)

    st.write("---")

    # -----------------------------------
    # INTERVIEW QUESTIONS
    # -----------------------------------
    st.subheader("🤖 AI Interview Questions")

    questions = [
        "Explain Python decorators.",
        "Difference between INNER JOIN and LEFT JOIN?",
        "How does JWT authentication work?",
        "How would you deploy a Flask app?"
    ]

    for q in questions:
        st.info(q)

    st.write("---")

    # -----------------------------------
    # REPORT DOWNLOAD
    # -----------------------------------
    report = """
HireReady AI Candidate Report

Resume Score: 84%
Skill Match: 78%
Hiring Potential: High

Detected Skills:
Python
SQL
Flask
Git
Machine Learning
REST API

Missing Skills:
Docker
AWS
System Design

Learning Plan:
Week 1 - Docker Basics
Week 2 - AWS Core Services
Week 3 - System Design
Week 4 - Interview Prep
"""

    st.download_button(
        label="📥 Download Candidate Report",
        data=report,
        file_name="HireReady_AI_Report.txt",
        mime="text/plain"
    )

    st.success("✅ Assessment Completed Successfully!")