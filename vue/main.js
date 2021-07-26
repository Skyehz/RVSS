import Vue from 'vue'
import App from './App.vue'
import router from './router'
import'./assets/css/global.css'

import axios from 'axios'
//配置请求根路径
axios.defaults.baseURL='http://192.168.137.133:5000'
Vue.prototype.$axios=axios;

import ElementUI from 'element-ui' //element-ui的全部组件
import 'element-ui/lib/theme-chalk/index.css'//element-ui的css
import './plugins/element.js'
Vue.use(ElementUI)
Vue.config.productionTip = false

new Vue({
  axios,
  router,
  render: h => h(App),
}).$mount('#app')
