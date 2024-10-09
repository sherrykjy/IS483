<template>
    <!-- <div id="app"> -->
        <nav>
            <ul>
                <div class="navbar">
                    <li class="nav-link">
                        <router-link :to="{ name: 'homePage' }" active-class="active-link">
                            <div class="nav-item">
                                <img class="navIcon" :src="isActiveRoute('homePage') ? require('../assets/icons/navbar/home_selected.png') : require('../assets/icons/navbar/home.png')">
                                <a href="./views/homePage.vue" :class="isActiveRoute('homePage') ? 'active-text' : 'inactive-text'">Home</a>
                            </div>
                            </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'eventsPage' }" active-class="active-link">
                            <div class="nav-item">
                                <img class="navIcon" :src="isActiveRoute('eventsPage') ? require('../assets/icons/navbar/explore_selected.png') : require('../assets/icons/navbar/explore.png')">
                                <a href="./views/eventsPage.vue" :class="isActiveRoute('eventsPage') ? 'active-text' : 'inactive-text'">Explore</a>
                            </div>
                            </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'collectionPage' }" active-class="active-link">
                            <div class="nav-item">
                                <img class="navIcon" :src="isActiveRoute('collectionPage') ? require('../assets/icons/navbar/collection_selected.png') : require('../assets/icons/navbar/collection.png')">
                                <a href="./views/collectionPage.vue" :class="isActiveRoute('collectionPage') ? 'active-text' : 'inactive-text'">Collection</a>
                            </div>
                            </router-link>
                    </li>

                    <li class="nav-link">
                        <router-link :to="{ name: 'profilePage' }" active-class="active-link">
                            <div class="nav-item">
                                <img class="navIcon" :src="isActiveRoute('profilePage') ? require('../assets/icons/navbar/profile_selected.png') : require('../assets/icons/navbar/profile.png')">
                                <a href="./views/profilePage.vue" :class="isActiveRoute('profilePage') ? 'active-text' : 'inactive-text'">Profile</a>
                            </div>
                        </router-link>
                    </li>

                </div>
            </ul>
        </nav>
    <!-- </div> -->
</template>

<script>
export default {
  methods: {
    isActiveRoute(routeName) {
      return this.$route.name === routeName;
    }
  }
};
</script>

<style scoped>
ul {
    padding-left: 0px;
}

.navbar {
    display: flex;
    padding: 16px 35px 25px 32px;
    background-color: var(--default-white);
    justify-content: space-between;
    width: 100%;

    position: fixed;
    bottom: 0;
    z-index: 50000;
}

.nav-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    justify-content: center;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.navIcon {
    display: block;
    margin-bottom: 5px;
    width: 20px;
}

.nav-link a {
    display: block;
    font-family: text-semibold;
    font-size: 10.5px;
}

.active-text {
    color: var(--green);
}

.inactive-text {
    color: var(--default-text);
}

</style>