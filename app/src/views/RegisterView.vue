<template>
    <div class="p-4 max-w-xl mx-auto">
      <h1 class="text-2xl font-bold mb-4 text-center">Cadastro de Usuárias</h1>
  
      <!-- Modal de Sucesso -->
      <div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">
        <!-- Fundo semi-transparente -->
        <div class="fixed inset-0 bg-black opacity-50"></div>
        <!-- Caixa do Modal -->
        <div class="bg-white rounded-lg p-6 z-50 w-80">
          <h2 class="text-xl font-bold mb-4 text-center">Cadastro com Sucesso!</h2>
          <p class="mb-4 text-center">Seu cadastro foi realizado com sucesso.</p>
          <div class="flex justify-center">
            <button @click="closeModal" class="bg-[#E67E80] text-white px-4 py-2 rounded hover:bg-[#d46567] transition-colors">
              Fechar
            </button>
          </div>
        </div>
      </div>
  
      <!-- Exibição de mensagem de sucesso global (caso necessário) -->
      <div v-if="successMessage" class="text-green-600 font-semibold mb-4">
        {{ successMessage }}
      </div>
  
      <!-- Formulário -->
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
        <!-- Nome de Usuária -->
        <div>
          <label for="username" class="block font-medium mb-1">Nome de Usuária</label>
          <input
            v-model="formData.username"
            type="text"
            id="username"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="Ex: Maria2025"
          />
          <span v-if="errors.username" class="text-red-600 text-sm">
            {{ errors.username }}
          </span>
        </div>
  
        <!-- E-mail -->
        <div>
          <label for="email" class="block font-medium mb-1">E-mail</label>
          <input
            v-model="formData.email"
            type="email"
            id="email"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="exemplo@dominio.com"
          />
          <span v-if="errors.email" class="text-red-600 text-sm">
            {{ errors.email }}
          </span>
        </div>
  
        <!-- Senha e Repetir Senha com botão de mostrar/ocultar -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Senha -->
          <div>
            <label for="password1" class="block font-medium mb-1">Senha</label>
            <div class="relative">
              <input
                v-model="formData.password1"
                :type="showPassword1 ? 'text' : 'password'"
                id="password1"
                class="w-full p-2 border border-gray-300 rounded"
              />
              <button
                type="button"
                @click="showPassword1 = !showPassword1"
                class="absolute right-2 top-1/2 transform -translate-y-1/2 focus:outline-none"
              >
                <svg
                  v-if="!showPassword1"
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.522 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.478 0-8.268-2.943-9.542-7z"
                  />
                </svg>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.542-7a10.05 10.05 0 012.147-3.392M6.29 6.29A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.542 7a9.953 9.953 0 01-1.257 2.043M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 3l18 18"
                  />
                </svg>
              </button>
            </div>
            <span v-if="errors.password1" class="text-red-600 text-sm">
              {{ errors.password1 }}
            </span>
          </div>
  
          <!-- Repetir Senha -->
          <div>
            <label for="password2" class="block font-medium mb-1">Repetir Senha</label>
            <div class="relative">
              <input
                v-model="formData.password2"
                :type="showPassword2 ? 'text' : 'password'"
                id="password2"
                class="w-full p-2 border border-gray-300 rounded"
              />
              <button
                type="button"
                @click="showPassword2 = !showPassword2"
                class="absolute right-2 top-1/2 transform -translate-y-1/2 focus:outline-none"
              >
                <svg
                  v-if="!showPassword2"
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.522 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.478 0-8.268-2.943-9.542-7z"
                  />
                </svg>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.542-7a10.05 10.05 0 012.147-3.392M6.29 6.29A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.542 7a9.953 9.953 0 01-1.257 2.043M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 3l18 18"
                  />
                </svg>
              </button>
            </div>
            <span v-if="errors.password2" class="text-red-600 text-sm">
              {{ errors.password2 }}
            </span>
          </div>
        </div>
  
        <!-- Data de Nascimento -->
        <div>
          <label for="birth_date" class="block font-medium mb-1">Data de Nascimento</label>
          <input
            v-model="formData.birth_date"
            type="date"
            id="birth_date"
            class="w-full p-2 border border-gray-300 rounded"
          />
          <span v-if="errors.birth_date" class="text-red-600 text-sm">
            {{ errors.birth_date }}
          </span>
        </div>
  
        <!-- CEP com integração à API (ação em blur, enter e botão de busca) -->
        <div>
          <label for="cep" class="block font-medium mb-1">CEP</label>
          <div class="relative">
            <input
              v-model="formData.cep"
              type="text"
              id="cep"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="Ex: 12345-678"
              @blur="fetchCep"
              @keyup.enter="fetchCep"
            />
            <button
              type="button"
              @click="fetchCep"
              class="absolute right-2 top-1/2 transform -translate-y-1/2 focus:outline-none"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </button>
          </div>
          <span v-if="errors.cep" class="text-red-600 text-sm">
            {{ errors.cep }}
          </span>
        </div>
  
        <!-- Rua, Número e Bairro -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label for="street" class="block font-medium mb-1">Rua</label>
            <input
              v-model="formData.street"
              type="text"
              id="street"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="Ex: Av. Principal"
            />
            <span v-if="errors.street" class="text-red-600 text-sm">
              {{ errors.street }}
            </span>
          </div>
          <div>
            <label for="house_number" class="block font-medium mb-1">Número</label>
            <input
              v-model="formData.house_number"
              type="text"
              id="house_number"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="123"
            />
            <span v-if="errors.house_number" class="text-red-600 text-sm">
              {{ errors.house_number }}
            </span>
          </div>
          <div>
            <label for="neighborhood" class="block font-medium mb-1">Bairro</label>
            <input
              v-model="formData.neighborhood"
              type="text"
              id="neighborhood"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="Ex: Centro"
            />
            <span v-if="errors.neighborhood" class="text-red-600 text-sm">
              {{ errors.neighborhood }}
            </span>
          </div>
        </div>
  
        <!-- Cidade e Estado -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label for="city" class="block font-medium mb-1">Cidade</label>
            <input
              v-model="formData.city"
              type="text"
              id="city"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="Ex: Recife"
            />
            <span v-if="errors.city" class="text-red-600 text-sm">
              {{ errors.city }}
            </span>
          </div>
          <div>
            <label for="state" class="block font-medium mb-1">Estado</label>
            <input
              v-model="formData.state"
              type="text"
              id="state"
              class="w-full p-2 border border-gray-300 rounded"
              placeholder="Ex: PE"
            />
            <span v-if="errors.state" class="text-red-600 text-sm">
              {{ errors.state }}
            </span>
          </div>
        </div>
  
        <!-- Interesses e Hobbies -->
        <div>
          <label for="interests" class="block font-medium mb-1">Interesses e Hobbies</label>
          <textarea
            v-model="formData.interests"
            id="interests"
            rows="2"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="Ex: novelas, filmes, culinária, yoga, leitura, etc."
          ></textarea>
          <span v-if="errors.interests" class="text-red-600 text-sm">
            {{ errors.interests }}
          </span>
        </div>
  
        <!-- Serviços Oferecidos -->
        <div>
          <label for="services_offered" class="block font-medium mb-1">Serviços que você oferece</label>
          <textarea
            v-model="formData.services_offered"
            id="services_offered"
            rows="2"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="Ex: cuidar de crianças, oferecer caronas, dar aulas de yoga..."
          ></textarea>
          <span v-if="errors.services_offered" class="text-red-600 text-sm">
            {{ errors.services_offered }}
          </span>
        </div>
  
        <!-- Serviços Necessários -->
        <div>
          <label for="services_needed" class="block font-medium mb-1">Serviços que você precisa</label>
          <textarea
            v-model="formData.services_needed"
            id="services_needed"
            rows="2"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="Ex: caronas, reforço escolar para meus filhos, etc."
          ></textarea>
          <span v-if="errors.services_needed" class="text-red-600 text-sm">
            {{ errors.services_needed }}
          </span>
        </div>
  
        <!-- Quantos filhos -->
        <div>
          <label for="number_of_children" class="block font-medium mb-1">Quantos filhos você tem?</label>
          <input
            v-model="formData.number_of_children"
            type="number"
            id="number_of_children"
            class="w-full p-2 border border-gray-300 rounded"
            placeholder="Use apenas números"
          />
          <span v-if="errors.number_of_children" class="text-red-600 text-sm">
            {{ errors.number_of_children }}
          </span>
        </div>
  
        <!-- Faixa etária dos filhos (checkboxes) -->
        <div>
          <p class="block font-medium mb-2">Faixa etária dos seus filhos (você pode marcar mais de uma)</p>
          <div class="flex flex-wrap gap-4">
            <label>
              <input type="checkbox" value="0-2" v-model="formData.children_age_groups" />
              0 a 2 anos
            </label>
            <label>
              <input type="checkbox" value="3-5" v-model="formData.children_age_groups" />
              3 a 5 anos
            </label>
            <label>
              <input type="checkbox" value="6-8" v-model="formData.children_age_groups" />
              6 a 8 anos
            </label>
            <label>
              <input type="checkbox" value="9-12" v-model="formData.children_age_groups" />
              9 a 12 anos
            </label>
          </div>
          <span v-if="errors.children_age_groups" class="text-red-600 text-sm">
            {{ errors.children_age_groups }}
          </span>
        </div>
  
        <!-- Botão de Cadastro -->
        <div class="flex justify-center mt-6">
          <button
            type="submit"
            class="bg-[#E67E80] text-white px-6 py-2 rounded-md text-sm font-semibold hover:bg-[#d46567] transition-colors"
          >
            Registrar
          </button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  // O useRouter permite navegar para outra rota após o cadastro
  const router = useRouter()
  
  // Objeto reativo para armazenar os dados do formulário
  const formData = ref({
    username: '',
    email: '',
    password1: '',
    password2: '',
    birth_date: '',
    cep: '',
    street: '',
    house_number: '',
    neighborhood: '',
    city: '',
    state: '',
    interests: '',
    services_offered: '',
    services_needed: '',
    number_of_children: '',
    children_age_groups: []
  })
  
  // Variáveis reativas para erros, mensagem de sucesso e controle do modal
  const errors = ref({})
  const successMessage = ref('')
  const showModal = ref(false)
  
  // Variáveis para controlar a visualização das senhas
  const showPassword1 = ref(false)
  const showPassword2 = ref(false)
  
  // Função para enviar os dados via POST para a API
  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/register/', formData.value, {
        headers: { 'Content-Type': 'application/json' }
      })
      successMessage.value = 'Registro bem-sucedido!'
      errors.value = {}
      
      showModal.value = true
    } catch (error) {
      if (error.response && error.response.data && error.response.data.errors) {
        errors.value = error.response.data.errors
      } else {
        console.error(error)
        alert('Ocorreu um erro ao tentar registrar. Verifique o console.')
      }
    }
  }
  
  // Função para buscar os dados do endereço a partir do CEP (usando a API ViaCEP)
  const fetchCep = async () => {
   
    const cepClean = formData.value.cep.replace(/\D/g, '')
    if (cepClean.length === 8) {
      try {
        const { data } = await axios.get(`https://viacep.com.br/ws/${cepClean}/json/`)
        if (!data.erro) {
          formData.value.street = data.logradouro
          formData.value.neighborhood = data.bairro
          formData.value.city = data.localidade
          formData.value.state = data.uf
        } else {
          errors.value.cep = 'CEP não encontrado.'
        }
      } catch (err) {
        errors.value.cep = 'Erro ao buscar o CEP.'
      }
    }
  }
  
  
  const closeModal = () => {
    showModal.value = false
    router.push('/')
  }
  </script>
  
  <style scoped>

  </style>
  