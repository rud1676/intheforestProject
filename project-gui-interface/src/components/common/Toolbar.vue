<template>
  <div id="inspire">
      <v-app-bar color="#9CCC65" app clipped-left flat dense>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-btn text @click="gotohome()">
        <v-icon> mdi-home </v-icon>home
      </v-btn>
    <v-spacer></v-spacer>
    <v-btn text v-if="isLogin">{{ userInfo.name }}님 환영합니다.</v-btn>     
    <v-btn icon>
      <v-icon @click="logout">mdi-export</v-icon>
    </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      :width="330"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          color="#7CB342"
        >
        <img
          src="../../assets/logo2.png"
        />
        <p class="text-center black--text">
          Wellcome, admin!😊
        </p>
        <v-divider></v-divider>

          <v-list-item v-for="(item, i) in items" :key="i" @click="link(item)">
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
import { mapState, mapActions } from "vuex"
export default {
data: () => ({
      drawer: false,
      items: [
      {
        text: "Home",
        icon: "mdi-home",
        link: "/home"
      },
      { text: "Account", icon: "mdi-account", link:"/" },
      { text: "Module", icon: "mdi-clipboard-text" , link:"/dashboard"},
      { text: "Admin Panel", icon: "mdi-wrench" },
    ],
    }),
    computed:{
        ...mapState(["isLogin","userInfo"])
    },
    methods:{
    ...mapActions(['logout']),

    link(item){
      this.$router.push({ path: item.link })
    },
    gotohome(){
        this.$router.push('/home');
    },
    gotologin(){
        this.$router.push('/login');
    }
  },
}
</script>

<style>

</style>