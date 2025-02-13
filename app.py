from flask import Flask, request, jsonify, send_from_directory, render_template
import random

app = Flask(__name__, static_folder="static", static_url_path="")

# Chatbot responses (Version 2.0 - Improved AI logic)
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi there! What brings you here?"],
    "how are you": ["I'm an AI, but I'm here to help!", "I'm always ready to assist you!"],
    "bye": ["Goodbye! Take care!", "See you next time! Have a great day!"],
    "default": ["I'm not sure I understand. Could you rephrase that?"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
