import joblib

# Load trained model and vectorizer
model = joblib.load("models/intent_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_intent(user_input):

    text = user_input.lower()

    # Rule-based overrides
    personalization_keywords = [
        "my name is",
        "i like",
        "remember",
        "save my",
        "don't forget",
        "dont forget",
        "i am interested in",
        "keep in mind"
    ]

    for keyword in personalization_keywords:
        if keyword in text:
            return "personalization"

    # ML prediction
    input_vector = vectorizer.transform([user_input])

    prediction = model.predict(input_vector)[0]

    return prediction