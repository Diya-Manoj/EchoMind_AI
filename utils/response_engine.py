def generate_response(intent, user_preferences):

    user_name = user_preferences.get("name", "")

    user_interest = user_preferences.get("interest", "")

    responses = {

        "greeting":
        f"Hello {user_name}! 👋 How can I assist you today?"
        if user_name else
        "Hello! 👋 How can I assist you today?",

        "general_query":
        f"That's an interesting question! Since you're interested in {user_interest}, this could be useful for you."
        if user_interest else
        "That's an interesting question! Let me help you with that.",

        "personalization":
        "Got it! ✅ I'll remember that preference for future interactions.",

        "image_request":
        "🖼️ Sure! I generated an image based on your request.",

        "file_request":
        "📄 Absolutely! I generated a downloadable file for your request.",

        "goodbye":
        f"Goodbye {user_name}! 👋 Have a great day ahead."
        if user_name else
        "Goodbye! 👋 Have a great day ahead."
    }

    return responses.get(
        intent,
        "I'm not sure how to respond to that yet."
    )