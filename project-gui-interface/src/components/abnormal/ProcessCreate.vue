<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1200" color="light-green lighten-4">
      <v-card-title>ProcessCreate 이벤트</v-card-title>
      <user-list />
      <date-slider @transAgoDate="getAllEventDate" />
      <data-table-detail
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        @ClickEvent="hashCheckClick"
        title="test Event"
      ></data-table-detail>
      <v-divider class="mx-5 mt-4"> </v-divider>
    </v-card>
    <!--This part appear when user Click-->
    <v-card min-width="800">
      <malicious-check
        title="Malicious HashValue Check"
        labeling="HashValue"
        :url="hashValue"
        :loading="loading"
        :error="error"
        @dnscheck="hashValuecheck"
      ></malicious-check>
      <malicious-result
        :alert="alert"
        :value="value"
        :positives="positives"
        :total="total"
        :url="hashValue"
        :check="check"
        :check2="check2"
        @close="close"
      ></malicious-result>
      <malicous-dialog
        :dialog="dialog"
        @dialog="dialogAccept"
      ></malicous-dialog>
    </v-card>
  </v-container>
</template>

<script>
import userList from "../common/userlist";
import dateSlider from "../common/dateSlider.vue";
import DataTableDetail from "../chart/dataTableDetail.vue";
import MaliciousCheck from "../chart/maliciousCheck.vue";
import MaliciousResult from "../chart/maliciousResult.vue";
import MalicousDialog from "../common/malicousDialog.vue";
export default {
  components: {
    userList,
    dateSlider,
    DataTableDetail,
    MaliciousCheck,
    MaliciousResult,
    MalicousDialog,
  },
  data: () => ({
    dialog: false,
    positives: 0,
    value: 100,
    total: 100,
    check: [],
    check2: [],
    error: false,
    loading: false,
    alert: false,
    overlay: false,
    search: "",
    filter: true,
    Image: "",
    load: true,
    snackbar: false,
    alertOn: "unknown",
    apiurl: "/process/getEvent",
    events: [],
    hashValue: "",
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
    test() {
      return 0;
    },
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
    close() {
      this.$data.alert = false;
    },
    showimg(image) {
      this.$data.Image = image.imageLoad;
      this.$data.overlayData = image;
      this.$data.overlay = true;
    },
    dialogAccept() {
      this.$data.dialog = false;
    },
    hashCheckClick(hash) {
      console.log(hash);
      this.$data.hashValue = /SHA256=(.+),/.exec(hash)[1];
    },
    hashValuecheck() {
      this.error = false;
      if (this.hashValue != "") {
        console.log(this.$data.hashValue);
        this.loading = true;
        this.check = [];
        this.check2 = [];
        this.alert = false;
        this.$http
          .post("/process/check", {
            hash: this.$data.hashValue,
          })
          .then((result) => {
            this.total = result.data[0].total;
            this.positives = result.data[0].positives;
            this.value = ((this.total - this.positives) / this.total) * 100;
            delete result.data[0];
            this.check = result.data.slice(1, this.total / 2 + 1);
            this.check2 = result.data.slice(this.total / 2 + 1);
            console.log(this.check);
            console.log(this.check2);
            this.loading = false;
            this.alert = true;
          })
          .catch((error) => {
            this.error = true;
            this.dialog = true;
            console.log(error);
          });
      }
    },
  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
