window.onload = function() {
    try {
        const chatLog = document.getElementById('chat-log');
        if (chatLog) {
            chatLog.scrollTop = chatLog.scrollHeight;
        } else {
            console.error("Chat log element not found.");
        }
    } catch (error) {
        console.error("Error setting scroll position:", error);
    }
};

var groupName = JSON.parse(document.getElementById('group-name').textContent)
var groupType = JSON.parse(document.getElementById('group-type').textContent)

var protocol = 'ws://'
if (window.location.protocol == 'https:') {
    protocol = 'wss://'
}
var ws = new WebSocket(
    protocol + window.location.host + '/ws/ajwc/' + groupType + '/' + groupName + '/'
)

ws.onopen = function() {
    console.log("WebSocket Connection open...");
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const chatLog = document.querySelector('#chat-log');
    chatLog.value += `${data.user}: ${data.msg}    \n\n    `;

    // Scroll to the bottom after a short delay
    setTimeout(() => {
        chatLog.scrollTop = chatLog.scrollHeight;
    }, 10); // 10 ms delay
};

ws.onclose = function(event) {
    console.log(event);
    console.error('Chat Socket Closed Unexpectedly...');
};

document.getElementById('chat-message-submit').onclick = function(event) {
    const messageInputDom = document.getElementById('chat-message-input')
    const message = messageInputDom.value
    ws.send(JSON.stringify({    // converting object to string.
        'msg': message
    }))
    messageInputDom.value = ''

    // Automatically scroll to the bottom
    const chatLog = document.getElementById('chat-log'); // Get the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}