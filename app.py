from flask import Flask, render_template, request, jsonify
from recommender import *
import random
import google.generativeai as genai

# 🔑 Add your Gemini API key here
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

data = init_scores(load_data())

def detect_category(text):
    text = text.lower()
    for cat in products:
        if cat in text:
            return cat
    return None

def get_image(product):
    return f"https://source.unsplash.com/300x200/?{product}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", data=data)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]

    category = detect_category(msg)

    # ✅ Local recommendations
    if category:
        recs = recommend(category, data)
        return jsonify({
            "reply": f"Top {category} products:",
            "products": [{"name": p, "image": get_image(p)} for p in recs]
        })

    # 🔥 Gemini AI recommendations
    prompt = f"""
    Suggest 3 real products for: {msg}
    Include product names only.
    """

    response = model.generate_content(prompt)
    lines = response.text.split("\n")

    products_ai = [line.strip("-•123. ") for line in lines if line.strip()]

    return jsonify({
        "reply": "Here are smart AI suggestions:",
        "products": [{"name": p, "image": get_image(p)} for p in products_ai[:3]]
    })

@app.route("/feedback", methods=["POST"])
def feedback():
    product = request.json["product"]
    action = request.json["action"]

    update_feedback(product, action, data)

    return jsonify({"status": "updated"})

if __name__ == "__main__":
    app.run(debug=True)