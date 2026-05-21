import random


def generate_response(intent, user_preferences, user_input):

    user_name = user_preferences.get("name", "")

    user_interest = user_preferences.get("interest", "")

    user_input = user_input.lower()

    # -----------------------------------
    # GREETING
    # -----------------------------------

    if intent == "greeting":

        responses = [

            f"Hello {user_name}! How can I assist you today?"
            if user_name else
            "Hello! How can I assist you today?",

            "Hey there! What would you like help with today?",

            "Hi! Ready to continue working on your goals?"
        ]

        return random.choice(responses)

    # -----------------------------------
    # GENERAL QUERY
    # -----------------------------------

    elif intent == "general_query":

        if "ai" in user_input:

            return (
                "Artificial Intelligence focuses on building systems capable of learning, reasoning, and decision-making similar to humans."
            )

        elif "python" in user_input:

            return (
                "Python is a powerful high-level programming language commonly used in AI, machine learning, automation, and backend development."
            )

        elif "cloud" in user_input:

            return (
                "Cloud computing allows scalable storage, infrastructure, and services over the internet using platforms such as AWS and Azure."
            )

        else:

            return (
                "That's an interesting topic. Let me help you understand it better."
            )

    # -----------------------------------
    # CODING HELP
    # -----------------------------------

    elif intent == "coding_help":

        if "python" in user_input:

            return (
                "I can help debug Python issues, explain concepts, optimize logic, and improve your implementation structure."
            )

        elif "api" in user_input:

            return (
                "APIs help different software systems communicate. I can help you design, debug, or optimize API workflows."
            )

        elif "sql" in user_input:

            return (
                "SQL optimization usually involves indexing, query restructuring, joins optimization, and minimizing unnecessary scans."
            )

        else:

            return (
                "I can help with debugging, algorithms, optimization, backend logic, and software development concepts."
            )

    # -----------------------------------
    # CAREER GUIDANCE
    # -----------------------------------

    elif intent == "career_guidance":

        return (
            "For AI and software engineering roles, focus on strong projects, DSA, internships, GitHub presence, problem-solving, and consistent technical practice."
        )

    # -----------------------------------
    # STUDY PLANNING
    # -----------------------------------

    elif intent == "study_planning":

        return (
            "An effective study plan should include consistency, revision, project implementation, active recall, and practical problem-solving."
        )

    # -----------------------------------
    # MOTIVATION
    # -----------------------------------

    elif intent == "motivation":

        return (
            "Progress may feel slow sometimes, but consistency compounds over time. Keep building one step at a time 🚀"
        )

    # -----------------------------------
    # SUMMARIZATION
    # -----------------------------------

    elif intent == "summarization":

        return (
            "Here’s a concise summary: the topic mainly focuses on core concepts, practical applications, and real-world implementation strategies."
        )

    # -----------------------------------
    # PERSONALIZATION
    # -----------------------------------

    elif intent == "personalization":

        return (
            "Got it! I'll remember that preference for future interactions."
        )

    # -----------------------------------
    # IMAGE REQUEST
    # -----------------------------------

    elif intent == "image_request":

        return (
            "Sure! I generated an image based on your request."
        )

    # -----------------------------------
    # FILE REQUEST
    # -----------------------------------

    elif intent == "file_request":

        return (
            "Absolutely! I generated a downloadable file for your request."
        )

    # -----------------------------------
    # GOODBYE
    # -----------------------------------

    elif intent == "goodbye":

        return (
            f"Goodbye {user_name}! Have a great day ahead."
            if user_name else
            "Goodbye! Have a great day ahead."
        )

    # -----------------------------------
    # DEFAULT
    # -----------------------------------

    return (
        "I'm not completely sure about that yet, but I'll do my best to help."
    )