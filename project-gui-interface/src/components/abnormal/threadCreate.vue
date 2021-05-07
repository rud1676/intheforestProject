<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>프로세스가 만든 쓰레드 감지!</v-card-title>
      <userlist></userlist>
      <date-slider @transAgoDate="getThreadEvent"></date-slider>
      <data-table
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        title="USB감지"
      ></data-table>
      <v-divider class="mx-5 mt-4"></v-divider>
    </v-card>
  </v-container>
</template>

<script>
import userlist from "../common/userlist.vue";
import DateSlider from "../common/dateSlider.vue";
import DataTable from "../chart/dataTable.vue";
export default {
  components: { userlist, DateSlider, DataTable },
  data: () => ({
    search: "",
    load: true,
    filter: "",
    events: [],
    headers: [
      { text: "Source", value: "source" },
      { text: "Target", value: "target" },
      { text: "name", value: "name" },
    ],
  }),
  methods: {
    getThreadEvent() {
      this.$http
        .post("/createThread/thread", { date: this.$store.state.date })
        .then((result) => {
          this.$data.events = result.data;
          this.$data.load = false;
        });
    },
  },
  mounted() {
    this.getThreadEvent();
  },
};
</script>
