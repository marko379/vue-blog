import { createApp } from 'vue'
import VueCookies from 'vue-cookies';
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas,far,fab)

import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000/articles'



createApp(App).use(store).use(router,axios).use(VueCookies,VueCropper).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

// createApp(App).use(store,router,axios,VueCookies,VueCropper).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

