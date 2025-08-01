import streamlit as st
import json
from openai import OpenAI

# Load resume data
with open("resume.json", "r") as f:
    resume_data = json.load(f)

# Format resume context
resume_context = json.dumps(resume_data, indent=2)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="Jainam Patel - Resume Chatbot 🤖", layout="centered")
st.title("🧠 Resume Chatbot")
st.write("Ask me anything about Jainam Patel's resume!")

# User input
user_input = st.text_input("Your question:")

# Chat logic
if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Answer based only on this resume:\n{resume_context}"},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.success(answer)
