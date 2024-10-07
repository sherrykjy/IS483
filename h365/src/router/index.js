import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: "/",
        name: "loginPage",
        component: () => import("@/views/loginPage.vue"),
        meta: { hideNavBar: true }
    },

    {
        path: "/info",
        name: "informationPage",
        component: () => import("@/views/informationPage.vue"),
        meta: { hideNavBar: true }
    },

    {
        path: "/goal",
        name: "goalSettingPage",
        component: () => import("@/views/goalSettingPage.vue"),
        meta: { hideNavBar: true }
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
      path: "/booked",
      name: "bookedEventsPage",
      component: () => import("@/views/bookedEventsPage.vue")
    },

    {
      path: "/event/:eventId",
      name: "viewEventPage",
      component: () => import("@/views/viewEventPage.vue")
    },

    {
      path: "/collection",
      name: "collectionPage",
      component: () => import("@/views/collectionPage.vue")
    },

    {
      path: "/popup",
      name: "popup",
      component: () => import("@/components/popUp.vue")
    },

    {
      path: "/store",
      name: "storePage",
      component: () => import("@/views/storePage.vue")
    },

    {
      path: "/trade",
      name: "tradePage",
      component: () => import("@/views/tradePage.vue")
    },

    {
      path: "/mytrades",
      name: "myTradesPage",
      component: () => import("@/views/myTradesPage.vue")
    },

    {
      path: "/test",
      name: "testTest",
      component: () => import("@/components/testTest.vue")
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