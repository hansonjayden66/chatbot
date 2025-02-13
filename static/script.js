document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("user-input").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

const greetings = ["hi", "hello", "hey", "how are you", "sup", "what's up"];
const randomResponses = [
    "Hey there!", "Hello, I'm glad to talk with you!", "Sup?", "I love you!", "I like you!",
    "How's your day going?", "Nice to see you!", "What’s up?", "Yo!", "It's great to chat with you!",
    "Tell me something interesting!", "Haha, that's funny!", "Wow, really?", "No way!", "That sounds cool!",
    "Oh, I see!", "Let's keep chatting!", "I'm here to talk!", "You're awesome!", "I appreciate you!"
];

function sendMessage() {
    let inputField = document.getElementById("user-input");
    let message = inputField.value.trim().toLowerCase();
    if (message === "") return;

    appendMessage("user", message);
    inputField.value = "";

    // Determine response
    let botResponse;
    if (greetings.some(greet => message.includes(greet))) {
        botResponse = "Great! How are you? ☺";
    } else if (message.includes("?")) {
        botResponse = "I'm not intelligent as you so I don't know lol";
    } else {
        let randomIndex = Math.floor(Math.random() * randomResponses.length);
        botResponse = randomResponses[randomIndex];
    }

    // Simulate a typing delay
    setTimeout(() => {
        appendMessage("bot", botResponse);
    }, 1200);
}

function appendMessage(sender, message) {
    let chatBox = document.getElementById("chat-box");
    let messageElement = document.createElement("div");
    let timestamp = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

    messageElement.classList.add(sender === "bot" ? "bot-message" : "user-message");
    messageElement.innerHTML = `<span class="message-text">${message}</span><span class="timestamp">${timestamp}</span>`;
    chatBox.appendChild(messageElement);

    chatBox.scrollTop = chatBox.scrollHeight;
}
