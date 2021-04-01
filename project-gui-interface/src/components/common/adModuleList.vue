<template>
  <v-item-group class="pa-4">
    <v-container grid-list-md>
      <v-layout wrap>
<<<<<<< HEAD
        <v-flex v-for="[text, l, img, admin] in adminlinks"
        :key="l"
        link
        >

=======
        <v-flex v-for="[text, l, img, admin] in links" :key="l" link>
>>>>>>> b8d590321102d97a497a49b5fc4ef850e6aee9b5
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
<<<<<<< HEAD
data(){ 
    return{
      adminlinks: [
      [ 'Dashboard', '/dashboard',require("../../assets/dashboard.png"),false],
      [ 'Discover', '/discover',require("../../assets/search.png"),false],
      [ 'check', '/check',require("../../assets/check.png"),false],
      [ 'function', '/function',require("../../assets/function.png"),false],
      [ 'alert', '/alert', require("../../assets/alert.png"),false],
      ],
    }
=======
  data() {
    return {
      description: "",
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
>>>>>>> b8d590321102d97a497a49b5fc4ef850e6aee9b5
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