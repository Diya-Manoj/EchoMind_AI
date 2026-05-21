# 🧠 EchoMind AI

EchoMind AI is a Personalized Multi-Session AI Assistant built using Machine Learning, NLP, and Streamlit.

The system supports:
- Intent Detection
- Contextual Conversations
- Personalized Memory
- Multi-Session Chat Management
- Dynamic File Generation
- Adaptive Image Generation
- Context-Aware Response Engine

---

# 🚀 Features

## ✅ Intent Detection

The chatbot uses:
- TF-IDF Vectorization
- Logistic Regression Classification

to detect user intent dynamically.

Supported intents include:
- Greeting
- General Query
- Personalization
- Coding Help
- Career Guidance
- Study Planning
- Motivation
- Summarization
- File Request
- Image Request
- Goodbye

---

## ✅ Personalized Conversations

The assistant remembers:
- User names
- Interests
- Preferences
- Conversation context

Example:
- “My name is Diya”
- “I like Machine Learning”

---

## ✅ Multi-Session Chat Support

Users can:
- Create multiple chat sessions
- Switch between sessions
- Delete sessions
- Preserve chat history

Each session maintains independent conversational context.

---

## ✅ Dynamic File Generation

The assistant can generate downloadable notes dynamically.

Example:
- “Generate notes on NLP”

Outputs:
- Structured text notes
- Downloadable `.txt` file

---

## ✅ Adaptive Image Generation

The assistant generates visual artwork dynamically based on user prompts.

Supported themes include:
- Cyberpunk Cities
- Galaxy/Space Scenes
- Forest Landscapes
- Sunset Artwork
- AI Futuristic Concepts

Example:
- “Draw futuristic AI city”
- “Generate galaxy artwork”

---

## ✅ Context-Aware Response Engine

The chatbot dynamically adapts responses based on:
- detected intent
- user input
- personalization context
- conversational flow

This creates an LLM-inspired response workflow architecture.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Development |
| Streamlit | Frontend UI |
| Scikit-learn | ML Intent Classification |
| TF-IDF Vectorizer | Text Feature Extraction |
| Logistic Regression | Intent Prediction |
| Pillow (PIL) | Dynamic Image Generation |
| Joblib | Model Persistence |
| JSON | Session Storage |

---

# 📂 Project Structure

```bash
EchoMind_AI/
│
├── app.py
├── requirements.txt
├── README.md
├── documentation.md
├── train_model.py
│
├── data/
│   └── intents.json
│
├── generated_files/
├── generated_images/
├── models/
│
├── sessions/
│
└── utils/
    ├── file_generator.py
    ├── image_generator.py
    ├── intent_detector.py
    ├── personalization.py
    ├── response_engine.py
    └── session_manager.py
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd EchoMind_AI
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Train Intent Detection Model

```bash
python train_model.py
```

---

## 4️⃣ Run Application

```bash
streamlit run app.py
```

---

# 💡 Example Prompts

## General Queries
- What is machine learning?
- Explain NLP
- What is cloud computing?

---

## Coding Help
- Help debug my Python API
- Explain recursion
- Optimize this SQL query

---

## Career Guidance
- How do I prepare for AI interviews?
- Resume tips for freshers
- Best skills for ML engineers

---

## Study Planning
- Make a machine learning roadmap
- Create a study plan for NLP

---

## Motivation
- Motivate me
- I feel burned out from studying

---

## Summarization
- Summarize cloud computing
- Quick notes on transformers

---

## Personalization
- My name is Diya
- I like AI and Machine Learning

---

## File Generation
- Generate notes on NLP
- Create study notes on AI

---

## Image Generation
- Draw futuristic AI city
- Generate sunset artwork
- Create galaxy illustration

---

# 🔮 Future Improvements

- LLM API Integration
- Voice Interaction
- PDF Generation
- Database Integration
- Authentication System
- Advanced AI Image Models
- Cloud Database Storage
- HuggingFace/Local LLM Support

---

# 🌐 Deployment

The application can be deployed using:
- Streamlit Cloud
- GitHub Integration

---

# 👩‍💻 Author

Developed by Diya Manoj