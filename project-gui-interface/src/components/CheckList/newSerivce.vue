<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>일주일 간 서비스 설치 내역</v-card-title>
      <user-list />
      <date-slider
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
            label="Hostname, service, path"
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
            <span>wi-fi 뿐만 아니라 LAN연결도 잡아냄!</span>
          </v-tooltip>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import userList from "../common/userlist";
import dateSlider from "../common/dateSlider.vue";
export default {
  components: {
    userList,
    dateSlider
  },
  data: () => ({
    search: "",
    load: true,
    apiurl: "/service/7045",
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
      { text: "기기이름", value: "service" },
      { text: "connect", value: "path" }
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
    axios.post(URL, { date: 7 }).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  }
};
</script>
