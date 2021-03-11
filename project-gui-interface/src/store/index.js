import Vue from "vue"
import Vuex from "vuex"
import router from '@/router'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        allUsers: [
            { id: "imyuseop", name: "임유섭", password: "1234" },
            { id: "rud", name: "주경진", password: "1234" }
        ],
        isLogin: false,
        isLoginError: false,
        userInfo: null,
    },
    mutations: {
        //로그인 성공,
        loginSuccess(state, payload){
            state.isLogin = true;
            state.isLoginError = false;
            state.userInfo = payload;
        },
        //로그인 실패,
        loginError(state){
            state.isLogin = false;
            state.isLoginError = true;
        },
        logout(state){
            state.isLogin = false;
            state.isLoginError = false;
            state.userInfo = null;
        }
    },
    actions: {
        //로그인 시도
        login( {state, commit}, loginObj){
          let selectedUser = null;
          state.allUsers.forEach(user =>{
              if(user.id === loginObj.id) selectedUser = user
          })
          if(selectedUser === null || selectedUser.password !== loginObj.password) commit('loginError')
          else{
              commit('loginSuccess', selectedUser)
              router.push('/home');
            }
        },
        logout({commit}){
            commit('logout')
            router.push('/login')
        }
    }
})