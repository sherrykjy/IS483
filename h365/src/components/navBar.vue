<template>
    <div id="app">
        <nav>
            <ul>
                <div>
                    <li class="nav-link">
                        <router-link :to="{ name: 'homePage' }">
                            <a href="./views/homePage.vue">Home</a>
                        </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'explorePage' }">
                            <a href="./views/explorePage.vue">Explore</a>
                        </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'collectionPage' }">
                            <a href="./views/collectionPage.vue">Collection</a>
                        </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'profilePage' }">
                            <a href="./views/profilePage.vue">Profile</a>
                        </router-link>
                    </li>

                </div>
            </ul>
        </nav>
    </div>
</template>

<script></script>

<style scoped>
#app {
    color: black;
}
</style>