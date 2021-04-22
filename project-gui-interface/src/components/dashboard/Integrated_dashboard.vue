
<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1400" color="light-green lighten-4">
      <v-card-title>통합 대시보드</v-card-title>
      <agent />
      <date-slider @transAgoDate="getAllEventDate"></date-slider>
      <v-card-title class="text-center">Agent별 status</v-card-title>
      <line-chart v-if="reRender" :chartdata="AgentStatusEvent"></line-chart>
    </v-card>
  </v-container>
</template>

<script>
//부모에서 Log정보 다 받기 - agent actives 받아오기
import agent from "../common/userlist";
import DateSlider from "../common/dateSlider.vue";
import LineChart from "../chart/Linechart";
export default {
  components: {
    agent,
    LineChart,
    DateSlider,
  },
  data: () => {
    return {
      linechartEvents: null,
      showActiveTime: false,
      AgentStatusEvent: [],
      reRender: true,
    };
  },
  methods: {
    makeRandColor: () => {
      return "#" + Math.round(Math.random() * 0xffffff).toString(16);
    },
    getAllEventDate: function () {
      this.$data.reRender = false;
      this.getAllActiveEvent();
    },
    //LineChart에 Activate 로그를 넣어줌!
    getAllActiveEvent: function () {
      this.AgentStatusEvent = [];
      const URL = this.$store.state.pyurl + "/maindash/agentactive";
      const moment = this.$moment;
      this.$http.post(URL, { date: this.$store.state.date }).then((result) => {
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
        this.$data.reRender = true;
      });
      //for Test
      console.log("Activate Status EventGet");
    },
  },

  mounted: function () {},
};
</script>

<style>
</style>