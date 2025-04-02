<script setup>
import AppButton from "../components/AppButton.vue";
</script>

<template>
 
  <div class="flex md:flex-row flex-col justify-end items-end w-full bg-[#F5F7FA]">
    <div
      class="h-[600px] w-full
             bg-[url(/images/smiley-mae-e-filho-em-casa-vista.png)]
             bg-contain bg-[right_30px_top_-10px] md:bg-[right_top_10px]
             bg-no-repeat"
    >
     
      <div class="md:w-[70%] font-semibold flex flex-col pl-5 md:pl-20 md:pt-20 md:pr-10">
        <h1 class="md:leading-[80px] text-[1.5rem] md:text-[3.5625rem] text-[#4D4D4D] pr-1 mb-4">
          Apoio real, conexões <br />
          que fortalecem e <br />
          transformam.
        </h1>
        <div>
          <p class="text-[#717171] text-[14px] mb-4">
            Uma rede colaborativa onde mães se ajudam, economizam e crescem juntas.
          </p>
          <AppButton label="Faça parte" class="w-[146px] h-[52px]" />
        </div>
      </div>
    </div>
  </div>

  
  <section class="p-5 md:p-10 text-center bg-white">
    <h2 class="text-2xl md:text-3xl font-bold mb-4 text-[#4D4D4D]">
      Sobre o Projeto
    </h2>
    <p class="text-[#717171] text-sm md:text-base leading-6 max-w-[800px] mx-auto mb-8">
      Este projeto nasceu do desejo de conectar mães que buscam apoio real,
      troca de experiências e oportunidades de crescimento conjunto. <br />
      Ser mãe é desafiador, mas não precisa ser solitário. O Entre Mães é uma
      rede colaborativa onde mães se ajudam, economizam e ganham recompensas.
      Aqui, você troca serviços, recebe cashback e usa nossa moeda interna
      para facilitar o dia a dia.
    </p>

 
    <div class="max-w-[800px] mx-auto text-left text-[#4D4D4D] mb-8">
      <h3 class="text-xl md:text-2xl font-semibold mb-4">Como funciona?</h3>
      <ul class="list-disc list-inside space-y-2 text-[#717171]">
        <li>
          <strong>Troque e compartilhe:</strong> Ofereça e receba ajuda de outras mães da comunidade.
        </li>
        <li>
          <strong>Ganhe recompensas:</strong> Acumule pontos e troque por benefícios exclusivos.
        </li>
        <li>
          <strong>Encontre oportunidades:</strong> Participe de cursos, palestras e eventos voltados ao desenvolvimento pessoal e profissional.
        </li>
      </ul>
    </div>

   
    <div class="max-w-[800px] mx-auto text-left text-[#4D4D4D] mb-8">
      <h3 class="text-xl md:text-2xl font-semibold mb-4">Por que fazer parte?</h3>
      <ul class="list-disc list-inside space-y-2 text-[#717171]">
        <li><strong>Comunidade real:</strong> Conecte-se a mães que vivem os mesmos desafios.</li>
        <li><strong>Apoio mútuo:</strong> Troque recursos e maximize seu sucesso.</li>
        <li><strong>Economia colaborativa:</strong> Reduza custos e impulsione seu crescimento.</li>
        <li><strong>Impacto positivo:</strong> Transforme sua rede de apoio em algo sustentável.</li>
      </ul>
    </div>

   
    <div class="max-w-[800px] mx-auto text-center">
      <p class="text-lg md:text-xl font-semibold text-[#4D4D4D] mb-4">
        Somos uma rede de mães que se ajudam. Vem fazer parte!
      </p>
      <button
        class="bg-[#E67E80] text-white px-6 py-3 rounded-md text-sm md:text-base font-semibold
               hover:bg-[#d46567] transition-colors"
      >
        Quero fazer parte
      </button>
    </div>
  </section>
</template>

<style scoped>

</style>
