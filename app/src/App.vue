<script setup>
import AppFooter from "./components/AppFooter.vue";
import AppTopbar from "./components/AppTopbar.vue";
import { useWindowSize } from '@vueuse/core'
import {  RouterView } from 'vue-router'
const { width, height } = useWindowSize();
</script>

<template>
    <div class="bg-[#ffffff] dark:bg-surface-950 min-h-screen flex flex-col">
        <RouterView></RouterView>
    </div>
</template>
