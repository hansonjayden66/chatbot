from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    return jsonify({"response": "Hello! This is your chatbot."})

if __name__ == "__main__":
    app.run(debug=True)
