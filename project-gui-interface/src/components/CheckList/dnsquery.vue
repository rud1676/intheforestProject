<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>Dns Query 리스트</v-card-title>
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Filter about user, program, query"
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
      <v-alert
      icon="mdi-shield-lock-outline"
      prominent
      text
      type="info"
    >
      MALICIOUS DNS TRAFFIC Check.
      <v-divider
        class="my-4 info"
        style="opacity: 0.22"
      ></v-divider>
      <v-row
        align="center"
        no-gutters
      >
      <v-col class="grow">
          Iodine tool detections(High rate of null requests), Do - Exfiltration(High rate of txt requests), Detect queries with base64 encoded strings, Detect Backdoor using DNS TXT queries.
        </v-col>
        <v-spacer></v-spacer>
      <div>
          <v-btn
            color="info"
            outlined
             @click="alert = !alert">
            Check            
          </v-btn>          
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
      <iframe width="100%" height="600px" :src="url"></iframe>
    </v-alert>
    <v-divider class="mx-5 mt-4"></v-divider>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    alert: false,
    url: "virustotal.com",
    search: "",
    load: true,
    events: [],
    check: [], //timestamp, name, rtype, query
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        filterable: false,
        sortable: false,
        value: "timestamp"
      },
      { text: "Hostname", value: "name" },
      { text: "Program", value: "image" },
      { text: "Queryname", value: "query" },
      {text: "Record Type", value: "record"},
    ],
  }),
  methods: {

  },
  mounted() {
    const URL1 = this.$store.state.pyurl+"/dnsquery/dnsquery";
    axios.get(URL1).then((result) => {
      this.$data.events = result.data;
      this.$data.load = false;
    });

    const URL2 = this.$store.state.pyurl+"/dnsquery/check";
    axios.get(URL2).then((result)=>{
      this.$data.check = result.data;
    });

  }
  

};
</script>
