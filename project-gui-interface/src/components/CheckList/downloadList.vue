<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>파일 다운로드 리스트</v-card-title>
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
            label="Filter about user, filename, program"
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
          @click:row="showurl"
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
        close-icon="$cancel"
      >
        when you click row, page show direct download url
      </v-alert>
    </v-card>
    <v-snackbar v-model="snackbar" multi-line timeout="-1">
      {{ url }}
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
export default {
  components: {
    userList,
    dateSlider,
  },
  data: () => ({
    snackbar: false,
    apiurl: "/filedown/filestream",
    url: "",
    search: "",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        value: "timestamp",
      },
      { text: "Hostname", value: "name" },
      { text: "Program", value: "image" },
      { text: "Filename", value: "file" },
    ],
  }),
  methods: {
    showurl(items) {
      this.$data.url = items.url;
      this.$data.snackbar = true;
    },
    pload(load) {
      this.$data.load = load;
    },
    eventchangt(data) {
      this.$data.events = data;
      console.log(this.$data.events);
    },
  },
  mounted() {
    this.$http.post(this.$data.apiurl, { date: 7 }).then((result) => {
      console.log(result.data);
      this.$data.events = result.data;
      this.$data.load = false;
    });
  },
};
</script>