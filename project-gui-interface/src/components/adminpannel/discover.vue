<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-btn @click="openfunc">Click to Open Discover</v-btn>
  </v-container>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    openfunc: function () {
      window.open(
        "http://34.64.140.231:5601/goto/37a4ebb4e3cb0f67b23cec8c6007af67"
      );
    },
  },
};
</script>
