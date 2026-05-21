import streamlit as st
import uuid
from utils.response_engine import generate_response
from utils.image_generator import generate_image
from utils.personalization import extract_preferences
from utils.intent_detector import predict_intent
from utils.file_generator import generate_text_file
from utils.session_manager import (
    save_session,
    load_sessions,
    delete_session
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="EchoMind AI",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------

if "sessions" not in st.session_state:

    loaded_sessions = load_sessions()

    st.session_state.sessions = (
        loaded_sessions
        if loaded_sessions
        else {}
    )

if "preferences" not in st.session_state:
    st.session_state.preferences = {}

# Create first session if none exist
if not st.session_state.sessions:

    session_id = str(uuid.uuid4())[:8]

    st.session_state.sessions[session_id] = {
        "title": "New Chat",
        "messages": [],
        "generated_file": None
    }

    st.session_state.current_session = session_id

# Ensure current session exists
if "current_session" not in st.session_state:

    st.session_state.current_session = list(
        st.session_state.sessions.keys()
    )[0]

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("💬 Chat Sessions")

# -----------------------------------
# NEW CHAT
# -----------------------------------

if st.sidebar.button("➕ New Chat"):

    new_session_id = str(uuid.uuid4())[:8]

    st.session_state.sessions[new_session_id] = {
        "title": "New Chat",
        "messages": [],
        "generated_file": None
    }

    st.session_state.current_session = new_session_id

    save_session(
        new_session_id,
        st.session_state.sessions[new_session_id]
    )

    st.rerun()

# -----------------------------------
# SESSION TITLES
# -----------------------------------

session_titles = {
    session_id: session_data["title"]
    for session_id, session_data
    in st.session_state.sessions.items()
}

# -----------------------------------
# SESSION SELECTOR
# -----------------------------------

session_keys = list(session_titles.keys())

selected_index = session_keys.index(
    st.session_state.current_session
)

selected_session = st.sidebar.radio(
    "Select Session",
    session_keys,
    index=selected_index,
    format_func=lambda x: session_titles[x]
)

if selected_session != st.session_state.current_session:

    st.session_state.current_session = selected_session

    st.rerun()
# -----------------------------------
# DELETE SESSION
# -----------------------------------

if st.sidebar.button("🗑️ Delete Current Session"):

    if len(st.session_state.sessions) > 1:

        delete_session(
            st.session_state.current_session
        )

        del st.session_state.sessions[
            st.session_state.current_session
        ]

        st.session_state.current_session = list(
            st.session_state.sessions.keys()
        )[0]

        st.rerun()

# -----------------------------------
# MAIN TITLE
# -----------------------------------

st.title("🧠 EchoMind AI")
st.subheader("Personalized Multi-Session AI Assistant")

# -----------------------------------
# CURRENT CHAT
# -----------------------------------

current_session_data = st.session_state.sessions[
    st.session_state.current_session
]

current_chat = current_session_data["messages"]

# -----------------------------------
# DISPLAY CHAT HISTORY
# -----------------------------------

for chat in current_chat:

    with st.chat_message(chat["role"]):

        # Text Messages
        if "message" in chat:
            st.markdown(chat["message"])

        # Image Messages
        if "image" in chat:
            try:
                st.image(
                    chat["image"],
                    caption="AI Generated Image",
                    use_container_width=True
                )
            except:
                st.warning(
                    "Image could not be loaded."
                )

# -----------------------------------
# DISPLAY GENERATED FILE
# -----------------------------------

if current_session_data["generated_file"]:

    with open(
        current_session_data["generated_file"],
        "rb"
    ) as file:

        st.download_button(
            label="📄 Download Generated File",
            data=file,
            file_name="generated_notes.txt",
            mime="text/plain"
        )

# -----------------------------------
# USER INPUT
# -----------------------------------

user_input = st.chat_input("Type your message here...")

if user_input:

    current_session_id = st.session_state.current_session

    current_session_data = st.session_state.sessions[
        current_session_id
    ]

    # -----------------------------------
    # AUTO SESSION TITLE
    # -----------------------------------

    if current_session_data["title"] == "New Chat":

        generated_title = (
            user_input[:30] + "..."
            if len(user_input) > 30
            else user_input
        )

        current_session_data["title"] = generated_title

    # -----------------------------------
    # PERSONALIZATION EXTRACTION
    # -----------------------------------

    extracted_data = extract_preferences(user_input)

    if current_session_id not in st.session_state.preferences:

        st.session_state.preferences[current_session_id] = {}

    st.session_state.preferences[current_session_id].update(
        extracted_data
    )

    # -----------------------------------
    # INTENT DETECTION
    # -----------------------------------

    intent = predict_intent(user_input)

    # -----------------------------------
    # RESPONSE GENERATION
    # -----------------------------------

    user_preferences = st.session_state.preferences.get(
        current_session_id,
        {}
    )

    bot_response = generate_response(
        intent,
        user_preferences,
        user_input
    )
    
    # Reset generated file
    current_session_data["generated_file"] = None

    # -----------------------------------
    # STORE USER MESSAGE
    # -----------------------------------

    current_chat.append({
        "role": "user",
        "message": user_input
    })

    # -----------------------------------
    # STORE ASSISTANT RESPONSE
    # -----------------------------------

    current_chat.append({
        "role": "assistant",
        "message": bot_response
    })

    # -----------------------------------
    # IMAGE GENERATION
    # -----------------------------------

    if intent == "image_request":

        generated_image_path = generate_image(user_input)

        current_chat.append({
            "role": "assistant",
            "image": generated_image_path
        })

    # -----------------------------------
    # FILE GENERATION
    # -----------------------------------

    if intent == "file_request":

        topic = user_input.strip()

        topic_display = (
            topic.upper()
            if len(topic) <= 5
            else topic.title()
        )

        file_content = f"""
===============================
      EchoMind AI Notes
===============================

Topic: {topic_display}

--------------------------------
Introduction
--------------------------------

{topic_display} is an important concept in Artificial Intelligence and Computer Science.

It is widely used in modern intelligent systems and applications.

--------------------------------
Key Concepts
--------------------------------

1. Data Processing
2. Pattern Recognition
3. Machine Learning Integration
4. Real-world Applications
5. Automation and Optimization

--------------------------------
Applications
--------------------------------

- Chatbots
- Recommendation Systems
- Predictive Analytics
- AI Assistants
- Automation Platforms

--------------------------------
Conclusion
--------------------------------

{topic_display} plays a major role in modern AI-driven technologies and continues to evolve rapidly.

--------------------------------
Generated By:
EchoMind AI Assistant
--------------------------------
"""

        current_session_data["generated_file"] = generate_text_file(
            file_content,
            "generated_notes.txt"
        )

    # -----------------------------------
    # SAVE SESSION
    # -----------------------------------

    save_session(
        current_session_id,
        current_session_data
    )

    st.rerun()