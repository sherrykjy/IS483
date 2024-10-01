<template>
    <div>
        <h1>Home Page</h1>
    </div>
</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';
export default {
    setup() {
        console.log("home page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
        console.log(userId.value);
        console.log(userEmail.value);
        return {
            userId,
            userEmail
        };
    }
}
</script>

<style scoped>

</style>