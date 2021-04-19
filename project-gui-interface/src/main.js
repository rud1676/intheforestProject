import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import axios from "axios";
import store from "./store/index";
import VueGoogleCharts from "vue-google-charts";

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
new Vue({
  VueGoogleCharts,
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
