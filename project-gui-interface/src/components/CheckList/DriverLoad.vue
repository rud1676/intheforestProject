<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="800" color="light-green lighten-4">
      <v-card-title>Driver Load 이벤트 감지</v-card-title>

        <user-list/>
        <date-slider @onload="pload" @finishload="pload" @submitEvent="eventchangt" :url="apiurl"/>
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
          @click:row="showimg"
          loading-text="wait a moment"
          class="elevation-1"
        ></v-data-table>
      </v-card>
      <v-divider class="mx-5 mt-4"></v-divider>
            <v-alert
      border="top"
      colored-border
      type="info"
      elevation="2"
    >
      if Signature is Revoke, Driver Corp is None. Click row and get Driver image path.
    </v-alert>
    </v-card>
    <v-snackbar
      v-model="snackbar"
      multi-line
      timeout = -1
    >
      {{Image}}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from "axios";
import userList from "../common/userlist"
import dateSlider from '../common/dateSlider.vue';
export default {
  components:{
    userList,
    dateSlider
  },
  data: () => ({
    search: "",
    Image:"",
    load: true,
    snackbar: false,
    alertOn: "unknown",
    apiurl:"/driverload/event",
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
      { text: "Driver Cop.", value: "driver" },
      { text: "SignatureIs...", value: "sigstate" },
    ],
  }),
  methods: {
    showimg(image){
      this.$data.Image= image.imageLoad;
      this.$data.snackbar = true;
    },
    pload(load){
      this.$data.load =load;
    },
    eventchangt(data){
      this.$data.events = data;
      console.log(this.$data.events)
    }
  },
  mounted() {
    axios.post(URL,{"date":7}).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>
