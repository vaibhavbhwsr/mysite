var groupName = JSON.parse(document.getElementById('group-name').textContent)

var ws = new WebSocket(
    'ws://' + window.location.host + '/ws/ajwc/' + groupName + '/'
)

ws.onopen = function() {
    console.log("WebSocket Connection open...");
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data)
    document.querySelector('#chat-log').value += (data.user + ': ' + data.msg + '    \n\n    ')
};

ws.onclose = function(event) {
    console.error('Chat Socket Closed Unexpectedly...');
};

document.getElementById('chat-message-submit').onclick = function(event) {
    const messageInputDom = document.getElementById('chat-message-input')
    const message = messageInputDom.value
    ws.send(JSON.stringify({    // converting object to string.
        'msg': message
    }))
    messageInputDom.value = ''
}