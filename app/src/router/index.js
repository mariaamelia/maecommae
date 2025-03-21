import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SigninView from '../views/SignInView.vue'
import _publicLayout from '../views/_publicLayout.vue'
import { subtitle } from '@primeuix/themes/aura/card'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: _publicLayout,
      children: [
        { path: '', name:'Home',  component: () => import('../views/HomeView.vue'),  
          meta: { title: 'Mães apoiando mães:' ,  image:'cuidado-maes.png' ,
                  subtitle: "mais do que um serviço, uma comunidade.",
                  phrase:'É suporte, é conexão, é comunidade - mães ajudando mães a crescerem juntas.' }
        },
        { path: 'about', name:'About',  
          component: () => import('../views/AboutView.vue'),
          meta: { title: 'Apoio real, conexões que fortalecem e transformam.' ,  
          image:'smiley-mae-e-filho-em-casa-vista.png' ,
          phrase:'Uma rede colaborativa onde mães se ajudam, economizam e crescem juntas.' }
        
        },
      ]
    },
    {
      path: '/about',     
      component: () => import('../views/AboutView.vue'),
    },
  ],
})


export default router