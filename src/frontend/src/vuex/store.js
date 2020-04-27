import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  BASEURL: 'http://127.0.0.1:8000/',
  username: ''
}

export default new Vuex.Store({
  state
})
