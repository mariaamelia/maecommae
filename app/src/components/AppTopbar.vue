<script setup>
import { ref, onMounted } from "vue";
import { useLayout } from "../composables/useLayout";
import AppButton from "./AppButton.vue";
import { useRouter } from "vue-router";
import emitter from '@/eventBus'

const { isDarkMode, toggleDarkMode } = useLayout();
const router = useRouter();

const user = ref(null);

onMounted(() => {
  const savedUser = localStorage.getItem("user");
  if (savedUser) {
    user.value = savedUser;
  }
});

emitter.on("user:logged", (nome) => {
  user.value = nome;
});


const handleLogout = () => {
  localStorage.removeItem("user");
  user.value = null;
  router.push("/logout");
};

const items = ref([
  { label: "Início", route: "/" },
  { label: "Sobre", route: "/about" },
  { label: "Serviços", route: "/servicos" },
  { label: "Dúvidas", route: "/duvidas" },
]);
</script>

<template>
  <div class="bg-white dark:bg-gray-900 w-full border-b border-gray-300 dark:border-gray-700">
    <Menubar
      :model="items"
      :pt="{
        root: 'flex flex-wrap justify-between items-center px-4 py-2',
        item: {
          class: 'text-gray-800 dark:text-white hover:text-[#E67E80] px-4 py-2 text-[16px]'
        },
        itemlabel: 'text-[16px]',
        end: 'flex items-center gap-4'
      }"
    >
      
      <template #start>
        <div class="flex items-center gap-2">
          <img src="/images/heart-logo.png" alt="Logo" class="h-8" />
        </div>
      </template>

     
      <template #end>
        <div class="flex flex-wrap items-center gap-4">
        
          <button
            type="button"
            @click="toggleDarkMode"
            class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-gray-200 dark:hover:bg-gray-700 transition-all text-gray-800 dark:text-white"
          >
            <i :class="['pi text-base', isDarkMode ? 'pi-moon' : 'pi-sun']" />
          </button>

          <template v-if="!user">
            <RouterLink to="/login" class="text-[#E67E80] font-medium">Acessar</RouterLink>
            <RouterLink to="/register">
              <AppButton label="Faça seu cadastro" class="w-[180px] h-[38px] text-sm" />
            </RouterLink>
          </template>

          <template v-else>
            <div class="flex items-center gap-3 text-gray-800 dark:text-white font-medium">
              <i class="pi pi-user"></i>
              <span class="hidden sm:inline">Olá, {{ user }}</span>
              <button
                @click="handleLogout"
                class="text-[#E67E80] font-semibold hover:underline"
              >
                Sair
              </button>
            </div>
          </template>
        </div>
      </template>

      <template #item="{ item, props }">
        <router-link
          v-slot="{ href, navigate }"
          :to="item.route"
          custom
        >
          <a
            v-ripple
            :href="href"
            v-bind="props.action"
            @click="navigate"
            class="block text-gray-800 dark:text-white hover:text-[#E67E80]"
          >
            <span>{{ item.label }}</span>
          </a>
        </router-link>
      </template>
    </Menubar>
  </div>
</template>


<style scoped>

@media (max-width: 640px) {
  .pi-user + span {
    display: none;
  }
}
</style>
