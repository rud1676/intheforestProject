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
        title="ProcessCreate Event"
      ></data-table>
      <v-divider class="mx-5 mt-4"> </v-divider>
    </v-card>
    <v-overlay :value="overlay">
      <v-btn class="white--text" color="teal" @click="overlay = false">
        {{ overlayData.hashes }}
      </v-btn>
    </v-overlay>
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
    overlay: true,
    search: "",
    filter: true,
    Image: "",
    load: true,
    snackbar: false,
    alertOn: "unknown",
    apiurl: "/process/getEvent",
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: true,
        value: "time",
      },
      { text: "Hostname", value: "agent" },
      { text: "FileName", value: "originalFileName" },
      { text: "description", value: "description" },
    ],
    overlayData: {},
  }),
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      const URL = this.$store.state.pyurl + this.$data.apiurl;
      this.$http.post(URL, { date: this.$store.state.date }).then((result) => {
        console.log(result.data);
        this.$data.events = result.data;
        this.$data.load = false;
      });
    },
    showimg(image) {
      this.$data.Image = image.imageLoad;
      this.$data.overlayData = image;
      this.$data.overlay = true;
    },
  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
