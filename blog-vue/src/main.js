import { createApp } from 'vue'
import VueCookies from 'vue-cookies';
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


import { library } from '@fortawesome/fontawesome-svg-core'
// import { faUserSecret,faStar,faStarHalfStroke } from '@fortawesome/free-solid-svg-icons'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// library.add(faUserSecret,faStar,faStarHalfStroke )
library.add(fas,far)

import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000/'



createApp(App).use(store).use(router,axios).use(VueCookies,VueCropper).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
