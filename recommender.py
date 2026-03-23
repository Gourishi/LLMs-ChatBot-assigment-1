import json
import os

DATA_FILE = "data.json"

products = {
    "gaming": ["Asus ROG Phone", "iQOO Neo", "OnePlus 11"],
    "budget": ["Redmi Note", "Realme Narzo", "Poco X series"],
    "camera": ["iPhone 14", "Samsung S23", "Google Pixel"],
    "laptop": ["MacBook Air", "Dell XPS", "HP Pavilion"]
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {"scores": {}, "history": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def init_scores(data):
    for cat in products:
        for item in products[cat]:
            if item not in data["scores"]:
                data["scores"][item] = 0
    save_data(data)
    return data

def recommend(category, data):
    items = products[category]
    return sorted(items, key=lambda x: data["scores"][x], reverse=True)[:3]

def update_feedback(product, action, data):
    if product not in data["scores"]:
        data["scores"][product] = 0

    if action == "like":
        data["scores"][product] += 10
    else:
        data["scores"][product] -= 5

    data["history"].append({"product": product, "action": action})
    save_data(data)