import streamlit as st

# Simple login system
def login():
    # Logo at the top
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://i.imgur.com/BeJsyd2.png" alt="Guide to IIT Logo" style="width: 150px; border-radius: 10px;">
    </div>
    """, unsafe_allow_html=True)
    
    # Title below the logo
    st.title("Guide to IIT 🔒")
    
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "student" and password == "physics123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong credentials ❌")

# Dashboard with chapters (FIXED: Only one dashboard function)
def dashboard():
    st.title("Dashboard 📚")
    chapters = ["Kinematics", "Newton’s Laws", "Vectors", "Work and Energy"]
    selected = st.selectbox("Choose a chapter", chapters)
    
    if st.button("Open Chapter"):
        st.session_state.current_chapter = selected
        st.rerun()
    
    # Progress tracker (example)
    st.progress(30)
    st.write("Progress: 30% completed")

# Chapter page with video and quiz
def chapter_page():
    st.title(f"Chapter: {st.session_state.current_chapter} 📐")
    
    # Back button
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.current_chapter = None
        st.rerun()

    # Show different content based on selected chapter
    if st.session_state.current_chapter == "Vectors":
        # Vectors chapter with your video
        st.markdown("""
        <div style="max-width: 640px; margin: 0 auto">
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
                <iframe 
                    src="https://guidetoiit-my.sharepoint.com/personal/atmandeshmane_guidetoiit_onmicrosoft_com/_layouts/15/embed.aspx?UniqueId=efa9e677-eb35-407d-865d-26d36b4bd919&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                    width="640" 
                    height="360" 
                    frameborder="0" 
                    scrolling="no" 
                    allowfullscreen 
                    title="Vectors Video" 
                    style="border:none; position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                </iframe>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # Default video for other chapters
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Download notes
    st.download_button("Download Notes 📄", data="Content here", 
                      file_name=f"{st.session_state.current_chapter}_notes.pdf")

    # Quiz button
    if st.button("Start Quiz ➡️"):
        st.session_state.quiz_started = True
        st.rerun()

# Quiz logic (FIXED: Added proper quiz implementation)
def quiz():
    st.title("Quiz 🧠")
    
    # Back button at the top
    if st.button("⬅️ Back to Chapter"):
        st.session_state.quiz_started = False
        st.rerun()
    
    # Quiz questions and logic
    questions = [
        {
            "question": "What is the formula for velocity?",
            "options": ["v = d/t", "v = a*t", "v = m*a"],
            "answer": "v = d/t"
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q['question']}")
        user_answer = st.radio("Options", q["options"], key=i)
        if user_answer == q["answer"]:
            score += 1
    
    st.success(f"Your score: {score}/{len(questions)}")

# Main app flow
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_chapter" not in st.session_state:
        st.session_state.current_chapter = None
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    
    if not st.session_state.logged_in:
        login()
    elif st.session_state.quiz_started:
        quiz()
    elif st.session_state.current_chapter:
        chapter_page()
    else:
        dashboard()

if __name__ == "__main__":
    main()