
<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>통합 대시보드</v-card-title>
      <agent />
      <date-slider @transAgoDate="getAllEventDate"></date-slider>
      <v-card-title class="text-center"
        >TimeLine Status about agents</v-card-title
      >
      <line-chart v-if="reRender" :chartdata="AgentStatusEvent"></line-chart>
      <v-card-title class="text-center">APP Usage Log Count TOP20</v-card-title>
      <pie-chart
        :height="h"
        v-if="reRender"
        :chartdata="appUseLogCount"
      ></pie-chart>
      <v-card-title class="text-center">Log Count by AGENT</v-card-title>
      <bar-chart v-if="reRender" :chartdata="agentAlllogCount"></bar-chart>
      <v-row dense>
        <v-col>
          <data-table
            v-if="reRender"
            title="파일 다운로드 수"
            :items="downLoadCountData"
          ></data-table>
        </v-col>
        <v-col>
          <data-table
            v-if="reRender"
            title="기간 동안 새롭게 서비스 설치한 갯수"
            :items="serviceinstallcount"
          ></data-table>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <data-double-table
            v-if="reRender"
            title="설치된 서비스 수"
            subtitle="설치된 서비스 회사별로 보기"
            :items="pakageEventCount"
          ></data-double-table>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <data-table
            v-if="reRender"
            title="DNS Query IN Browser TOP 80"
            :items="dns_in_browser_logCount"
          ></data-table>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
//부모에서 Log정보 다 받기 - agent actives 받아오기
import agent from "../common/userlist";
import DateSlider from "../common/dateSlider.vue";
import LineChart from "../chart/Linechart";
import PieChart from "../chart/piechart";
import DataTable from "../chart/dataTable";
import DataDoubleTable from "../chart/dataDoubleTable"; //this component need for id column!
import BarChart from "../chart/bar-chart.vue";

export default {
  components: {
    agent,
    LineChart, //timeline status about agents
    DateSlider,
    PieChart, //all event load!
    DataTable,
    DataDoubleTable,
    BarChart,
  },
  data: () => {
    return {
      h: 600,
      linechartEvents: null,
      showActiveTime: false,
      AgentStatusEvent: [], //StatusChart data
      downLoadCountData: [], //donwload count data
      serviceinstallcount: [], //new service install event coint
      pakageEventCount: [], //wazuh api => pakagelist
      appUseLogCount: [], //Process create for Product name
      agentAlllogCount: [], //All log categorize by AGNET
      dns_in_browser_logCount: [], //DNS LOG
      reRender: false,
    };
  },
  methods: {
    makeRandColor: () => {
      return "#" + Math.round(Math.random() * 0xffffff).toString(16);
    },
    getAllEventDate: async function () {
      this.$data.reRender = false;
      //console.log("call: getAllActive");
      await this.getAllActiveEvent();
      //console.log("call: downLoadCount");
      await this.downLoadCount();
      //console.log("call: serviceInstallCount");
      await this.serviceInstallCount();
      //console.log("In await, async : ", this.$data.downLoadCountData);
      await this.getAppLogCount();
      await this.pakageCountByAgent();
      await this.AgentLogCount();
      await this.DNSLogCount();
      this.$data.reRender = true;
    },
    //LineChart에 Activate 로그를 넣어줌!
    getAllActiveEvent: async function () {
      this.AgentStatusEvent = [];
      const URL = this.$store.state.pyurl + "/maindash/agentactive";
      const moment = this.$moment;
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          let datas = result.data; //data들을 datas로 명칭
          for (let i = 0; i < datas.length; i++) {
            //result.data.agent는 label에 넣자!
            let data = []; //data들을 받기위한 그릇
            let dataset = datas[i].data; // 각 데이터를 dataset이라 칭함
            let step = 1; //날짜가 많아지면 너무많이 보여주므로 몇개는 생략하기 위함
            if (this.$store.state.date >= 30) step = 7;
            else if (this.$store.state.date >= 25) step = 6;
            else if (this.$store.state.date >= 20) step = 5;
            else if (this.$store.state.date >= 15) step = 4;
            else if (this.$store.state.date >= 10) step = 3;
            else if (this.$store.state.date >= 5) step = 2;
            //각 데이터의 날짜타입으로 형변환
            for (let j = 0; j < dataset.length; j += step) {
              data.unshift({
                x: moment(dataset[j].time).toDate(),
                y: dataset[j].status,
              });
            }
            //데이터를 Linechart에 넣어주기 위해 형식을 맞춤
            this.$data.AgentStatusEvent.push({
              label: datas[i].agent,
              borderColor: this.makeRandColor(),
              fill: false,
              steppedLine: true,
              data: data,
            });
          }

          //차트를 다시 로드하기 위한 reRender값
        });
      //for Test
    },
    //download count 를 agent 마다 있는 이벤트를 받아오는 api call.
    downLoadCount: async function () {
      this.$data.downLoadCountData = [];
      const URL = this.$store.state.pyurl + "/maindash/downCount";
      console.log("Inside downLoadCount");
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          console.log("Inside downLoadCount - axios");
          for (let i = 0; i < result.data.length; i++) {
            this.$data.downLoadCountData.push({
              label: result.data[i].agent,
              data: result.data[i].count,
            });
          }
          console.log("Inside downLoadCount - axios FINISH!!");
        });
      console.log("Main: ", this.$data.downLoadCountData);
    },
    //Service 설치 이벤트 카운트를 받아와서 보여줍니다!
    serviceInstallCount: async function () {
      this.$data.serviceinstallcount = [];
      const URL = this.$store.state.pyurl + "/maindash/serviceinstallcount";
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          for (let i = 0; i < result.data.length; i++) {
            this.$data.serviceinstallcount.push({
              label: result.data[i].agent,
              data: result.data[i].count,
            });
          }
        });
    },
    pakageCountByAgent: async function () {
      const URL = this.$store.state.pyurl + "/maindash/getPackageCount";
      await this.$http.get(URL).then((result) => {
        this.$data.pakageEventCount = result.data;
        console.log(result.data);
      });
    },
    getAppLogCount: async function () {
      this.$data.appUseLogCount = [];
      const URL = this.$store.state.pyurl + "/maindash/getAppLogCount";
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          for (let i = 0; i < result.data.length; i++) {
            this.$data.appUseLogCount.push({
              label: result.data[i].label,
              data: result.data[i].data,
              backgroundColor: this.makeRandColor(),
            });
          }
        });
    },
    AgentLogCount: async function () {
      this.$data.agentAlllogCount = [];
      const URL = this.$store.state.pyurl + "/maindash/AgentLogCount";
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          console.log(result.data);
          for (let i = 0; i < result.data.length; i++) {
            this.$data.agentAlllogCount.push({
              label: result.data[i].label,
              data: result.data[i].data,
              backgroundColor: this.makeRandColor(),
            });
          }
        });
    },
    DNSLogCount: async function () {
      this.$data.dns_in_browser_logCount = [];
      const URL = this.$store.state.pyurl + "/maindash/DNSLogCount";
      await this.$http
        .post(URL, { date: this.$store.state.date })
        .then((result) => {
          console.log(result.data);
          for (let i = 0; i < result.data.length; i++) {
            this.$data.dns_in_browser_logCount.push({
              label: result.data[i].label,
              data: result.data[i].data,
              backgroundColor: this.makeRandColor(),
            });
          }
        });
    },
  },

  mounted: function () {
    //this.DNSLogCount();
  },
};
</script>

<style>
</style>