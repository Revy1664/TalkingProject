// get room_name from html code
const room_name = JSON.parse(document.getElementById("room-name").textContent);

// websocket initialization
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + room_name
    + '/'
);

// add message to chat log
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};

// print error to console if it occured
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// focus on message input and use "Enter" button like click on submit
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

// send message from client side to server
document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};