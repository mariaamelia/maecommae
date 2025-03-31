<script setup>
import AppComunity from "../components/AppComunity.vue";
import AppNetwork from "../components/AppNetwork.vue";
import AppPartners from "../components/AppPartners.vue";
import AppTestimony from "../components/AppTestimony.vue";
import AppButton from "../components/AppButton.vue";

</script>

<template>
  <main>
    <div class="bg-[#F5F7FA]">
      <div class="relative h-[552px] w-full bg-[url(/images/cuidado-maes.png)] bg-no-repeat bg-contain bg-[right_bottom]">
        <div class="absolute inset-0 flex items-center">
          <div class="md:w-7/12 px-5 md:px-20">
            <h1 class="text-2xl md:text-6xl font-semibold text-[#4D4D4D] mb-4">
              Mães apoiando mães:
            </h1>
            <div>
              <p class="text-[#E67E80] text-2xl md:text-5xl leading-tight mb-4">
                mais do que um <br> serviço, uma <br> comunidade.
              </p>
              <p class="text-[#717171] text-sm md:text-base mb-4">
                É suporte, é conexão, é comunidade - mães ajudando mães a crescerem juntas.
              </p>
              <AppButton label="Faça parte" class="w-[146px] h-[52px]" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <AppPartners />
    <AppComunity />
    <AppSuport/>
    <AppNetwork/>
    <AppHowWork></AppHowWork>
     <AppTestimony />
  </main>
</template>


