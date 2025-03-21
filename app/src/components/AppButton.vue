<script setup>
import { useAttrs, defineEmits } from 'vue'



</script>
<template>
  <Button
    v-bind="$attrs"
    class="!bg-[#E67E80] font-medium text-[16px] !rounded-[6px] py-[6px] px-6 font-medium h-[40px]"
  >
    <template v-for="(slot, index) of Object.keys($slots)" :key="index" v-slot:[slot]>
      <slot :name="slot"></slot>
    </template>
  </Button>
</template>
