<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>일주일 간 서비스 설치 내역</v-card-title>
      <user-list />
      <date-slider @transAgoDate="getAllEventDate" />
      <data-table
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        title="RDP and Chromoting"
      ></data-table>
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
import DataTable from "../chart/dataTable.vue";
export default {
  components: {
    userList,
    dateSlider,
    DataTable,
  },
  data: () => ({
    filter: true,
    search: "",
    load: false,
    apiurl: "/service/7045",
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: true,
        value: "time",
      },
      { text: "Hostname", value: "agent" },
      { text: "패키지이름", value: "service" },
      { text: "설치경로", value: "path" },
    ],
  }),
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      const URL = this.$store.state.pyurl + this.$data.apiurl;
      axios.post(URL, { date: this.$store.state.date }).then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
    },
  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
