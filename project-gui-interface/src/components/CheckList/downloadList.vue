<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>파일 다운로드 리스트</v-card-title>
      <user-list/>
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
    </v-card>
    <v-snackbar
      v-model="snackbar"
      multi-line
      timeout = -1
      max-width="1500px"
      class="custom"
      bottom="true"
      vertical="true"
    >
      {{url}}
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
export default {
  components:{
    userList
  },
  data: () => ({
    snackbar: false,
    url:"",
    search: "",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        value: "timestamp"
      },
      { text: "Hostname", value: "name" },
      { text: "Program", value: "image" },
      { text: "Filename", value: "file" }
    ]
  }),
  methods: {
    showurl(items){
      this.$data.url = items.url
      this.$data.snackbar = true;
    }
  },
  mounted() {
    const URL = this.$store.state.pyurl+"/filedown/filestream";
    console.log("post time and abnormal detect");
    axios.get(URL).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });
  }
};
</script>