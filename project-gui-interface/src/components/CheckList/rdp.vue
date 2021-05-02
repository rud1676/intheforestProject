<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>원격 데스크톱 클라이언트 사용 내역</v-card-title>
      <userlist></userlist>
      <date-slider @transAgoDate="getAllEventDate"></date-slider>
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
            <span>ChromeDesktop과 윈도우 RDP사용여부를 감지합니다!</span>
          </v-tooltip>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import DataTable from "../chart/dataTable.vue";
import DateSlider from "../common/dateSlider.vue";
import Userlist from "../common/userlist.vue";
export default {
  components: { DateSlider, DataTable, Userlist },
  data: () => ({
    filter: true,
    search: "",
    DateSlideroad: true,
    events: [],
    load: false,
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        value: "time",
      },
      { text: "Hostname", value: "agent" },
      { text: "description", value: "desc" },
    ],
    apiurl: "/rdp/get",
  }),
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      this.getRDPevent();
    },
    getRDPevent() {
      const URL = this.$store.state.pyurl + this.$data.apiurl;
      console.log("post time and abnormal detect");
      this.$http.post(URL, { date: this.$store.state.date }).then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
    },
  },
  mounted() {
    this.getRDPevent();
  },
};
</script>
