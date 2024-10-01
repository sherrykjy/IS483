import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"
import axios from 'axios';
import store from './store';

import { create, NTabs, NTab, NTabPane } from 'naive-ui'

const naive = create({
    components: [NTabs, NTab, NTabPane]
})

// const requireStyles = require.context('@/assets/styling', false, /\\.css$/);
// requireStyles.keys().forEach(fileName => requireStyles(fileName));

const app = createApp(App)

app.config.globalProperties.$http = axios;

app.use(router).use(naive).use(store).mount('#app')