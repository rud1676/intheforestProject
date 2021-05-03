<template>
  <v-alert icon="mdi-shield-lock-outline" prominent text type="info">
    {{ title }}
    <v-divider class="my-4 info" style="opacity: 0.22"></v-divider>
    <v-row align="center" no-gutters>
      <v-col class="grow">
        Check value :
        <v-text-field
          v-model="url"
          :label="labeling"
          dense
          color="info"
          clearable
        ></v-text-field>
      </v-col>
      <v-progress-circular
        indeterminate
        color="green"
        :size="70"
        :width="7"
        v-if="loading && !error"
      ></v-progress-circular>
      <v-spacer></v-spacer>
      <div>
        <v-btn color="info" outlined @click="clickevent"> Check </v-btn>
      </div>
    </v-row>
  </v-alert>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "MALICIOUS DNS TRAFFIC Check.",
    },
    url: {
      type: String,
      default: "",
    },
    labeling: {
      type: String,
      defualt: "",
    },
    loading: {
      type: Boolean,
      default: false,
    },
    error: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    clickevent() {
      console.log("hi");
      this.$emit("dnscheck");
    },
  },
};
</script>
      