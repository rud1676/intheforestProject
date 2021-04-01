import Vue from "vue";
import Vuex from "vuex";
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
    isAdmin: true //test를 위해 true로 바꿈
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
  },
  actions: {
    //로그인 시도
    login({ state, commit }, loginObj) {
      let selectedUser = null;
      state.allUsers.forEach((user) => {
        if (user.id === loginObj.id) selectedUser = user;
      });
      if (selectedUser === null || selectedUser.password !== loginObj.password)
        commit("loginError");
      else if (selectedUser.admin == true) {
        commit("adminloginSuccess", selectedUser);
        console.log("admin login");
        router.push("/home");
      } else {
        commit("userloginSuccess", selectedUser);
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
