<template>
  <div class="d-flex mx-12">
    <v-slider
      v-model="slider.val"
      :label="slider.label"
      :thumb-color="slider.color"
      min = "0"
      max = "30"
      thumb-label="always"
    ></v-slider>
    <v-btn @click="submit">submit</v-btn>
  </div>
</template>

<script>
//import axios from "axios";
export default {
    props:{
      url:String
    },
    data: () => ({
        slider: { label: '..days ago', val: 7, color: 'blue' },
    }),
    methods:{
      submit(){
        this.onload()
        const realURL = this.$store.state.pyurl+this.$props.url;
        this.$http.post(realURL,{"date":this.$data.slider.val}).then((result) => {
          this.$emit("submitEvent",result.data);
          this.finishload()
    });
      },
      onload(){
        this.$emit("onload",true)
      },
      finishload(){
        this.$emit("finishload",false)
      }
    },
}
</script>
