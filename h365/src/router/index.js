import {createRouter, createWebHistory} from "vue-router";

const routes = [
    // {
    //     path: "/",
    //     name: "loginPage",
    //     component: () => import("@/views/login_page.vue")
    // },
    
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;