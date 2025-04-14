<template>
  <div class="p-4 max-w-xl mx-auto flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Encerrando Sessão...</h1>
    <p>Por favor, aguarde enquanto efetuamos o logout.</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const performLogout = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/logout/', {}, {
      headers: { 'Content-Type': 'application/json' }
    })
    // Após efetuar o logout, redireciona para a página de login
    router.push('/')
  } catch (error) {
    console.error(error)
    alert('Ocorreu um erro ao tentar fazer logout. Verifique o console.')
  }
}

onMounted(() => {
  performLogout()
})
</script>

<style scoped>
/* Adicione estilos conforme necessário */
</style>
