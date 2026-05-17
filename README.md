# 🧠 EchoMind AI

Example:
- “Generate notes on NLP”

Outputs:
- Structured text notes
- Downloadable `.txt` file

---

## ✅ Adaptive Image Generation
The assistant generates dynamic visual artwork based on user prompts.

Supported themes include:
- Cyberpunk Cities
- Space/Galaxy Scenes
- Forest Landscapes
- Sunset Art

Example:
- “Draw futuristic AI city”
- “Generate galaxy artwork”

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Development |
| Streamlit | Frontend UI |
| Scikit-learn | ML Intent Classification |
| TF-IDF | Text Vectorization |
| Logistic Regression | Intent Prediction |
| Pillow (PIL) | Image Generation |
| Joblib | Model Saving/Loading |

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
    └── response_engine.py
```
---
⚙️ Setup Instructions
1. Clone Repository
git clone <your-github-repo-link>
cd EchoMind_AI
2. Install Dependencies
pip install -r requirements.txt
3. Train Intent Model
python train_model.py
4. Run Application
streamlit run app.py
---
💡 Example Prompts
General
1. What is machine learning?
2. Explain NLP
Personalization
1. My name is Diya
2. I like AI
File Generation
1. Generate notes on NLP
Image Generation
1. Draw futuristic AI city
2. Generate galaxy artwork
---
🔮 Future Improvements
- LLM Integration
- Voice Interaction
- PDF Generation
- Database Storage
- Real AI Image Models
- Authentication System
- Cloud Deployment
---
👩‍💻 Author

Developed by Diya Manoj