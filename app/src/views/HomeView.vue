<script setup>
import AppComunity from "../components/AppComunity.vue";
import AppNetwork from "../components/AppNetwork.vue";
import AppPartners from "../components/AppPartners.vue";
import AppTestimony from "../components/AppTestimony.vue";

</script>

<template>
  <main>
    <div class="flex md:flex-row flex-col justify-end items-end  w-full bg-[#F5F7FA] ">
                        <div
                            class=" h-[552px] w-full bg-[url(/images/cuidado-maes.png)] bg-contain bg-[right_30px_top_-10px]  md:bg-[right_top_-30px]
                              bg-no-repeat ">
                        
                            <div  :class="'md:w-[70%] font-semibold  flex flex-col pl-5   md:pl-25 md:pt-5 mt-[280px] md:mt-0  md:pr-10'">
                                <p class="md:leading-[69px] text-[1.5rem] md:text-[3.5625rem] text-[#4D4D4D] pr-1    ">
                                    Mães apoiando mães:
                                </p>
                                <div class=" ">
                                    <p class="text-[#E67E80]  md:leading-[69px] text-[1.5rem] md:text-[3.5625rem] place-self-start ">
                                        mais do que um <br>serviço, uma<br> comunidade.
                                    </p>
                                    <p class="text-[#717171] text-[14px]">É suporte, é conexão, é comunidade - mães ajudando
                                        mães a crescerem juntas.</p>
                                    <AppButton label="Faça parte" class="w-[146px] h-[52px] mt-5" />
                                </div>
                            </div>                        
                        </div>
                    </div>    
       <AppPartners/> 
        <AppComunity/>
        <AppSuport/>
        <AppNetwork/>
       <AppHowWork></AppHowWork>
        <AppTestimony/> 
</main>   
   
</template>
