function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessage = document.createElement("p");
    userMessage.className = "user-message";
    userMessage.textContent = "You: " + userInput;
    chatbox.appendChild(userMessage);

    // Send message to chatbot backend
    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("p");
        botMessage.className = "bot-message";
        botMessage.textContent = "Jayden AI: " + data.response;
        chatbox.appendChild(botMessage);

        // Scroll to bottom
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    // Clear input
    document.getElementById("userInput").value = "";
}
