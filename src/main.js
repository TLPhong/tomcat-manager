import Vue from 'vue'
import App from './App.vue'
import './assets/tailwind.css'
import router from './router'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faTrash, faPlus, faCheck, faSpinner, faTimes} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false

Vue.component('font-awesome-icon', FontAwesomeIcon)

library.add(faTrash)
library.add(faCheck)
library.add(faSpinner)
library.add(faPlus)
library.add(faTimes)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
