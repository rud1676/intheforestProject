<template>
  <div>
    <GChart type="LineChart" :data="chartData" :options="chartOptions" />
    <v-btn @click="callLineChartData">동기화...ㅠ</v-btn>
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
export default {
  props: {
    url: {
      type: String,
      default: "",
    },
  },
  components: {
    GChart,
  },
  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [],
      chartOptions: {
        chart: {
          title: "Company Performance",
          curveType: 'function',
          subtitle: "Sales, Expenses, and Profit: 2014-2017",
          vAxis: {
            viewWindow: {
              ticks: []
            }
          }
        },
      },
      agents: [],
    };
  },
  methods: {
    callLineChartData: async function(){
    URL = this.$store.state.pyurl + "/driverload/count";
    let events=[];
    await this.$http
    .post(URL, { date: this.$store.state.date })
    .then((result) => {
      events = result.data;
    });
    
    await events.forEach((e,i,a) => {
        console.log(e,i);
        if(i==0) console.log(i);
        else{
          e[0] = new Date(e[0])
        }
      });
    this.$data.chartData = events;
    
    }
  }
}
</script>
