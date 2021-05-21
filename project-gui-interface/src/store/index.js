import Vue from "vue";
import Vuex from "vuex";
import axois from "axios";
import createPersistedState from "vuex-persistedstate";
import router from "@/router";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    allUsers: [
      { id: "imyuseop", name: "임유섭", password: "1234", admin: true },
      { id: "rud", name: "주경진", password: "1234", admin: false }
    ],
    isLogin: false,
    isLoginError: false,
    userInfo: null,
    isAdmin: true, //test를 위해 true로 바꿈
    pyurl: "http://127.0.0.1:8888",
    date: 7,
  },
  mutations: {

    //로그인 성공,
    userloginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
      state.isAdmin = false;
    },
    adminloginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
      state.isAdmin = true;
    },
    //로그인 실패,
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = true;
    },
    logout(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
      state.isAdmin = false;
    }
    //for making Loading view, call this function in dashboard
  },
  actions: {
    //로그인 시도
    async login({ commit }, loginObj) {
      let user = null;
      let state = null;
      console.log(loginObj);
      await axois.post("/login/logon", loginObj).then(r => {
        user = r.data.user;
        state = r.data.state;
        console.log(r)
      })
      if (user === null) {
        alert(state);
        commit("loginError");
      }
      else if (user.admin == "true") {
        commit("adminloginSuccess", user);
        console.log("admin login");
        router.push("/home");
      } else {
        commit("userloginSuccess", user);
        console.log("user login");
        router.push("/home");
      }
    },
    logout({ commit }) {
      commit("logout");
      router.push("/login");
    }
  }
});
