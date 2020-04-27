// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueCardPayment from 'vue-card-payment'
import 'vue-card-payment/dist/vue-card-payment.css'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@progress/kendo-ui'
import '@progress/kendo-theme-default/dist/all.css'
import App from './App'
import router from './router'
import { Chat, ChatInstaller } from '@progress/kendo-chat-vue-wrapper'
import axios from 'axios'
import VueAxios from 'vue-axios'
import {store} from './store/store'

Vue.use(Element)
Vue.use(ChatInstaller)
Vue.use(VueAxios, axios)
Vue.use(VueCardPayment)

axios.defaults.baseURL = 'http://localhost:8000/';
Vue.config.productionTip = false
Vue.config.devtools = true;

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({
        path: '/Login',
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresVisitor)) {
    if (store.getters.loggedIn) {
      next({
        path: '/Home',
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App, Chat }
})
