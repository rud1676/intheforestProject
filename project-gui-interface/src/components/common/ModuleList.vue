<template>
  <v-item-group class="pa-4">
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l, img, admin] in links" :key="l" link>
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
        ["Anomaly", "not", require("../../assets/anomaly.png"), true],
        ["usb Check", "driverload", require("../../assets/develop.png"), true],
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