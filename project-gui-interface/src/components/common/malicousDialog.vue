<template>
  <v-dialog v-model="dialog" width="650">
    <v-card>
      <v-card-title class="headline grey lighten-2">
        Please try again later
      </v-card-title>

      <v-card-text>
        <h2>Notice</h2>
        <br />
        <p>
          Malicious Check기능은 하루에 500개의 요청과 분당 4개의 요청으로
          제한합니다.
        </p>
        <p>그외의 문제는 관리자에게 문의하십시오.</p>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="accept"> I accept </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  props: {
    dialog: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    accept() {
      this.$emit("dialog");
    },
  },
};
</script>
