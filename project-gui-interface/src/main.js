import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import axios from "axios";
import store from "./store/index";
import VueChartJs from "vue-chartjs";
import vueMoment from 'vue-moment';

Vue.use(VueChartJs);
Vue.use(vueMoment);
Vue.config.productionTip = false;
Vue.prototype.$http = axios;
new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
