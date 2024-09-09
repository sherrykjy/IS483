import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: "/",
        name: "loginPage",
        component: () => import("@/views/loginPage.vue")
    },

    {
      path: "/home",
      name: "homePage",
      component: () => import("@/views/homePage.vue")
    },

    {
      path: "/explore",
      name: "explorePage",
      component: () => import("@/views/explorePage.vue")
    },

    {
      path: "/collection",
      name: "collectionPage",
      component: () => import("@/views/collectionPage.vue")
    },

    {
      path: "/profile",
      name: "profilePage",
      component: () => import("@/views/profilePage.vue")
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;