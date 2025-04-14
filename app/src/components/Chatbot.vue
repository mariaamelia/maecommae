<template>
    <transition name="fade">
      <div class="chatbot-box" v-if="visible">
        <div class="header">
          <strong>Chatbot do Maecommae 🤖</strong>
          <div class="header-buttons">
            <button @click="clearConversation" title="Limpar Conversa">🧹</button>
            <button @click="downloadConversation" title="Salvar Conversa">💾</button>
            <button @click="$emit('close')" title="Fechar">❌</button>
          </div>
        </div>
        <div class="chat-window" ref="chatWindow">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            :class="['chat-message', msg.sender === 'Você' ? 'user' : 'bot']"
          >
            <div class="message-bubble">
              <strong>{{ msg.sender }}:</strong> {{ msg.text }}
            </div>
          </div>
          <div v-if="loading" class="loading">
            <em>Respondendo...</em>
          </div>
        </div>
        <form @submit.prevent="sendMessage" class="chat-input">
          <input v-model="input" placeholder="Digite sua pergunta..." />
          <button type="submit">Enviar</button>
        </form>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { ref, onMounted, nextTick } from 'vue'
  import axios from 'axios'
  
  const input = ref('')
  const messages = ref([])
  const loading = ref(false)
  const visible = ref(true)
  const chatWindow = ref(null)
  
  axios.defaults.withCredentials = true
  
  async function sendMessage() {
    if (!input.value.trim()) return
  
    messages.value.push({ sender: 'Você', text: input.value })
    loading.value = true
    const userInput = input.value
    input.value = ''
  
    try {
      const res = await axios.post(
        'http://localhost:8000/chatbot/',
        { message: userInput },
        { headers: { 'Content-Type': 'application/json' } }
      )
  
      const responseText = res.data?.response || 'Desculpe, houve um problema na resposta do servidor.'
      messages.value.push({ sender: 'Bot', text: responseText })
    } catch (err) {
      console.error('Erro ao enviar para o chatbot:', err)
      messages.value.push({ sender: 'Bot', text: 'Erro ao conectar ao servidor.' })
    } finally {
      loading.value = false
      await nextTick()
      scrollToBottom()
    }
  }
  
  function scrollToBottom() {
    if (chatWindow.value) {
      chatWindow.value.scrollTop = chatWindow.value.scrollHeight
    }
  }
  
  function clearConversation() {
    messages.value = []
  }
  
  function downloadConversation() {
    const content = messages.value
      .map((msg) => `${msg.sender}: ${msg.text}`)
      .join('\n')
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' })
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = 'conversa.txt'
    link.click()
  }
  </script>
  
  <style scoped>
  .chatbot-box {
    position: fixed;
    bottom: 110px;
    right: 20px;
    width: 320px;
    background: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 0 15px #ccc;
    padding: 10px;
    z-index: 1000;
    display: flex;
    flex-direction: column;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .header-buttons button {
    background: none;
    border: none;
    cursor: pointer;
    margin-left: 5px;
    font-size: 1.2em;
  }
  
  .chat-window {
    flex: 1;
    max-height: 250px;
    overflow-y: auto;
    margin: 10px 0;
    padding-right: 5px;
  }
  
  .chat-message {
    margin-bottom: 10px;
    display: flex;
  }
  
  .chat-message.user {
    justify-content: flex-end;
  }
  
  .chat-message.bot {
    justify-content: flex-start;
  }
  
  .message-bubble {
    max-width: 70%;
    padding: 10px;
    border-radius: 10px;
    background-color: #e0e0e0;
  }
  
  .chat-message.user .message-bubble {
    background-color: #cfe9ff;
  }
  
  .chat-input {
    display: flex;
  }
  
  .chat-input input {
    flex: 1;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  .chat-input button {
    padding: 5px 10px;
    margin-left: 5px;
    border-radius: 5px;
    border: none;
    background-color: #4caf50;
    color: white;
    cursor: pointer;
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  
  .loading {
    font-style: italic;
    color: #555;
  }
  </style>
  