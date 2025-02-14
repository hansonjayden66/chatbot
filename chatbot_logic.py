import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "Feeling ready to chat!"],
    "your name": ["I'm Jayden AI, your personal assistant!", "You can call me Jayden AI."],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "default": ["I'm not sure how to respond to that.", "Could you rephrase that?", "Hmm... I'm not sure."]
}

def get_chat_response(user_input):
    """Returns a chatbot response based on user input."""
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

