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
        title="RDP and Chromoting"
      >
      </data-table>
      <v-divider class="mx-5 mt-4"></v-divider>
      <v-alert icon="mdi-shield-lock-outline" prominent text type="info">
        MALICIOUS DNS TRAFFIC Check.
        <v-divider class="my-4 info" style="opacity: 0.22"></v-divider>
        <v-row align="center" no-gutters>
          <v-col class="grow"> Check domain : {{ url }} </v-col>
          <v-spacer></v-spacer>
          <div>
            <v-btn color="info" outlined @click="dnscheck"> Check </v-btn>
          </div>
        </v-row>
      </v-alert>
      <v-alert
        :value="alert"
        border="right"
        colored-border
        type="error"
        elevation="2"
      >
        <v-progress-circular
          :rotate="360"
          :size="100"
          :width="15"
          :value="value"
          color="teal"
        >
          {{ positives }} / {{ total }}
        </v-progress-circular>
        | {{ date }} UTC a moment ago
        <div>{{ url }}</div>
        <v-row no-gutters>
          <v-col>
            <v-card>
              <v-simple-table dense>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th>Scans</th>
                      <th>Result</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in check" :key="item.scans">
                      <td>{{ item.scans }}</td>
                      <td>
                        <v-icon v-if="item.clean === 'clean site'" color="green"
                          >mdi-check-circle-outline</v-icon
                        >
                        <v-icon v-else>mdi-help</v-icon>
                        {{ item.clean }}
                      </td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-card>
          </v-col>

          <v-col>
            <v-card>
              <v-simple-table dense>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th>Scans</th>
                      <th>Result</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in check2" :key="item.scans">
                      <td>{{ item.scans }}</td>
                      <td>
                        <v-icon v-if="item.clean === 'clean site'" color="green"
                          >mdi-check-circle-outline</v-icon
                        >
                        <v-icon v-else>mdi-help</v-icon>
                        {{ item.clean }}
                      </td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-card>
          </v-col>
        </v-row>
      </v-alert>
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
    alert: false,
    filter: true,
    url: "",
    load: true,
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
      { text: "Record Type", value: "record" },
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
      const URL1 = this.$store.state.pyurl + "/dnsquery/dnsquery";
      this.$http.post(URL1, { date: this.$store.state.date }).then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
    },
    clickurl(items) {
      this.$data.url = items.query;
    },
    dnscheck() {
      if (this.url != "") {
        this.alert = !this.alert;
        const URL2 = this.$store.state.pyurl + "/dnsquery/check";
        this.$http
          .get(URL2, {
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
            // for(var i = 0; i < result.data.length;i++){
            //   if(result.data[i].clean == "clean site"){
            //     result.data[i].clean =
            //   }

            // };
            this.check = result.data.slice(1, this.total / 2 + 1);
            this.check2 = result.data.slice(this.total / 2 + 1);
            console.log(this.check);
            console.log(this.check2);
          });
      }
    },
  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
