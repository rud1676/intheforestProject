<template>
  <v-item-group class="pa-4">
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l, img, admin] in adminlinks" :key="l" link>
          <v-card
            v-if="isAdmin(admin)"
            height="220"
            width="220"
            @click="tolink(l)"
            align="center"
          >
            <v-card-title class="justify-center py-2">{{ text }}</v-card-title>

            <img width="150" style=" auto" :src="img" />
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-item-group>
</template>

<script>
import store from "@/store/index";
export default {
  data() {
    return {
      adminlinks: [
        [
          "Dashboard",
          "/dashboard",
          require("../../assets/dashboard.png"),
          false,
        ],
        ["Discover", "/discover", require("../../assets/search.png"), false],
      ],
    };
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