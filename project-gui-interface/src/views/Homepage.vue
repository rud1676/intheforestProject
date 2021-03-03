<template>
  <div>
    <v-app-bar color="#7CB342">
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-btn text href="javascript:window.location.reload(true);">
        <v-icon> mdi-home </v-icon>home
      </v-btn>
    <v-spacer></v-spacer>     
    <v-btn icon>
      <v-icon>mdi-export</v-icon>
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
          src="../assets/logo2.png"
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


        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  
        <img
          width="400"
          style="display: block; margin: -100px auto;"
          src="../assets/logo.png"
        />
      <v-icon>mdi-clipboard-text</v-icon>
      Modules
    <v-divider></v-divider>
    <ModuleList></ModuleList>
  </div>
</template>

<script>
import ModuleList from '../components/common/ModuleList.vue';
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
      { text: "Logout", icon: "mdi-export" },
    ],
    }),
  components:{
    ModuleList,
  },
  methods:{
    link(item){
      this.$router.push({ path: item.link })
    }
  },
};
</script>

<style>
.static {
  display: flex;
  position: absolute;
  width: 100px;
  height: 100px;
  top: 300px;
  left: 30%;
  border-width: 15px;
}
</style>
