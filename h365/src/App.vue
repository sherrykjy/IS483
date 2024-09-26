<script setup>
  import { RouterView, useRoute } from 'vue-router'
  import navBar from './components/navBar.vue'

  const route = useRoute();
</script>

<template>
  <navBar v-if="!route.meta.hideNavBar" />  
  <RouterView />
</template>

<script>
  import "bootstrap/dist/css/bootstrap.min.css";
  import "bootstrap/dist/js/bootstrap.min.js";

  import '@/assets/styling/general.css';
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
