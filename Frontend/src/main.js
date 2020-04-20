// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@progress/kendo-ui'
import '@progress/kendo-theme-default/dist/all.css'
import App from './App'
import router from './router'
import { Chat, ChatInstaller } from '@progress/kendo-chat-vue-wrapper'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Element)
Vue.use(ChatInstaller)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App, Chat }
})
