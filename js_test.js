// chat_app/static/chat_app/js/chat.js
document.addEventListener('DOMContentLoaded', function () {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + chatId + '/'
    );

    chatSocket.onopen = function (event) {
        console.log('WebSocket connection opened:', event);
    };

    chatSocket.onmessage = function (event) {
        const message = JSON.parse(event.data).message;
        console.log('Received message:', message);
    };

    chatSocket.onclose = function (event) {
        console.log('WebSocket connection closed:', event);
    };

    // Пример: отправка сообщения
    document.querySelector('#send-button').onclick = function () {
        const messageInputDom = document.querySelector('#message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'text': message  // Изменено с 'message' на 'text'
        }));
        messageInputDom.value = '';
    };
});
