import streamlit as st

st.set_page_config(
    page_title="Karan Baiga Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("🚀 Karan Baiga")
st.subheader("Data Science | Machine Learning | AI Enthusiast")

st.write("""
Aspiring Data Scientist and Machine Learning Engineer with hands-on experience
in Python, SQL, Data Analytics, Tableau, and Machine Learning.
Passionate about building AI-driven solutions and solving real-world problems.
""")

# Sidebar
st.sidebar.title("Contact")

st.sidebar.info("""
📧 kb410629@gmail.com

📱 +91 7566770325

📍 Bhopal, Madhya Pradesh
""")

# Education
st.header("🎓 Education")

st.write("""
**B.Tech Electronics & Communication Engineering**
(SISTec Bhopal)

CGPA: 5.94 / 10

2022 - 2026
""")

# Skills
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Python
    - SQL
    - C Programming
    - JavaScript
    - HTML/CSS
    - React
    """)

with col2:
    st.markdown("""
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Tableau
    - Machine Learning
    """)

# Experience
st.header("💼 Experience")

st.subheader("Software Development Engineer Intern")

st.write("""
**Bluestock Fintech**

April 2025 - May 2025
""")

st.markdown("""
- Worked on software development tasks
- Debugging and feature implementation
- Collaborated in virtual development environment
""")

# Projects
st.header("🚀 Projects")

project1, project2 = st.columns(2)

with project1:
    st.info("Retail Store Trial Analysis")
    st.write("""
    - R Programming
    - Statistical Analysis
    - Business Insights
    - Data Visualization
    """)

with project2:
    st.info("Interactive Tableau Dashboard")
    st.write("""
    - KPI Tracking
    - Business Analytics
    - Dashboard Design
    - Data Visualization
    """)

# Certifications
st.header("📜 Certifications")

st.markdown("""
✅ Web Development using HTML/CSS/JavaScript

✅ Deloitte Data Analytics Job Simulation

✅ Unstop Coding Challenges

✅ All India NCAT
""")

# Resume Download
st.header("📄 Resume")

with open("KaranResume.pdf", "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Karan_Baiga_Resume.pdf",
        mime="application/pdf"
    )


st.subheader("Technical Skills")

st.write("Python")
st.progress(90)

st.write("Machine Learning")
st.progress(80)

st.write("Data Science")
st.progress(85)

st.write("SQL")
st.progress(75)

st.write("Streamlit")
st.progress(90)

col1, col2 = st.columns(2)

with col1:
    st.image("Retail Store Trial Analysis.jpg")
    st.subheader("Retail Store Trial Analysis")
    st.write("Statistical analysis using R.")
    st.link_button("GitHub", "https://github.com/Karanb786")

with col2:
    st.image("Tableau Dashboard.jpg")
    st.subheader("Tableau Dashboard")
    st.write("Business KPI dashboard.")
    st.link_button("GitHub", "https://github.com/Karanb786")


st.subheader("Certifications")

cols = st.columns(3)

with cols[0]:
    st.image("certificate1.jpeg")
    st.caption("Software Development Engineer")

with cols[1]:
    st.image("certificate2.jpeg")
    st.caption("Vibe Coding")

with cols[2]:
    st.image("certificate3.jpeg")
    st.caption("Web Development")


skills = {
    "Python":90,
    "Machine Learning":85,
    "Data Science":85,
    "SQL":80,
    "Tableau":75,
    "Streamlit":90,
    "Django":70,
    "Deep Learning":65
}

import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.title("Karan Baiga AI Portfolio")

prompt = st.chat_input("Ask me anything about my profile")

if prompt:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response.choices[0].message.content)
    
# Footer
st.markdown("---")
st.write("© 2026 Karan Baiga | Data Science Portfolio")