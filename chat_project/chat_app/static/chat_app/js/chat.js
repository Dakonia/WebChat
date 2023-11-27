document.addEventListener('DOMContentLoaded', function () {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + chatId + '/'
    );

    chatSocket.onopen = function (event) {
        console.log('WebSocket connection opened:', event);
    };

    chatSocket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log('Received data from server:', data);

        const sender = data.sender;
        const message = data.message;

        // Создаем новый элемент сообщения
        const messageElement = document.createElement('p');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;

        // Добавляем элемент в контейнер с сообщениями
        const chatMessagesContainer = document.getElementById('chat-messages');
        chatMessagesContainer.appendChild(messageElement);

        // Прокручиваем контейнер вниз, чтобы видеть последнее сообщение
        chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
    };

    chatSocket.onclose = function (event) {
        console.log('WebSocket connection closed:', event);
    };

    // Пример: отправка сообщения
    document.querySelector('#send-button').onclick = function () {
        const messageInputDom = document.querySelector('#message-input');
        const message = messageInputDom.value;
        console.log('Sending message:', message);
        chatSocket.send(JSON.stringify({
            'text': message  // Используйте 'text' вместо 'message', как в вашем receive методе
        }));
        messageInputDom.value = '';
    };
});
