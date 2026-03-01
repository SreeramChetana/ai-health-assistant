# 🩺 HEALTHCARE MONITORING AI AGENT DEVELOPMENT PROJECT 

An AI-powered personal health assistant that helps users manage medications, track basic health metrics, and get reliable medical guidance through an intelligent chatbot.

Built as part of a Digital Health & Wellness project.

---

## 🚀 Features

* 💊 Medication reminder and scheduling
* 🤖 AI health chatbot (Gemini-powered)
* 📊 Basic health data tracking
* 🗄️ SQLite health metrics database
* 🖥️ Interactive Streamlit dashboard
* 🔒 Secure API key handling

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **SQLite**
* **Google Gemini API**
* **pandas**
* **LangChain (optional ready)**

---

## 📁 Project Structure

```
ai-health-assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── modules/
│   ├── health_chatbot.py
│   ├── medication_manager.py
│   └── database.py
│
└── data/
    └── health.db
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-health-assistant.git
cd ai-health-assistant
```

---

### 2️⃣ Create virtual environment

```
python -m venv .venv
```

Activate:

**Windows**

```
.venv\Scripts\activate
```

**Mac/Linux**

```
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add your Gemini API key

Create a `.env` file in the root:

```
GEMINI_API_KEY=your_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

### 5️⃣ Run the app

```
streamlit run app.py
```

App will open in your browser.

---

## 🧪 Example Use Cases

* Track daily medications
* Get health information via chatbot
* Monitor simple fitness metrics
* Maintain personal health records

---

## 🔐 Privacy & Safety

* API keys stored using environment variables
* Local SQLite database for user data
* No sensitive data is shared externally
* Educational/demo purposes only

---

## 🚧 Future Improvements

* Google Fit integration
* Nutrition tracking
* Advanced health analytics
* Email/SMS medication alerts
* Multi-user login system

---

## 👩‍💻 Author

**Chetana Sreeram**

---

## 📌 Project Status

✅ Week 1 Milestone Complete
🔄 More healthcare integrations coming soon

---

## ⚠️ Disclaimer

This project is for educational purposes only and is **not a substitute for professional medical advice**.
