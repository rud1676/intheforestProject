<template>
  <v-item-group>
    <v-container grid-list-md>
      <v-layout wrap>
<<<<<<< HEAD:project-gui-interface/src/components/common/ModuleList.vue
        <v-flex v-for="[text, l, img, admin] in links" :key="l" link>
=======
        <v-flex v-for="[text, l, img, admin] in adminlinks"
        :key="l"
        link
        >
       
>>>>>>> 01f87fcf04616878fe124f9f06f00be76e8893de:project-gui-interface/src/components/common/adModuleList.vue
          <v-item>
            <v-card
              v-if="isAdmin(admin)"
              slot-scope="{ active }"
              :color="active ? 'primary' : ''"
              height="200"
              width="200"
              @click="tolink(l)"
              align="center"
            >
              {{ text }}
              <div>{{ description }}</div>
              <img width="150" style="margin: 15px auto" :src="img" />
            </v-card>
          </v-item>
        </v-flex>
      </v-layout>
    </v-container>
  </v-item-group>
</template>

<script>
import store from "@/store/index";
export default {
<<<<<<< HEAD:project-gui-interface/src/components/common/ModuleList.vue
  data() {
    return {
      links: [
        [
          "Dashboard",
          "/dashboard",
          require("../../assets/dashboard.png"),
          true,
        ],
        ["Discover", "/discover", require("../../assets/search.png"), true],
        ["check", "/check", require("../../assets/check.png"), true],
        ["function", "/function", require("../../assets/function.png"), true],
        ["alert", "/alert", require("../../assets/alert.png"), true],
        [
          "Management",
          "/Management",
          require("../../assets/management.png"),
          false,
        ],
      ],
    };
=======
data(){ 
    return{
      adminlinks: [
      [ 'Dashboard', '/dashboard',require("../../assets/dashboard.png"),false],
      [ 'Discover', '/discover',require("../../assets/search.png"),false],
      [ 'check', '/check',require("../../assets/check.png"),false],
      [ 'function', '/function',require("../../assets/function.png"),false],
      [ 'alert', '/alert', require("../../assets/alert.png"),false],
      [ 'Management', '/Management',require("../../assets/management.png"),false],
      ],
    }
>>>>>>> 01f87fcf04616878fe124f9f06f00be76e8893de:project-gui-interface/src/components/common/adModuleList.vue
  },
  methods: {
    tolink(l) {
      this.$router.push({ path: l });
    },
    isAdmin(admin) {
      if (store.state.isAdmin) return true;
      else {
        return admin;
      }
    },
  },
};
</script>

<style>
</style>