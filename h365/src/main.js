import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"

import { create, NTabs, NTab, NTabPane } from 'naive-ui'

const naive = create({
    components: [NTabs, NTab, NTabPane]
})

// const requireStyles = require.context('@/assets/styling', false, /\\.css$/);
// requireStyles.keys().forEach(fileName => requireStyles(fileName));

createApp(App).use(router).use(naive).mount('#app')