import { createApp } from 'vue'
import { create, NButton, NCard } from 'naive-ui'
import App from './App.vue'

import router from "./router"
const naive = create({
    components: [NButton, NCard]
})

// const requireStyles = require.context('@/assets/styling', false, /\\.css$/);
// requireStyles.keys().forEach(fileName => requireStyles(fileName));

createApp(App).use(router).use(naive).mount('#app')
