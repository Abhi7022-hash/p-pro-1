from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/feedback", methods=["GET"])
def get_feedback():
    data = load_data()
    return jsonify(data)

@app.route("/api/feedback", methods=["POST"])
def add_feedback():
    new_feedback = request.json
    data = load_data()
    data.append(new_feedback)
    save_data(data)
    return jsonify({"message": "Feedback saved successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

