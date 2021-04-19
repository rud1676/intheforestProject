<template>
  <div class="d-flex mx-12">
    <v-slider
      v-model="slider.val"
      :label="slider.label"
      :thumb-color="slider.color"
      min="0"
      max="30"
      thumb-label="always"
    ></v-slider>
    <v-btn @click="submit">submit</v-btn>
  </div>
</template>

<script>
//import axios from "axios";
export default {
  props: {
    url: {
      type: String,
      default: "",
    },
    starttime: {
      type: String,
      default: null,
    },
    endtime: {
      type: String,
      default: null,
    },
    who: {
      type: String,
      default: null,
    },
    date: {
      type: Number,
      default: 7,
    },
  },
  data: () => ({
    slider: { label: "..days ago", val: 7, color: "blue" },
  }),
  methods: {
    submit() {
      console.log("DateSlide submit call");
      this.$store.state.date = this.$data.slider.val;
      if (this.$props.who == "timeout") {
        this.submit__for_timeoutcomponent();
      } else {
        this.submit_default();
      }
    },
    //default component!
    submit_default() {
      this.onload();

      console.log(this.$store.state.date);
      const realURL = this.$store.state.pyurl + this.$props.url;
      this.$http
        .post(realURL, { date: this.$data.slider.val })
        .then((result) => {
          this.$emit("submitEvent", result.data);
          this.finishload();
        });
    },
    //use timeout component!
    submit__for_timeoutcomponent() {
      this.onload();
      const realURL = this.$store.state.pyurl + this.$props.url;
      this.$http
        .post(realURL, {
          data: {
            start: this.$props.starttime,
            end: this.$props.endtime,
            date: this.$data.slider.val,
          },
        })
        .then((result) => {
          this.$emit("submitEvent", result.data);
          this.finishload();
        });
    },
    onload() {
      this.$emit("onload", true);
    },
    finishload() {
      this.$emit("finishload", false);
    },
  },
  mounted() {
    this.$data.slider.val = this.$store.state.date;
  },
};
</script>
