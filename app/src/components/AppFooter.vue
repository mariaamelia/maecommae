<template>
    <div class="flex flex-col  items-center mx-auto w-full  p-2">
        <div class="bg-[#F5F7FA] h-[300px]  flex  items-center justify-center  w-full p-6 text-center">
            <span class="text-[2rem] md:text-[4rem] md:leading-[4.5rem]  justify-center  text-[#8ABEB7]  font-semibold ">
                "Mães ajudando mães <br>
                a crescer, sonhar <br>e prosperar!"

            </span>
        </div>
        <div class="bg-[#8ABEB7]  flex justify-center items-center sm:flex-row flex-col gap-2 w-full p-6 pt-10  md:px-30">
            <div class="flex items-start md:flex-row flex-col  w-full">
                <div class="basis-1/4 flex flex-col  items-start md:basis-2/3  ">
                    <div class="flex flex-row items-center mb-8 ">
                        <Image src="/images/nexcent-Icon.png" alt="Image" />
                        <span class="ml-4"></span>
                        <Image src="/images/nexcent.png" alt="Image" />
                    </div>
                    <p class="text-[20px] text-white !leading-[20px] mt-5">
                        Copyright © 2025 MãeComMãe ltd.
                    </p>
                    <p class="mt-3 text-[14px] text-white !leading-[20px] mb-10">
                        Todos os direitos reservados
                    </p>
                    <div class="gap-4 flex flex-row items-center mt-4">
                        <div class="w-[32px] h-[32px] bg-white/10 flex justify-center items-center p-2 rounded-full  "><i class="pi pi-twitter opacit-20" style="color: white; font-size: 14px;"></i></div>
                        <div class="w-[32px] h-[32px] bg-white/10 flex justify-center items-center p-2 rounded-full  "><i class="pi pi-youtube opacit-20" style="color: white; font-size: 14px;"></i></div>
                        <div class="w-[32px] h-[32px] bg-white/10 flex justify-center items-center p-2 rounded-full  "><i class="pi pi-instagram opacit-20" style="color: white; font-size: 14px;"></i></div>
                        <div class="w-[32px] h-[32px] bg-white/10 flex justify-center items-center p-2 rounded-full  "><i class="pi pi-facebook opacit-20" style="color: white; font-size: 14px;"></i></div>
                    </div>
                </div>
                <div class=" md:basis-1/3 ">
                    <p class=" font-semibold text-white text-[20px] leading-[28px] mb-10">Company</p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Sobre
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Blog
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Fale Conosco
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Avaliações
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2 h-[25px]">
                    </p>

                </div>
                <div class="w-full  md:basis-1/3 ">
                    <p class=" font-semibold text-white text-[20px] leading-[28px] mb-10">Suporte</p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        ChatBot
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Termos de serviço
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Legal
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Política de Privacidade
                    </p>
                    <p class="text-white text-[14px] leading-[28px] mb-2">
                        Status
                    </p>

                </div>
                <div class=" md:basis-1/3 md:h-[250px]  ">
                    <p class="font-semibold text-white text-[20px] leading-[28px] mb-7">Assine nossa<br> newsletter</p>
                    <IconField class="border border-[white] opacity-40 px-3 rounded-[8px] bg-[white] flex items-center">
                        <div class="flex items-center ">
                            <InputText placeholder="Escreva seu e-mail" class="bg-[white] h-[40px]  w-[255px] " />
                            <div class=" pi pi-send opacity-40 " />
                        </div> 
                    </IconField>
                </div>
            </div>
        </div>
    </div>
</template>
