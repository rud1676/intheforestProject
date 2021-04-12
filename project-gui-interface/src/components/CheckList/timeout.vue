<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="800" color="light-green lighten-4">
      <v-card-title>근무 시간 외에 컴퓨터 활동 감지</v-card-title>
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Filter about user"
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
      <v-card-title> 근무 시간 설정</v-card-title>
      <v-row justify="space-around" align="center">
        <v-col style="width: 350px; flex: 0 1 auto">
          <h2>Start:</h2>
          <v-time-picker
            color="light-green lighten-1"
            v-model="start"
            :max="end"
          ></v-time-picker>
        </v-col>
        <v-col style="width: 350px; flex: 0 1 auto">
          <h2>End:</h2>
          <v-time-picker
            color="light-green lighten-1"
            v-model="end"
            :min="start"
          ></v-time-picker>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-card-actions>
            <v-btn
              class="mt-2"
              color="light-green lighten-1"
              @click="acceptTable"
              >checkAlert</v-btn
            >
          </v-card-actions>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    start: "10:00",
    end: "19:00",
    search: "",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "timestamp"
      },
      { text: "Hostname", value: "name" }
    ]
  }),
  methods: {
    acceptTable: function () {
      alert("적용하였습니다!");
      const URL = "http://127.0.0.1:80/detect/abnormal";
      axios
        .post(URL, {
          data: {
            start: this.$data.start,
            end: this.$data.end
          }
        })
        .then((result) => {
          this.$data.events = result.data;
          this.$data.load = false;
        });
    }
  },
  mounted() {
    const URL = this.$store.state.pyurl+"/detect/abnormal";
    console.log("post time and abnormal detect");
    axios
      .post(URL, {
        data: {
          start: this.$data.start,
          end: this.$data.end
        }
      })
      .then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
  }
};
</script>
