<template>
  <div id="inspire">
    <v-navigation-drawer color="#9CCC65" clipped app>
      <v-sheet color="#7CB342" class="pa-4 justify-center">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <img src="../../assets/logo.png"
        /></v-avatar>

        <div>intheForest-Project</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="[icon, text, l, admin] in links"
          :key="l"
          link
          v-on:click="tolink(l)"
          v-show="isAdmin(admin)"
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import store from "@/store/index"
export default {
  data: () => ({
    cards: ["Today", "Yesterday"],
    drawer: null,
    links: [
      ["mdi-view-dashboard", "Dashboard", "/dashboard",true],
      ["mdi-magnify", "Discover", "/discover",true],
      ["mdi-clock", "check", "/check",true],
      ["mdi-function", "function", "/function",true],
      ["mdi-alarm", "alert", "/alert",true],
      ["mdi-tune", "Management", "/management",false],
    ],
  }),
  methods: {
    tolink: function (l) {
      this.$router.push({ path: l });
    },
    isAdmin(admin){
      if(store.state.isAdmin) return true;
      else{
        return admin
      }
    },
  },
  
};
</script>

<style></style>
