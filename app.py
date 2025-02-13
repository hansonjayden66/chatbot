from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Chatbot responses (Basic AI logic)
responses = {
    "hello": ["Hello! How can I assist you?", "Hi there! How's your day going?"],
    "how are you": ["I'm just a chatbot, but I'm doing great!", "I'm here to help!"],
    "bye": ["Goodbye! Have a great day!", "See you next time!"],
    "default": ["I'm not sure I understand. Can you rephrase?"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Home Route (Loads the Chat UI)
@app.route("/")
def home():
    return render_template("index.html")  # Loads UI (Make sure index.html exists)

# Chatbot API Route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)


