// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import routers from './router/router'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueParticles from 'vue-particles'
import store from './vuex/store'
import echarts from 'echarts'

Vue.prototype.$echarts = echarts
Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.use(VueParticles)

const router = new VueRouter({
  mode: 'history',
  routes: routers
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
