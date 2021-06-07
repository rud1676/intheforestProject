<template>
  <v-item-group class="pa-4">
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l, img, admin] in links" :key="l" link shrink>
          <v-item>
            <v-card
              v-if="isAdmin(admin)"
              slot-scope="{ active }"
              :color="active ? 'primary' : ''"
              height="220"
              width="220"
              @click="tolink(l)"
              align="center"
              ><v-card-title class="justify-center py-2">{{
                text
              }}</v-card-title>

              <img width="150" style=" auto" :src="img" />
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
  data() {
    return {
      links: [
        ["Download", "download", require("../../assets/download.png"), true],
        [
          "Not office hours",
          "timeout",
          require("../../assets/office.png"),
          true,
        ],
        [
          "Anomaly",
          "networkconnection",
          require("../../assets/anomaly.png"),
          true,
        ],
        ["Usb Check", "driverload", require("../../assets/develop.png"), true],
      ],
    };
  },
  methods: {
    tolink(l) {
      this.$router.push({ name: l });
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