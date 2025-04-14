import { createWebHistory, createRouter } from "vue-router";
import _publicLayout from "../views/_publicLayout.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: _publicLayout,
      children: [
        {
          path: "",
          name: "Home",
          component: () => import("../views/HomeView.vue"),
        },
        {
          path: "about",
          name: "About",
          component: () => import("../views/AboutView.vue"),
        },
        {
          path: "servicos",
          name: "Servicos",
          component: () => import("../views/ServicesView.vue"),
        },
        {
          path: "register",
          name: "Register",
          component: () => import("../views/RegisterView.vue"),
        },
        {
          path: "login",
          name: "Login",
          component: () => import("../views/LoginView.vue"),
        },
        {
          path: "logout",
          name: "Logout",
          component: () => import("../views/LogoutView.vue"),
        }
      ],
    },
  ],
});

export default router;
