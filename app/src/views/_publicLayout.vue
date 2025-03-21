<script setup>
import { useRoute } from 'vue-router';

const route = useRoute()
</script>
<template>
    <div class="bg-[#ffffff] dark:bg-surface-950 min-h-screen flex flex-col ">
        <AppTopbar />
        <div class="flex flex-col w-full  mx-auto gap-6 flex-1">
            <div class=" gap-6  w-full px-2  mx-auto flex-1 ">
                <div class="mx-auto  w-full flex flex-col items-center ">

                    <RouterView />
                </div>
            </div>
        </div>
        <AppFooter />
    </div>    
</template>