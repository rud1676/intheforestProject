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
      item-key="id"
      @click:row="clickEvent"
      :items-per-page="10"
      class="elevation-1"
      :show-expand="true"
      :single-expand="true"
      @item-expanded="showDetail"
    >
      <template v-slot:expanded-item="{ headers }">
        <td :colspan="headers.length">
          <v-list class="asdf">
            <v-list-item>
              <v-list-item-title>FileName</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.originalFileName }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>fileVersion</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.fileVersion }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>company</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.company }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>product</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.product }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>description</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.description }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>image</v-list-item-title>

              <v-subheader>
                {{ overlayData.image }}
              </v-subheader>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>processId</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.processId }}
              </v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>parentImage</v-list-item-title>

              <v-subheader>
                {{ overlayData.parentImage }}
              </v-subheader>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>parentProcessId</v-list-item-title>

              <v-list-item-subtitle class="text-right">
                {{ overlayData.parentProcessId }}
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </td>
      </template>
    </v-data-table>
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
  data() {
    return {
      search: "",
      overlayData: {
        originalFileName: "...",
      },
    };
  },
  methods: {
    test() {
      return 0;
    },
    showDetail(image) {
      this.$data.overlayData = image.item;
    },
    clickEvent(image) {
      this.$emit("ClickEvent", image.hashes);
    },
  },
};
</script>