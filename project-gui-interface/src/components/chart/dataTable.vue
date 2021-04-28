<template>
  <v-card tile>
    <v-card-title>{{ title }}</v-card-title>
    <v-data-table
      :headers="headers"
      :items="items"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: () => null,
    },
    title: {
      type: String,
      defulat: "UnTitle",
    },
    headers: {
      type: Array,
      default: () => [
        {
          text: "AgentName",
          value: "label",
        },
        { text: "EventCount", value: "data" },
      ],
    },
  },
  data() {
    return {};
  },
  mounted() {
    this.$data.aggr = this.$props.items;
    console.log("datatable Mounted!:", this.$props.items);
  },
};
</script>