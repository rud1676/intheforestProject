<!--Using Chart js-->
<script>
import { Bar } from "vue-chartjs";
export default {
  extends: Bar,
  props: {
    chartdata: {
      type: Array,
      default: () => null,
    },
  },
  data: () => ({
    statusOptions: {
      responsive: true,
      maintainAspectRatio: false,
      title: {
        position: "top",
        display: true,
        text: "App Log PieChart",
      },
    },
  }),
  mounted() {
    console.log("piechart Comeon!");
    //console.log(this.chartdata);
    let data = {
      datasets: [{ label: "AGENT LOG COUNT", data: [], backgroundColor: [] }],
      labels: [],
    };
    for (let i = 0; i < this.chartdata.length; i++) {
      data.datasets[0].data.push(this.chartdata[i].data);
      data.labels.push(this.chartdata[i].label);
      data.datasets[0].backgroundColor.push(this.chartdata[i].backgroundColor);
    }
    this.renderChart(data, this.statusOptions);
    this.$refs.id = "hi";
  },
};
</script>