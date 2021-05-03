<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>wi-fi 연결 내역</v-card-title>
      <user-list />
      <date-slide @transAgoDate="getAllEventDate" />
      <data-table
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        title="Get NetWork Connnect"
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
            <span>wi-fi 뿐만 아니라 LAN연결도 잡아냄! => 랜카드 연결내역</span>
          </v-tooltip>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import userList from "../common/userlist";
import dateSlide from "../common/dateSlider";
import dataTable from "../chart/dataTable";
export default {
  components: {
    userList,
    dateSlide,
    dataTable,
  },
  data: () => ({
    filter: true,
    search: "",
    apiurl: "/wificonnection/wifi",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        value: "time",
      },
      { text: "Hostname", value: "agent" },
      { text: "기기이름", value: "name" },
      { text: "connect", value: "connect" },
    ],
  }),
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      this.$http
        .post(this.$data.apiurl, { date: this.$store.state.date })
        .then((result) => {
          console.log(result.data);
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
