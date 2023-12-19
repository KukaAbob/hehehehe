document.addEventListener("DOMContentLoaded", function () {
    const welcomeMessage = "Добро пожаловать!";
    displayMessage("Система", welcomeMessage);

    const chatList = document.querySelector(".chat-list");

    chatList.addEventListener("click", function (event) {
        const chatElement = event.target.closest(".chat");
        if (chatElement) {
            const chatName = chatElement.dataset.chatName;
            const chatAvatar = chatElement.querySelector("img").src;

            if (chatName === "Техподдержка") {
                createSupportChat();
            } else if (chatName === "Тестовый Чат") {
                createTestChat();
            } else {
                console.log("Выбран чат:", chatName);
                console.log("Аватар чата:", chatAvatar);
            }
        }
    });

    const sendMessageBtn = document.getElementById("sendMessageBtn");
    const messageInput = document.getElementById("messageInput");

    sendMessageBtn.addEventListener("click", sendMessage);

    messageInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const messageText = messageInput.value;
        if (messageText.trim() !== "") {
            displayMessage("Пользователь", messageText);
            messageInput.value = "";
        }
    }

    function createSupportChat() {
        const messagesContainer = document.querySelector(".messages");
        messagesContainer.innerHTML = '';

        displayMessage("Техподдержка", "Добро пожаловать в наш веб-сайт! Как мы можем вам помочь?");
        displayMessage("Техподдержка", "Наш веб-сайт предоставляет различные услуги и продукты. Если у вас есть вопросы, не стесняйтесь спрашивать!");

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function createTestChat() {
        const messagesContainer = document.querySelector(".messages");
        messagesContainer.innerHTML = '';

        displayMessage("Тестовый Чат", "Добро пожаловать в тестовый чат! Здесь вы можете проводить различные тесты и эксперименты.");

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
});

function displayMessage(sender, text) {
    const messagesContainer = document.querySelector(".messages");
    const messageElement = document.createElement("div");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${text}`;
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
