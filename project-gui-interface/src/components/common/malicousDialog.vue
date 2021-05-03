<template>
  <v-dialog v-model="dialog" width="650">
    <v-card>
      <v-card-title class="headline grey lighten-2">
        Please try again later
      </v-card-title>

      <v-card-text>
        <h2>Notice</h2>
        The Public API is limited to 500 requests per day and a rate of 4
        requests per minute.
        <div>
          The Public API must not be used in commercial products, services or
          business workflows.
        </div>
        <div>
          The Private API returns more threat data and exposes more endpoints.
        </div>
        The Private API is governed by an SLA that guarantees readiness of data.
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
