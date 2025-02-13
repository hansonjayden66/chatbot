<<<<<<< HEAD
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
=======
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

>>>>>>> 95850a48248e1d54ef7363a4afe0b6e36aeea27d
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
<<<<<<< HEAD
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)


=======
    response_message = f"You said: {user_message}"
    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Ensure Render uses port 10000
>>>>>>> 95850a48248e1d54ef7363a4afe0b6e36aeea27d
