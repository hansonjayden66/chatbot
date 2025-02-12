from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
    response_message = f"You said: {user_message}"
    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Ensure Render uses port 10000
