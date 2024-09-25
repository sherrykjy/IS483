import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: "/",
        name: "loginPage",
        component: () => import("@/views/loginPage.vue")
    },

    {
        path: "/info",
        name: "informationPage",
        component: () => import("@/views/informationPage.vue")
    },

    {
        path: "/goals",
        name: "goalSettingPage",
        component: () => import("@/views/goalSettingPage.vue")
    },

    {
      path: "/home",
      name: "homePage",
      component: () => import("@/views/homePage.vue")
    },

    {
      path: "/events",
      name: "eventsPage",
      component: () => import("@/views/eventsPage.vue")
    },

    {
      path: "/viewEvent",
      name: "viewEventPage",
      component: () => import("@/views/viewEventPage.vue")
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