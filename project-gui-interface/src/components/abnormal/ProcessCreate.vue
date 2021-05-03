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
    <!--This part appear when user Click-->
    <v-overlay :value="overlay">
      <v-card min-width="800">
        <v-list class="transparent">
          <v-list-item>
            <v-list-item-title>FileName</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.originalFileName }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>fileVersion</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.fileVersion }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>company</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.company }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>product</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.product }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>description</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.description }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>image</v-list-item-title>

            <v-subheader>
              {{ overlayData.image }}
            </v-subheader>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>processId</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.processId }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>parentImage</v-list-item-title>

            <v-subheader>
              {{ overlayData.parentImage }}
            </v-subheader>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>parentProcessId</v-list-item-title>

            <v-list-item-subtitle class="text-right">
              {{ overlayData.parentProcessId }}
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>
        <v-card-actions>
          <v-row>
            <v-col>
              <v-btn
                color="grey darken-2 ml-6 mb-3"
                @click="overlay = !overlay"
              >
                Close
              </v-btn>
            </v-col>
            <v-spacer></v-spacer>
            <v-col>
              <v-btn color="grey darken-2 ml-3 mb-3" @click="hashCheckClick">
                HashCheck
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
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
          :date="date"
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
    </v-overlay>
  </v-container>
</template>

<script>
import userList from "../common/userlist";
import dateSlider from "../common/dateSlider.vue";
import DataTable from "../chart/dataTable.vue";
import MaliciousCheck from "../chart/maliciousCheck.vue";
import MaliciousResult from "../chart/maliciousResult.vue";
import MalicousDialog from "../common/malicousDialog.vue";
export default {
  components: {
    userList,
    dateSlider,
    DataTable,
    MaliciousCheck,
    MaliciousResult,
    MalicousDialog,
  },
  data: () => ({
    dialog: false,
    positives: 0,
    value: 100,
    total: 100,
    date: "",
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
    hashCheckClick() {
      this.$data.hashValue = /SHA256=(.+),/.exec(
        this.$data.overlayData.hashes
      )[1];
    },
    hashValuecheck() {
      this.error = false;
      if (this.hashValue != "") {
        this.loading = true;
        this.check = [];
        this.check2 = [];
        this.alert = false;
        this.$http
          .get("/dnsquery/check", {
            params: {
              hash: this.$data.hashValue,
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
</script>
