<template>
  <div>
    <toolbar></toolbar>
  
        <img
          width="400"
          style="display: block; margin: -60px auto;"
          src="../assets/logo.png"
        />
      <v-icon>mdi-clipboard-text</v-icon>
      Modules
    <v-divider></v-divider>
    <v-show="isAdmin()">
    <v-divider></v-divider>
    <adModuleList></adModuleList>
  </div>
</template>

<script>
import store from "@/store/index"
import adModuleList from '../components/common/adModuleList.vue';
import Toolbar from '../components/common/Toolbar.vue';

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
    adModuleList,
    Toolbar,
  },
  methods:{
    link(item){
      this.$router.push({ path: item.link })
    },
    isAdmin(){
      return store.state.isAdmin;
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
