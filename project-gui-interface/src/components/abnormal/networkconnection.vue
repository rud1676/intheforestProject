<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>네트워크 연결 프로세스 감지 리스트</v-card-title>
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
            label="Filter about user, program"
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
          item-key="id"
          :show-expand="true"
          :single-expand="true"
          @item-expanded="test"
          loading-text="wait a moment"
          class="elevation-1"
        >
          <template v-slot:expanded-item="{ headers }">
            <td class="pa-3" :colspan="headers.length">
              <v-data-table
                class="elevation-2"
                :headers="expandHeaders"
                :loading="loadexpand"
                loading-text="wait a moment"
                :items="expandEvents"
              >
                <template v-slot:top>
                  <v-toolbar flat color="white">
                    <v-toolbar-title>상세한 페이지</v-toolbar-title>
                  </v-toolbar>
                </template>
              </v-data-table>
            </td>
          </template>
        </v-data-table>
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
            <span>암호같은 파일은 임시 파일일 수 있음!</span>
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
    dateSlider,
  },
  data: () => ({
    search: "",
    load: true,
    apiurl: "/networkConnection/process",
    events: [],
    loadexpand: true,
    headers: [
      { text: "Time", value: "time", sortable: true },
      { text: "Hostname", value: "agent" },
      { text: "Path", value: "image" },
      { text: "count", value: "count" },
    ],
    expandHeaders: [
      { text: "time", value: "time" },
      { text: "destIP", value: "destIP" },
      { text: "destPort", value: "destPort" },
      { text: "sourIP", value: "sourIP" },
      { text: "sourPort", value: "sourPort" },
      { text: "ruleName", value: "ruleName" },
      { text: "protocol", value: "protocol" },
    ],
    expandEvents: [],
    dateForExpand: 0,
  }),
  methods: {
    test({ item, value }) {
      this.$data.loadexpand = true;
      const URL = this.$store.state.pyurl + "/networkConnection/imageevent";
      axios
        .post(URL, {
          date: item.date,
          agent: item.agent,
          image: item.image,
        })
        .then((result) => {
          this.$data.expandEvents = result.data;
          console.log(this.$data.expandEvents);
          this.$data.loadexpand = false;
        });
    },
    pload(load) {
      this.$data.load = load;
    },
    eventchangt(data) {
      this.$data.events = data;
      console.log(this.$data.events);
    },
    transdate(child) {
      this.$data.dateForExpand = child;
    },
  },
  mounted() {
    const URL = this.$store.state.pyurl + this.$data.apiurl;
    axios.post(URL, { date: this.$store.state.date }).then((result) => {
      console.log(this.$store.state.date);
      console.log(result.data);
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>