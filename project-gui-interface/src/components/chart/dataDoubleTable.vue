<template>
  <v-card>
    <v-card-title>{{ title }}</v-card-title>
    <v-data-table
      dense
      :headers="headers"
      :items="items"
      item-key="id"
      :show-expand="true"
      :single-expand="true"
      @item-expanded="test"
      class="elevation-1"
    >
      <template v-slot:expanded-item="{ headers }">
        <td class="pa-3" :colspan="headers.length">
          <v-data-table
            class="elevation-2"
            :headers="expandHeaders"
            :items="expandEvents"
          >
            <template v-slot:top>
              <v-toolbar flat color="white">
                <v-toolbar-title>{{ subtitle }}</v-toolbar-title>
              </v-toolbar>
            </template>
          </v-data-table>
        </td>
      </template>
    </v-data-table>
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
    subtitle: {
      type: String,
      defulat: "UnTitle",
    },
  },
  data() {
    return {
      headers: [
        {
          text: "AgentName",
          value: "agent",
        },
        { text: "PakageCount", value: "count" },
      ],
      expandHeaders: [
        { text: "Company", value: "Company" },
        { text: "Count", value: "count" },
      ],
      expandEvents: [],
    };
  },
  methods: {
    test: function ({ item }) {
      this.$data.expandEvents = item.companyCount;
    },
  },
  mounted() {
    this.$data.aggr = this.$props.items;
    console.log("datatable Mounted!:", this.$props.items);
  },
};
</script>