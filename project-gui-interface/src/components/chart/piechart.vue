<!--Using Chart js-->
<script>
import { Pie } from "vue-chartjs";
export default {
  extends: Pie,
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
        text: "fildDown Count by agent",
      },
    },
  }),
  mounted() {
    console.log("piechart Comeon!");
    console.log(this.chartdata);
    let data = {
      datasets: [{ data: [], backgroundColor: [] }],
      labels: [],
    };
    for (let i = 0; i < this.chartdata.length; i++) {
      data.datasets[0].data.push(this.chartdata[i].data);
      data.labels.push(this.chartdata[i].label);
      data.datasets[0].backgroundColor.push(this.chartdata[i].backgroundColor);
    }
    console.log(data);
    this.renderChart(data, this.statusOptions);
  },
};
</script>