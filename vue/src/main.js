import Vue from 'vue'
import vuetify from './plugins/vuetify' // path to vuetify export
//import firebase from './plugins/firebase'
import App from './App.vue'
import store from './store'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  el: '#app',
  vuetify,
  //  firebase,
  router,
  store,
  data: {}
})

