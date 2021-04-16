<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>최근 일주일 wi-fi 연결 내역</v-card-title>
      <user-list />
      <date-slide
        @onload="pload"
        @finishload="pload"
        @submitEvent="eventchangt"
        :url="apiurl"
      />
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Hostname, name, connect"
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
            <span>wi-fi 뿐만 아니라 LAN연결도 잡아냄! => 랜카드 연결내역</span>
          </v-tooltip>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import userList from "../common/userlist";
import dateSlide from "../common/dateSlider";
export default {
  components: {
    userList,
    dateSlide
  },
  data: () => ({
    search: "",
    apiurl: "/wificonnection/wifi",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "time"
      },
      { text: "Hostname", value: "agent" },
      { text: "기기이름", value: "name" },
      { text: "connect", value: "connect" }
    ]
  }),
  methods: {
    pload(load) {
      this.$data.load = load;
    },
    eventchangt(data) {
      this.$data.events = data;
      console.log(this.$data.events);
    }
  },
  mounted() {
    const URL = this.$store.state.pyurl + this.$data.apiurl;
    console.log(URL);
    axios.post(URL, { date: 7 }).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  }
};
</script>
