<template>
  <div class="p-4 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-4 text-center">Login de Usuárias</h1>


    <div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">

      <div class="fixed inset-0 bg-black opacity-50"></div>

      <div class="bg-white rounded-lg p-6 z-50 w-80">
        <h2 class="text-xl font-bold mb-4 text-center">Login Realizado com Sucesso!</h2>
        <p class="mb-4 text-center">Você efetuou login com sucesso.</p>
        <div class="flex justify-center">
          <button @click="closeModal"
            class="bg-[#E67E80] text-white px-4 py-2 rounded hover:bg-[#d46567] transition-colors">
            Fechar
          </button>
        </div>
      </div>
    </div>


    <div v-if="successMessage" class="text-green-600 font-semibold mb-4">
      {{ successMessage }}
    </div>


    <form @submit.prevent="handleLogin" class="flex flex-col gap-4">

      <div>
        <label for="email" class="block font-medium mb-1">E-mail</label>
        <input v-model="formData.email" type="email" id="email" class="w-full p-2 border border-gray-300 rounded"
          placeholder="exemplo@dominio.com" />
        <span v-if="errors.email" class="text-red-600 text-sm">
          {{ errors.email }}
        </span>
      </div>


      <div>
        <label for="password" class="block font-medium mb-1">Senha</label>
        <div class="relative">
          <input v-model="formData.password" :type="showPassword ? 'text' : 'password'" id="password"
            class="w-full p-2 border border-gray-300 rounded" placeholder="Digite sua senha" />
          <button type="button" @click="showPassword = !showPassword"
            class="absolute right-2 top-1/2 transform -translate-y-1/2 focus:outline-none">

            <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none"
              viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M2.458 12C3.732 7.943 7.522 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.478 0-8.268-2.943-9.542-7z" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.542-7a10.05 10.05 0 012.147-3.392M6.29 6.29A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.542 7a9.953 9.953 0 01-1.257 2.043M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3l18 18" />
            </svg>
          </button>
        </div>
        <span v-if="errors.password" class="text-red-600 text-sm">
          {{ errors.password }}
        </span>
      </div>

      <div class="flex justify-center mt-6">
        <button type="submit"
          class="bg-[#E67E80] text-white px-6 py-2 rounded-md text-sm font-semibold hover:bg-[#d46567] transition-colors">
          Entrar
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import emitter from '@/eventBus'

const router = useRouter()


const formData = ref({
  email: '',
  password: ''
})


const errors = ref({})
const successMessage = ref('')
const showModal = ref(false)


const showPassword = ref(false)


const handleLogin = async () => {
  try {

    await axios.get("http://127.0.0.1:8000/csrf-cookie/", {
      withCredentials: true
    });


    const response = await axios.post('http://127.0.0.1:8000/login/', formData.value, {
      headers: { 'Content-Type': 'application/json' },
      withCredentials: true
    });


    localStorage.setItem("user", response.data.user);

    emitter.emit("user:logged", response.data.user)


    successMessage.value = 'Login realizado com sucesso!'
    errors.value = {}
    showModal.value = true
  } catch (error) {
    if (error.response && error.response.data && error.response.data.errors) {
      errors.value = error.response.data.errors
    } else {
      console.error(error)
      alert('Ocorreu um erro ao tentar fazer login. Verifique o console.')
    }
  }
}



const closeModal = () => {
  showModal.value = false
  router.push('/')
}
</script>

<style scoped></style>