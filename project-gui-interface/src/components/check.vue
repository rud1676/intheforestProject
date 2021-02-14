<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-btn @click="whitelist">whiteList check</v-btn>
    <p>{{ this.unkonwlist }}</p>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data: () => ({
    overlay: false,
    zIndex: 0,
    unkonwlist: [],
  }),
  methods: {
    whitelist: function() {
      const URL = 'http://localhost:80/processCreate/whitelist';
      axios.get(URL).then(result => {
        result.data.unknowlist.forEach(item => {
          console.log(item);
          this.unkonwlist.push(item);
        });
      });
    },
  },
};
</script>
