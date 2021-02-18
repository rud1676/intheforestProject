<template>
  <v-container class="py-2 px-1" fluid style="height: 97vh">
    <v-tabs class="green lighten-3">
      <v-tab>Sysmon Dash Board</v-tab>
      <v-tab>Item Two</v-tab>
      <v-tab>Item Three</v-tab>
    </v-tabs>
    <iframe
      width="100%"
      height="95%"
      src="http://34.64.140.231:5601/goto/e5d1eb97d811ddf8da258c3809387a70"
    ></iframe>
  </v-container>
</template>
<script>
export default {
  data: () => ({}),
};
</script>

<!--
    <v-tabs-items v-model="currentItem">
      <v-tab-item
        v-for="item in items.concat(more)"
        :key="item"
        :value="'tab-' + item"
      >
        <v-card flat>
          <v-card-text>
            <h2>{{ item }}</h2>
            {{ text }}
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
-->