<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>AGENT 대시보드</v-card-title>
      <userlist @clickEvent="AgentClick"></userlist>
      <v-divider></v-divider>
      <v-progress-linear
        v-if="!render"
        v-model="loadvalue"
        color="lime darken-3"
        height="25"
      >
        <template v-slot:default="{ value }">
          <strong>{{ Math.ceil(value) }}%</strong>
        </template>
      </v-progress-linear>
      <v-card-title v-if="render"
        >Last Scan Time is.. {{ scantime }}</v-card-title
      >
      <v-row>
        <v-col>
          <data-table
            v-if="render"
            Ifsearch="true"
            :headers="PortHeaders"
            :items="PortDataTable"
            :title="agentName + '의 사용중인 Port정보'"
          ></data-table>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <data-table
            v-if="render"
            Ifsearch="true"
            :headers="ProcessHeaders"
            :items="ProcessDataTable"
            :title="agentName + '의 사용중인 Process정보'"
          ></data-table>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <data-table
            v-if="render"
            Ifsearch="true"
            :headers="PackageHeaders"
            :items="ScanPackageDataTable"
            :title="agentName + '의 설치된 서비스 목록'"
          ></data-table>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import DataTable from "../chart/dataTable.vue";
import userlist from "../common/userlist.vue";

export default {
  components: { userlist, DataTable },
  data: () => {
    return {
      agentName: "",
      PortHeaders: [
        { text: "내부 아이피", value: "InnerIP" },
        { text: "내부 포트", value: "InnerPort" },
        { text: "외부 아이피", value: "OutIP" },
        { text: "외부 포트", value: "OutPort" },
        { text: "연결 상태", value: "status" },
        { text: "프로토콜", value: "protocol" },
        { text: "프로세스", value: "process" },
      ],
      PortDataTable: [], //getData Used PortName
      ProcessHeaders: [
        { text: "프로세스", value: "process" },
        { text: "PID", value: "PID" },
        { text: "PPID", value: "PPID" },
        { text: "우선순위", value: "priority" },
        { text: "쓰레드 수", value: "InThreads" },
        { text: "SESSION", value: "session" },
        { text: "커멘드라인", value: "Command" },
      ],
      ProcessDataTable: [],
      PackageHeaders: [
        { text: "Program", value: "Program" },
        { text: "Install_Time", value: "Install_time" },
        { text: "Company", value: "Company" },
        { text: "Path", value: "Path" },
      ],
      ScanPackageDataTable: [],
      render: false,
      scantime: null,
      loadvalue: 0,
    };
  },
  methods: {
    AgentClick: async function (agentName) {
      this.$data.render = false;
      this.$data.loadvalue = 0;
      await this.GetPortData(agentName);
      this.$data.loadvalue = 50;
      await this.GetProcessData(agentName);
      this.$data.loadvalue = 100;
      this.ScanPackage(agentName);
      this.$data.render = true;
    },
    GetPortData: async function (a) {
      this.$data.agentName = a;
      await this.$http
        .post("/agentdash/scanPortData", { agent: a })
        .then((result) => {
          this.$data.PortDataTable = result.data;
        });
    },
    ScanPackage: async function (a) {
      this.$data.ScanPackageDataTable = [];
      await this.$http
        .post("/agentdash/ScanPackage", { agent: a })
        .then((result) => {
          this.$data.ScanPackageDataTable = result.data;
        });
    },
    GetProcessData: async function (a) {
      //vmsize size 등 각 필드에 대한 연구
      this.$data.agentName = a;
      await this.$http
        .post("/agentdash/scanProcesses", { agent: a })
        .then((result) => {
          console.log(result.data.time);
          this.$data.scantime = result.data.time;
          this.$data.ProcessDataTable = result.data.result;
        });
    },
  },
  mounted() {},
};
</script>