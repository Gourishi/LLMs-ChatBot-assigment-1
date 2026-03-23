# 🤖 AI Smart Product Recommender (RL + Gemini)

## 🚀 Overview

The **AI Smart Product Recommender** is a conversational web application that combines **Generative AI** and **Reinforcement Learning (RL)** to deliver intelligent, personalized product recommendations.

It provides a **ChatGPT-like user experience**, allowing users to interact naturally and receive relevant product suggestions across various categories or even open-ended queries.

---

## 🧠 Key Features

* 💬 **Conversational Chat Interface**
  Modern, ChatGPT-inspired UI for smooth user interaction

* 🌍 **Open-Domain Product Search**
  Uses Gemini AI to recommend products for *any query*

* 🧠 **Reinforcement Learning (RL)**
  Learns from user feedback (👍 / 👎) and improves recommendations over time

* 📊 **Persistent Memory**
  Stores user interactions and product scores using JSON

* 🖼️ **Product Cards with Images**
  Clean visual display for better user experience

* 📈 **Analytics Dashboard**
  View product scores and learning progress

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (ChatGPT-style UI)
* **AI Integration:** Gemini API
* **Storage:** JSON (for RL memory & history)

---

## 🧩 System Architecture

User → Chat Interface → Flask Backend
→ (Category Match → Local DB)
→ (No Match → Gemini AI)
→ Product Suggestions → User Feedback
→ Reward System → Update Scores (RL Learning)

---

## 🔄 How It Works

1. User enters a query (e.g., *“best gaming phone under 30000”*)
2. System:

   * Checks predefined categories OR
   * Uses Gemini AI for smart recommendations
3. Displays product suggestions
4. User gives feedback (👍 / 👎)
5. System updates product scores (reward logic)
6. Future recommendations improve automatically

---

## 🧪 Example Use Cases

* Find the best gadgets within a budget
* Explore product recommendations conversationally
* Personalized shopping assistant
* AI-powered recommendation system demo

---

## 🏆 Hackathon Value

This project demonstrates:

* Hybrid AI architecture (Rule-based + Generative AI)
* Practical implementation of Reinforcement Learning
* Real-world application of conversational AI
* Scalable and extensible system design

---

## 📦 Installation & Setup

```bash
pip install flask google-generativeai
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Note

Replace `"YOUR_API_KEY"` in `app.py` with your Gemini API key.

---

## 🎯 Future Enhancements

* 📊 Advanced analytics dashboard (charts & insights)
* 🛒 E-commerce API integration (Amazon/Flipkart)
* 🔐 User authentication system
* 📱 Mobile responsive UI
* 🎙️ Voice-based interaction

---

## 💡 Conclusion

This project showcases how **AI + Reinforcement Learning + UX design** can be combined to build an intelligent, adaptive, and user-friendly recommendation system.

It goes beyond static recommendations by continuously learning from user interactions, making it a powerful foundation for real-world applications.

---

## 👨‍💻 Author

Built for Hackathon 🚀
