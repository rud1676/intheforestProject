<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1200" color="light-green lighten-4">
      <v-card-title>Driver Load 이벤트 감지</v-card-title>
      <user-list />
      <date-slider @transAgoDate="getAllEventDate" />
      <data-table
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        @ClickEvent="showimg"
        title="USB감지"
      ></data-table>
      <v-divider class="mx-5 mt-4"></v-divider>
      <v-alert border="top" colored-border type="info" elevation="2">
        if Signature is Revoke, Driver Corp is None. Click row and get Driver
        image path.
      </v-alert>
    </v-card>
    <v-snackbar v-model="snackbar" multi-line timeout="-1">
      {{ Image }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import userList from "../common/userlist";
import dateSlider from "../common/dateSlider.vue";
import DataTable from "../chart/dataTable.vue";
export default {
  components: {
    userList,
    dateSlider,
    DataTable,
  },
  data: () => ({
    search: "",
    filter: true,
    Image: "",
    load: true,
    snackbar: false,
    alertOn: "unknown",
    apiurl: "/driverload/event",
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "time",
      },
      { text: "Hostname", value: "agent" },
      { text: "Driver Cop.", value: "driver" },
      { text: "SignatureIs...", value: "sigstate" },
    ],
  }),
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      this.$http
        .post(this.$data.apiurl, { date: this.$store.state.date })
        .then((result) => {
          this.$data.events = result.data;
          this.$data.load = false;
        });
    },
    showimg(image) {
      this.$data.Image = image.imageLoad;
      this.$data.snackbar = true;
    },
    eventchangt(data) {
      this.$data.events = data;
      console.log(this.$data.events);
    },
  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
