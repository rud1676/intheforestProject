<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>프로세스가 만든 쓰레드 감지!</v-card-title>
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Filter about user, program"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          dense
          :headers="headers"
          :items="events"
          :loading="load"
          :search="search"
          loading-text="wait a moment"
          class="elevation-1"
        ></v-data-table>
      </v-card>
      <v-divider class="mx-5 mt-4"></v-divider>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    search: "",
    load: true,
    events: [],
    headers: [
      { text: "Source", value: "source" },
      { text: "Target", value: "target" },
      { text: "name", value: "name" },
    ],
  }),
  methods: {},
  mounted() {
    const URL = this.$store.state.pyurl+"/createThread/thread";
    console.log("post time and abnormal detect");
    axios.get(URL).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>
