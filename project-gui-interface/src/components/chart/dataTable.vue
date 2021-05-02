<template>
  <v-card tile>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-title v-if="Ifsearch">
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Input Filter Info"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="items"
      :loading="load"
      loading-text="wait a moment"
      :search="search"
      @click:row="clickEvent"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  props: {
    load: {
      type: Boolean,
      default: false,
    },
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
    Ifsearch: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    clickEvent(image) {
      this.$emit("ClickEvent", image);
    },
  },
  data() {
    return { search: "" };
  },
  mounted() {
    this.$data.aggr = this.$props.items;
  },
};
</script>