import json
import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents dataset
with open("data/intents.json", "r") as file:
    intents = json.load(file)

# Prepare training data
texts = []
labels = []

for intent, examples in intents.items():
    for example in examples:
        texts.append(example)
        labels.append(intent)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)

model.fit(X, labels)

# Create models directory if not exists
os.makedirs("models", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "models/intent_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model training completed successfully!")
print("intent_model.pkl saved")
print("vectorizer.pkl saved")