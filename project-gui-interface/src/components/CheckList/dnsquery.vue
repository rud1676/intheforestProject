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
          <v-col class="grow"> Check domain : 
            <v-text-field
            v-model="url"
            label="URL"
            dense
            
            color ="info"
            clearable
          ></v-text-field>
          </v-col>
          <v-progress-circular
      indeterminate
      color="green"
      :size="70"
      :width="7"
      v-if="loading && !error"
    ></v-progress-circular>
          <v-spacer></v-spacer>
          <div>
            <v-btn color="info" outlined @click="dnscheck"> Check </v-btn>
          </div>
        </v-row>
      </v-alert>
      <v-alert
      v-if="alert"
        :value="alert"
        border="right"
        colored-border
        type="error"
        elevation="2"
      >
      <v-row align="center" no-gutters>
          <v-col class="grow">
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
          </v-col>
        <v-spacer></v-spacer>
    
           <v-btn color="info" outlined @click="close"> Close </v-btn>

        </v-row>
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
      
      <v-dialog
      v-model="dialog"
      width="650"
    >


      <v-card>
        <v-card-title class="headline grey lighten-2">
          Please try again later
        </v-card-title>

        <v-card-text>
          <h2>
          Notice
</h2>
The Public API is limited to 500 requests per day and a rate of 4 requests per minute.
<div>
The Public API must not be used in commercial products, services or business workflows.
</div>
<div>
The Private API returns more threat data and exposes more endpoints.
</div>
The Private API is governed by an SLA that guarantees readiness of data.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
      const URL1 = this.$store.state.pyurl + "/dnsquery/dnsquery";
      this.$http.post(URL1, { date: this.$store.state.date }).then((result) => {
        this.$data.events = result.data;
        this.$data.load = false;
      });
    },
    close(){
      this.alert = false;
    },
    clickurl(items) {
      this.$data.url = items.query;
    },
    dnscheck(){
      this.error = false
      if(this.url != ''){
      this.loading = true
      this.check = []
      this.check2 = []
      this.alert = false;
      const URL2 = this.$store.state.pyurl+"/dnsquery/check";
      this.$http.get(URL2,{
        params:{
          domain: this.url
          }
        }).then((result) => {

      this.date = result.data[0].date;
      this.total = result.data[0].total;
      this.positives = result.data[0].positives;
      this.value = (this.total - this.positives)/this.total*100;
      delete result.data[0];
            this.check = result.data.slice(1, this.total / 2 + 1);
            this.check2 = result.data.slice(this.total / 2 + 1);
            console.log(this.check);
            console.log(this.check2);
            this.loading = false
            this.alert =true;
          }
          ).catch((error) => {
            this.error =true;
            this.dialog = true
            console.log(error)
          });
      }
    }

  },
  mounted() {
    this.getAllEventDate();
  },
};
</script>
