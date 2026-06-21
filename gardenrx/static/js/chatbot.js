// GardenRx AI Traditional Botanical Docent Chatbot
function toggleChatbot() {
    const panel = document.getElementById('chatbot-panel');
    panel.classList.toggle('active');
}

function sendChatMessage() {
    const input = document.getElementById('chatbot-input');
    const message = input.value.trim();
    if (!message) return;

    // Add user message
    addMessage(message, 'user');
    input.value = '';

    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot';
    typingDiv.id = 'typing-indicator';
    typingDiv.innerHTML = '<div class="message-content">생각하는 중...</div>';
    document.getElementById('chatbot-messages').appendChild(typingDiv);

    // Send to server
    fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('typing-indicator').remove();
        addMessage(data.response, 'bot');
    })
    .catch(() => {
        document.getElementById('typing-indicator').remove();
        addMessage('죄송합니다. 일시적인 오류가 발생했습니다. 다시 시도해주세요.', 'bot');
    });
}

function addMessage(text, type) {
    const container = document.getElementById('chatbot-messages');
    const div = document.createElement('div');
    div.className = `message ${type}`;
    div.innerHTML = `<div class="message-content">${text}</div>`;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}