<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="800" color="light-green lighten-4">
      <v-card-title>근무 시간 외에 컴퓨터 활동 감지</v-card-title>
      <user-list />
      <date-slide
        @onload="pload"
        @finishload="pload"
        @submitEvent="eventchangt"
        :url="apiurl"
        :endtime="end"
        :starttime="start"
        who="timeout"
        ref="sumbit"
      />
      <v-card>
        <v-card-title>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon class="pr-3" v-bind="attrs" v-on="on" medium
                >mdi-checkbox-marked-circle</v-icon
              >
            </template>
            <span>보이는 날짜는 -1d startime~ d endtime 에서 endday임</span>
          </v-tooltip>
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
              >Submit</v-btn
            >
          </v-card-actions>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import userList from "../common/userlist";
import dateSlide from "../common/dateSlider";
export default {
  components: {
    userList,
    dateSlide
  },
  data: () => ({
    start: "10:00",
    end: "19:00",
    search: "",
    apiurl: "/timeout/",
    load: true,
    events: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "date"
      },
      { text: "Hostname", value: "agent" }
    ]
  }),
  methods: {
    pload(load) {
      this.$data.load = load;
    },
    eventchangt(data) {
      this.$data.events = data;
      console.log(this.$data.events);
    },
    acceptTable: function () {
      alert("적용하였습니다!");
      this.$refs.sumbit.submit__for_timeoutcomponent(); //자식(dataslider에 있는 거 불러오기)
    },
    submit() {
      this.onload();
      const URL = this.$store.state.pyurl + this.$data.apiurl;
      this.$http
        .post(URL, {
          data: {
            start: this.$data.start,
            end: this.$data.end,
            date: this.$data.slider.val
          }
        })
        .then((result) => {
          this.$data.events = result.data;
          this.finishload();
        });
    }
  },
  mounted() {
    const URL = this.$store.state.pyurl + this.$data.apiurl;
    axios
      .post(URL, {
        data: {
          start: this.$data.start,
          end: this.$data.end,
          date: this.$store.state.date
        }
      })
      .then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
  }
};
</script>
