
import streamlit as st
from google.colab import userdata
import google.generativeai as genai


# Configure Gemini API
genai.configure(api_key="AQ.Ab8RN6Lr083gFFyEStb-9OPxYVD6GY0eVRtitqfpFbt_kMvXIg")

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit Page Configuration
st.set_page_config(
    page_title="Sania AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Sania AI Learning Buddy")
st.write("Learn any topic with AI!")

# User Input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    (
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    )
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
            Explain {topic} in simple language for a beginner.

            Include:
            - Definition
            - Key points
            - One real-life example
            """

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"""
            Create 5 multiple-choice questions on {topic}.

            Each question should have:
            A)
            B)
            C)
            D)

            Mention the correct answer after each question.
            """

        else:
            prompt = topic

        try:
            response = model.generate_content(prompt)
            st.success("Generated Successfully!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
