# 🤖 Customer Support Chatbot – Task 3

## Internship Task – Future Interns

This repository contains **Task 3** of my Machine Learning Internship at **Future Interns**.

---

## 🔹 Task Objective
Build a smart chatbot to handle **real-time customer support queries** using AI tools with:
- FAQ handling
- Intelligent fallback responses
- Web-based deployment

---

## 🔹 Tools & Technologies Used
- **Python**
- **Streamlit** – Web application
- **OpenAI GPT** – Smart fallback responses
- **Pandas** – Dataset handling
- **Kaggle Customer Support Twitter Dataset**
- **NLP (Text Similarity Matching)**

---

## 🔹 Dataset
- **Customer Support Conversations (Twitter)**
- Source: Kaggle
- File: `customer_support_twitter.csv`

---

## 🔹 Features
✔ Real-time chatbot interface  
✔ FAQ-based responses using dataset  
✔ AI-powered fallback for unseen queries  
✔ Multi-turn conversation support  
✔ Deployed as a Streamlit web app  

---

## 🔹 Project Structure
FUTURE_ML_03/ │ ├── app.py ├── customer_support_twitter.csv ├── requirements.txt ├── README.md └── .gitignore
---
2️⃣ Install Dependencies
Copy code
Bash
pip install -r requirements.txt
3️⃣ Add OpenAI API Key
Create a .env file:
Copy code
Env
OPENAI_API_KEY=your_api_key_here
4️⃣ Run Application
Copy code
Bash
streamlit run app.py
## 🔹 How to Run the Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/FUTURE_ML_03.git
cd FUTURE_ML_03
🔹 Output
A fully functional Customer Support Chatbot capable of:
Handling common support queries
Providing intelligent AI-based responses
Running in real-time via a web interface
