<script setup>
import { ref } from 'vue'
import AppComunity from "../components/AppComunity.vue";
import AppNetwork from "../components/AppNetwork.vue";
import AppPartners from "../components/AppPartners.vue";
import AppTestimony from "../components/AppTestimony.vue";
import AppButton from "../components/AppButton.vue";

import Chatbot from "../components/Chatbot.vue";
const showChatbot = ref(false)
const robotImage = '../../public/images/chatbot.png' 
</script>

<template>
  <main class="relative">
    
    <div class="bg-[#F5F7FA]">
      <div class="relative h-[552px] w-full bg-[url(/images/cuidado-maes.png)] bg-no-repeat bg-contain bg-[right_bottom]">
        <div class="absolute inset-0 flex items-center">
          <div class="md:w-7/12 px-5 md:px-20">
            <h1 class="text-2xl md:text-6xl font-semibold text-[#4D4D4D] mb-2">
              Mães apoiando mães:
            </h1>
            <div>
              <p class="text-[#E67E80] text-2xl md:text-5xl leading-tight mb-2">
                mais do que um <br> serviço, uma <br> comunidade.
              </p>
              <p class="text-[#717171] text-sm md:text-base mb-12">
                É suporte, é conexão, é comunidade - mães ajudando mães a crescerem juntas.
              </p>
              <RouterLink to="/register">
                <AppButton label="Faça parte" class="w-[146px] h-[52px] mt-8" />
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>

    
    <AppPartners />
    <AppComunity />
    <AppSuport />
    <AppNetwork />
    <AppHowWork />
    <AppTestimony />

    
    <img
      v-if="!showChatbot"
      :src="robotImage"
      class="robot-fixed"
      alt="Iniciar Chatbot"
      @click="showChatbot = true"
    />

    <!-- Chatbot -->
    <Chatbot v-if="showChatbot" @close="showChatbot = false" />
  </main>
</template>

<style scoped>
.robot-fixed {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 120px;
  height: 200px;
  z-index: 50;
  cursor: pointer;
  background-color: transparent;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: pulse 2s infinite;
  object-fit: contain; 
  box-shadow: none; 
}

.robot-fixed:hover {
  transform: scale(1.08);
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

</style>