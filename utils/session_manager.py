import json
import os

SESSIONS_FOLDER = "sessions"

# Create sessions folder if missing
os.makedirs(SESSIONS_FOLDER, exist_ok=True)

# -----------------------------------
# SAVE SESSION
# -----------------------------------

def save_session(session_id, session_data):

    file_path = os.path.join(
        SESSIONS_FOLDER,
        f"{session_id}.json"
    )

    with open(file_path, "w") as file:

        json.dump(
            session_data,
            file,
            indent=4
        )

# -----------------------------------
# LOAD ALL SESSIONS
# -----------------------------------

def load_sessions():

    sessions = {}

    for file_name in os.listdir(SESSIONS_FOLDER):

        if file_name.endswith(".json"):

            session_id = file_name.replace(".json", "")

            file_path = os.path.join(
                SESSIONS_FOLDER,
                file_name
            )

            with open(file_path, "r") as file:

                sessions[session_id] = json.load(file)

    return sessions

# -----------------------------------
# DELETE SESSION
# -----------------------------------

def delete_session(session_id):

    file_path = os.path.join(
        SESSIONS_FOLDER,
        f"{session_id}.json"
    )

    if os.path.exists(file_path):

        os.remove(file_path)