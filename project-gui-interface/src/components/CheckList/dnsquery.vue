<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>Dns Query 리스트</v-card-title>
      <userlist></userlist>
      <date-slider @transAgoDate="getAllEventDate"></date-slider>
      <data-table
        :headers="headers"
        :items="events"
        :Ifsearch="filter"
        :load="load"
        @ClickEvent="clickurl"
        title="DNS Query about All Agent"
      >
      </data-table>
      <v-divider class="mx-5 mt-4"></v-divider>
      <malicious-check
        :url="url"
        labeling="URL"
        :loading="loading"
        :error="error"
        @dnscheck="dnscheck"
      ></malicious-check>
      <malicious-result
        :alert="alert"
        :value="value"
        :positives="positives"
        :total="total"
        :date="date"
        :url="url"
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
import userlist from "../common/userlist.vue";
import DateSlider from "../common/dateSlider.vue";
import DataTable from "../chart/dataTable.vue";
import MaliciousCheck from "../chart/maliciousCheck.vue";
import MaliciousResult from "../chart/maliciousResult.vue";
import MalicousDialog from "../common/malicousDialog.vue";
export default {
  components: {
    userlist,
    DateSlider,
    DataTable,
    MaliciousCheck,
    MaliciousResult,
    MalicousDialog,
  },
  data: () => ({
    alert: false,
    filter: true,
    error: false,
    dialog: false,
    url: "",
    load: true,
    loading: false,
    events: [],
    check: [], //timestamp, name, rtype, query
    check2: [],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        value: "timestamp",
      },
      { text: "Hostname", value: "name" },
      { text: "Program", value: "image" },
      { text: "Queryname", value: "query" },
    ],
    headers2: [
      { text: "Scans", value: "scans" },
      { text: "Result", value: "clean" },
    ],
    total: 100,
    value: 100,
    positives: 0,
    date: "",
  }),
  computed: {},
  methods: {
    getAllEventDate() {
      this.$data.load = true;
      this.$http
        .post("/dnsquery/dnsquery", { date: this.$store.state.date })
        .then((result) => {
          this.$data.events = result.data;
          this.$data.load = false;
        });
    },
    dialogAccept() {
      this.dialog = false;
    },
    close() {
      this.alert = false;
    },
    clickurl(items) {
      this.$data.url = items.query;
    },
    dnscheck() {
      this.error = false;
      if (this.url != "") {
        this.loading = true;
        this.check = [];
        this.check2 = [];
        this.alert = false;
        this.$http
          .get("/dnsquery/check", {
            params: {
              domain: this.url,
            },
          })
          .then((result) => {
            this.date = result.data[0].date;
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
//이건 adnormal dectection으로 옮겨서 분석할 수 있게 도와주기!
</script>
