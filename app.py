import streamlit as st
import pandas as pd
import difflib
import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------- BASIC UI ----------
st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")
st.title("🤖 Customer Support Chatbot")
st.write("Ask a customer support question below:")

# ---------- LOAD ENV ----------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    df = pd.read_csv("customer_support_twitter.csv", nrows=3000)
    df = df.dropna(subset=["text"])
    return df

with st.spinner("Loading dataset..."):
    df = load_data()

faq_questions = df[df["inbound"] == True]["text"].tolist()

# ---------- FUNCTIONS ----------
def get_faq_response(user_query):
    match = difflib.get_close_matches(
        user_query, faq_questions, n=1, cutoff=0.6
    )
    if match:
        return "Thank you for contacting support. We are looking into this issue."
    return None

def get_gpt_response(user_query):
    if not api_key:
        return "AI service not configured. Please add OpenAI API key."
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a customer support assistant."},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content

# ---------- SESSION ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ---------- SEND MESSAGE ----------
def send_message():
    text = st.session_state.user_input.strip()
    if text == "":
        return

    reply = get_faq_response(text)
    if not reply:
        reply = get_gpt_response(text)

    # Append normally
    st.session_state.chat.append(("You", text))
    st.session_state.chat.append(("Bot", reply))

    # Clear input
    st.session_state.user_input = ""

# ---------- INPUT (ENTER WORKS) ----------
st.text_input(
    "Type your message and press Enter",
    key="user_input",
    on_change=send_message
)

st.divider()

# ---------- CHAT DISPLAY (LATEST ON TOP) ----------
for sender, msg in reversed(st.session_state.chat):
    if sender == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")