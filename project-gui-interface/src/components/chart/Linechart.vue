<!--Using Chart js-->
<script>
import { Line } from "vue-chartjs";
export default {
  extends: Line,
  props: {
    chartdata: {
      type: Array,
      default: () => null,
    },
    agoday: {
      type: Number,
      default: 0,
    },
  },
  data: () => ({
    statusOptions: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          text: "Chart.js Time Scale",
          display: true,
        },
      },
      scales: {
        xAxes: [
          {
            type: "time",
            time: {
              unit: "hour",
              unitStepSize: 12,
              tooltipFormat: "MMM D, h:mm:ss a",
              displayFormats: {
                hour: "MMM D, h:mm A",
              },
            },
          },
        ],
        yAxes: {
          title: {
            display: true,
            text: "value",
          },
        },
      },
    },
  }),
  mounted() {
    let dataset = null;
    //only test! --- sample date /// need to delete when this component complete
    if (this.label == null && this.chartdata == null) {
      dataset = [
        {
          label: "Dataset with point data",
          backgroundColor: "black",
          borderColor: "green",
          fill: false,
          steppedLine: true,
          data: [
            {
              x: this.test_makehour(1),
              y: 0,
            },
            {
              x: this.test_makehour(2),
              y: 0,
            },
            {
              x: this.test_makehour(4),
              y: 0,
            },
            {
              x: this.$moment("2021-04-22T08:45:00.952Z").toDate(),
              y: 1,
            },
          ],
        },
      ];
    }
    /////////////////////////////////////////////////////////////////////////////
    dataset = {
      labels: [this.test_makehour(this.$store.date), this.test_makehour(0)],
      datasets: this.chartdata,
    };
    this.renderChart(dataset, this.statusOptions);
  },
  methods: {
    test_makehour(days) {
      return this.$moment().subtract(days, "d").toDate();
    },
  },
};
</script>