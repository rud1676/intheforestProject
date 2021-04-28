<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <userlist @clickEvent="AgentClick"></userlist>
      <v-divider></v-divider>
      <data-table
        :headers="PortHeaders"
        :items="PortDataTable"
        :title="agentName + '의 사용중인 Port정보'"
      ></data-table>
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
    };
  },
  methods: {
    AgentClick: function (agentName) {
      //this.GetPortData(agentName);
      this.GetProcessData(agentName);
    },
    GetPortData: function (a) {
      this.$data.agentName = a;
      const URL = this.$store.state.pyurl + "/agentdash/scanPortData";
      this.$http.post(URL, { agent: a }).then((result) => {
        this.$data.PortDataTable = result.data;
      });
    },
    GetProcessData: function (a) {
      //vmsize size 등 각 필드에 대한 연구
      this.$data.agentName = a;
      const URL = this.$store.state.pyurl + "/agentdash/scanProcesses";
      this.$http.post(URL, { agent: a }).then((result) => {
        console.log(result);
      });
    },
  },
  mounted() {},
};
</script>