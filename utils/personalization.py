def extract_preferences(user_input):

    preferences = {}

    text = user_input.lower()

    # Extract name
    if "my name is" in text:

        name = text.split("my name is")[-1].strip()

        preferences["name"] = name.title()

    # Extract interests
    if "i like" in text:

        interest = text.split("i like")[-1].strip()

        preferences["interest"] = interest

    if "i am interested in" in text:

        interest = text.split("i am interested in")[-1].strip()

        preferences["interest"] = interest

    return preferences