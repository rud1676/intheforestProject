<template>
  <div id="inspire">
    <v-app-bar color="#9CCC65" app clipped-left flat dense>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-btn text @click="gotohome()"> <v-icon> mdi-home </v-icon>home </v-btn>
      <v-spacer></v-spacer>
      <v-icon v-if="isAdmin(false)">mdi-account-tie</v-icon>
      <v-icon v-else>mdi-account</v-icon>
      <v-btn text v-if="isLogin">{{ userInfo.name }}님 환영합니다.</v-btn>
      <v-btn icon>
        <v-icon @click="logout">mdi-export</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" :width="330" absolute temporary>
      <v-list nav dense>
        <v-list-item-group color="#7CB342">
          <img src="../../assets/logo2.png" />
          <p class="text-center black--text">Wellcome, admin!😊</p>
          <v-divider></v-divider>

          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            @click="link(item)"
            v-show="isAdmin(item.admin)"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-icon>
              <v-icon>mdi-export</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import store from "@/store/index";
import { mapState, mapActions } from "vuex";
export default {
  data: () => ({
    drawer: false,
    items: [
      {
        text: "Home",
        icon: "mdi-home",
        link: "home",
        admin: true,
      },
      { text: "Account", icon: "mdi-account", link: "userInfo", admin: true },
      //module은 일반 유저 기본 화면으로 link 추가하기
      {
        text: "Admin Panel - UserManage",
        icon: "mdi-wrench",
        link: "manageuser",
        admin: false,
      },
    ],
  }),
  computed: {
    ...mapState(["isLogin", "userInfo"]),
  },
  methods: {
    ...mapActions(["logout"]),
    isAdmin(admin) {
      if (store.state.isAdmin) return true;
      else {
        return admin;
      }
    },

    link(item) {
      this.$router.push({ name: item.link }).catch(() => {});
      this.$data.drawer = false;
    },
    gotohome() {
      this.$router.push("/home").catch(() => {});
    },
    gotologin() {
      this.$router.push("/login");
    },
  },
};
</script>

<style>
</style>