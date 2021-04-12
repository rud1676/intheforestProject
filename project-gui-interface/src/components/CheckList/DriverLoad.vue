<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="800" color="light-green lighten-4">
      <v-card-title>Driver Load 이벤트 감지</v-card-title>
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Filter about user"
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
      <v-row>
        <v-col class="d-flex justify-center">
          <v-card-actions>
            <v-badge bordered :color="alertOn" icon="mdi-alert-circle" overlap>
              <v-btn
                class="mt-2"
                color="light-green lighten-1"
                @click="getAlertState"
                >checkAlert</v-btn
              >
            </v-badge>
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
    alertOn: "unknown",
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "timestamp",
      },
      { text: "Hostname", value: "hostname" },
      { text: "Driver Cop.", filterable: false, value: "driver" },
    ],
  }),
  methods: {
    getAlertState: function () {
      const URL = "http://127.0.0.1:80/driverload/alert";
      console.log("get alert state");
      axios.get(URL).then((result) => {
        this.$data.alertOn = result.data;
        console.log(this.$data.alertOn);
      });
    },
  },
  mounted() {
    const URL = this.$store.state.pyurl+"/driverload/event";
    console.log("get Driver Event");
    axios.get(URL).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>
