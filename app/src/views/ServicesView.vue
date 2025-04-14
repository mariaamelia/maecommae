<script setup>
import AppButton from "../components/AppButton.vue";
</script>

<template>
  <main>
  
<section class="bg-[#F5F7FA] -mx-5 md:-mx-10 py-10">
  <div class="max-w-[1200px] mx-auto px-5 md:px-10 flex flex-col md:flex-row items-center justify-between gap-8">
    <!-- Columna de texto -->
    <div class="md:w-1/2 text-left">
      <h1 class="text-2xl md:text-4xl font-bold text-[#4D4D4D] mb-4">
        Ser mãe não precisa ser solitário!
      </h1>
      <p class="text-[#717171] text-sm md:text-base max-w-[600px] leading-6 mb-6">
        Aqui, você encontra um espaço seguro para trocar experiências,
        descobrir serviços e ficar com outras mulheres.
      </p>
      <AppButton label="Faça parte" class="px-6 py-3" />
    </div>
    <!-- Columna de imagen -->
    <div class="md:w-1/2 flex justify-center">
      <img
        src="/images/cuidado-maes1.png"
        alt="Mães reunidas"
        class="w-full max-w-md rounded-lg object-contain shadow-lg"
      />
    </div>
  </div>
</section>

    <!-- SECCIÓN NOSSOS SERVIÇOS -->
    <section class="bg-white py-10 px-5 md:px-10 text-center">
    <!-- Título -->
    <h2 class="text-2xl md:text-3xl font-bold text-[#4D4D4D]">
      Nossos serviços
    </h2>
    <!-- Subtítulo -->
    <p class="text-[#717171] text-base md:text-lg max-w-[700px] mx-auto mt-2">
      No Mãe com Mãe, cada troca fortalece a rede de apoio entre mães.
      Aqui, você encontra soluções práticas para o dia a dia e ainda
      recebe recompensas por participar.
    </p>

    <!-- Grid 2x2 -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 max-w-[900px] mx-auto">
      <!-- Card 1 -->
      <div class="flex flex-col items-center">
        <img
          src="/images/cuidado-maes-2.png"
          alt="Momento de brincadeiras"
          class="w-full h-48 object-cover rounded-lg shadow-md"
        />
        <h3 class="mt-3 text-lg font-semibold text-[#4D4D4D]">
          Momento de brincadeiras
        </h3>
      </div>

      <!-- Card 2 -->
      <div class="flex flex-col items-center">
        <img
          src="/images/cuidado-mae3.png"
          alt="Cozinhando"
          class="w-full h-48 object-cover rounded-lg shadow-md"
        />
        <h3 class="mt-3 text-lg font-semibold text-[#4D4D4D]">
          Cozinhando
        </h3>
      </div>

      <!-- Card 3 -->
      <div class="flex flex-col items-center">
        <img
          src="/images/cuidado-maes-4.png"
          alt="Transporte escolar"
          class="w-full h-48 object-cover rounded-lg shadow-md"
        />
        <h3 class="mt-3 text-lg font-semibold text-[#4D4D4D]">
          Transporte escolar
        </h3>
      </div>

      <!-- Card 4 -->
      <div class="flex flex-col items-center">
        <img
          src="/images/cuidado-maes-5.png"
          alt="Reforço escolar"
          class="w-full h-48 object-cover rounded-lg shadow-md"
        />
        <h3 class="mt-3 text-lg font-semibold text-[#4D4D4D]">
          Reforço escolar
        </h3>
      </div>
    </div>
  </section>


    <section class="bg-white py-10 px-5 md:px-10 text-center">
      <h2 class="text-2xl md:text-3xl font-bold text-[#4D4D4D] mb-3">
        O que você pode fazer?
      </h2>
      <p class="text-[#717171] text-sm md:text-base max-w-[800px] mx-auto mb-8">
        Além de aproveitar nossos serviços, você pode colaborar ativamente,
        compartilhar habilidades e construir uma rede de apoio que cresça
        cada vez mais.
      </p>
      <button
        class="bg-[#E67E80] text-white px-6 py-3 rounded-md text-sm md:text-base font-semibold
               hover:bg-[#d46567] transition-colors"
      >
        Contribuir agora
      </button>
    </section>
  </main>
</template>

<style scoped>

</style>
