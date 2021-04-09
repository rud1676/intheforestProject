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
      <v-row class="v-flex">
        <v-col>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon color="light-green" dark v-bind="attrs" v-on="on">
                mdi-information
              </v-icon>
            </template>
            <span>암호같은 파일은 임시 파일일 수 있음!</span>
          </v-tooltip>
        </v-col>
        <v-col class="d-flex justify-center">
          <v-card-actions>
            <v-btn
              class="mt-2"
              color="light-green lighten-1"
              @click="acceptTable"
              >checkAlert</v-btn
            >
          </v-card-actions>
        </v-col>
      </v-row>
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
    const URL = "http://127.0.0.1:80/createThread/thread";
    console.log("post time and abnormal detect");
    axios.get(URL).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>
