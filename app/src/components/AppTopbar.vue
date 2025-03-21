<script setup>
import { ref } from "vue";
import { useLayout } from "../composables/useLayout";
import AppButton from "./AppButton.vue";

const { isDarkMode, toggleDarkMode } = useLayout();

const items = ref([
    {
        label: 'Início',
        target: '_blank',
        route:'/',
        url:'/home',
    },
    {
        label: 'Sobre',
        action: {
            click: () => {
                console.log('Sobre');
            },
        },
        target: '_blank',
        route:'/about',
        url:'/about',
    },
    {
        label: 'Dúvidas',
    },
    {
        label: 'Sobre',
    },
    {
        label: 'Serviços',
    },
]);
</script>

<template>
    <div class=" dark:bg-surface-900 h-[90px] 
      mx-auto  w-full p-2">
            <Menubar :model="items" :pt="{
                root: ' !rounded-none !bg-[#4D4D4D] flex justify-between   '
                , item: {
                    class: '!bg-[#4D4D4D] !border-none !rounded-none px-5 hover:bg-[#4D4D4D] hover:text-[#E67E80] !text-white text-[16px] ',
                }
                , itemlabel: '!leading-[24px] !text-white text-[16px] ',
                buttonicon: 'text-[#E67E80]',
                itemcontent: '!bg-[#4D4D4D] active:bg-[#4D4D4D] active:text-[#E67E80] hover:bg-[#4D4D4D] hover:text-[#E67E80] !text-white text-[16px]'
            }">
                <template #start>
                    <div class="hidden md:block flex items-center gap-2 mr-40 ml-10">
                        <Image src="/images/heart-logo.png" alt="Image" />
                    </div>
                </template>
                <template #end>
                    <div class="flex items-center gap-5 ">
                      <div class="hidden md:block flex  justify-between items-center gap-10  ">

               <!--          <router-link v-for="item in items"   :to="item.route" custom>
                            <span class="!leading-[24px] !text-white text-[16px] pl-10" >{{ item.label }}</span>
                        </router-link>   -->                      
                       <!--  <a v-for="item in items" v-styleclass="{
                                    selector: '@next',
                                    enterFromClass: 'hidden',
                                    enterActiveClass: 'animate-scalein',
                                    leaveToClass: 'hidden',
                                    leaveActiveClass: 'animate-fadeout',
                                    hideOnOutsideClick: true,
                                }" :href="item?.url" :target="item?.target" v-bind="item?.action">
                            <span class="!leading-[24px] !text-white text-[16px] pl-10">{{ item.label }}</span>
                        </a> -->
                      </div>

                      <div class="flex items-center justify-end gap-10  md:mr-15">
                        <div class="text-[#E67E80]">Acessar</div>
                        <AppButton label="Faça seu cadastro" class="w-[200px] h-[40px]" />
                      </div>
                        <button type="button"
                    class="hidden w-10 h-10 flex items-center 
                    justify-center 
                    rounded-full 
                    hover:bg-surface-100 
                    dark:hover:bg-surface-800 transition-all text-surface-900 dark:text-surface-0 focus-visible:outline-hidden focus-visible:ring-1 focus-visible:ring-primary focus-visible:ring-offset-2 focus-visible:ring-offset-surface-0 dark:focus-visible:ring-offset-surface-950"
                    @click="toggleDarkMode">
                    <i :class="['pi text-base', { 'pi-moon': isDarkMode, 'pi-sun': !isDarkMode }]" />
                </button>
                    </div>
                </template>
                <template #item="{ item, props, hasSubmenu }">
                    <router-link  v-slot="{ href, navigate }" :to="item.route" custom>
                        <a v-ripple :href="href" v-bind="props.action" @click="navigate"
                        class="!leading-[24px] !text-white text-[16px] hover:text-[#E67E80] " 
                        >
                            <span :class="item.icon" />
                            <span>{{ item.label }}</span>
                        </a>
                    </router-link>
                  <!--   <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
                        <span  class="!leading-[24px] !text-white text-[16px] pl-10" >{{ item.label }}</span>
                    </a> -->
                </template>
            </Menubar>
       
    </div>
</template>
