import streamlit as st
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

# Function to optimize resume content
def optimize_resume_content(user_info):
    try:
        prompt = (
            f"Please help optimize my resume content. Write detailed experience and project details.\n\n"
            f"Education: {user_info['education']}\n\n"
            f"Experience: {user_info['experience']}\n\n"
            f"Projects: {user_info['projects']}\n\n"
            f"Skills: {user_info['skills']}\n\n"
            "Make the content more concise, professional, and impactful."
        )

        # Send the prompt to the Groq API
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",  # Hypothetical model
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("Resume Optimizer AI")

st.write("Enter your resume details below, and this AI will optimize it for you.")

# User input fields
education = st.text_input("Education", "Bachelor of Science in Computer Science, XYZ University, 2022")
experience = st.text_area("Experience", "Software Engineer Intern at ABC Corp, developed a full-stack web application using React and Node.js.")
projects = st.text_area("Projects", "Personal Finance App - A web app to track expenses, built with React and Firebase.")
skills = st.text_input("Skills", "Python, JavaScript, React.js, Node.js, SQL, HTML/CSS")

# Button to optimize resume
if st.button("Optimize Resume"):
    user_info = {
        "education": education,
        "experience": experience,
        "projects": projects,
        "skills": skills
    }

    # Get optimized resume content
    optimized_resume = optimize_resume_content(user_info)

    # Display the optimized resume content
    st.subheader("Optimized Resume Content:")
    st.write(optimized_resume)