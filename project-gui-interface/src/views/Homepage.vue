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
    <ModuleList></ModuleList>
  </div>
</template>

<script>
import ModuleList from '../components/common/ModuleList.vue';
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
    ModuleList,
    Toolbar,
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
