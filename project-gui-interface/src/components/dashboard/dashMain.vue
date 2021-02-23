<template>
  <v-container class="px-0 py-0" fluid style="height: 97vh">
    <v-toolbar class="pt-0" flat height="3vh">
      <template v-slot:extension>
        <v-tabs v-model="currentItem" slider-color="white">
          <v-tab v-for="item in items" :href="`#${item.text}`" :key="item.text">
            {{ item.text }}
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
    <v-tabs-items v-model="currentItem">
      <v-tab-item
        v-for="item in items"
        :value="`${item.text}`"
        :key="item.text"
      >
        <iframe width="100%" height="875px" :src="item.url"></iframe>
      </v-tab-item>
    </v-tabs-items>
    <!--  -->
  </v-container>
</template>
<script>
export default {
  data: () => ({
    currentItem: "Maplestory",
    items: [
      {
        text: "Sysmon-Dashboard",
        url: "http://34.64.140.231:5601/goto/e5d1eb97d811ddf8da258c3809387a70",
      },
      {
        text: "metric-dashboard",
        url: "http://34.64.140.231:5601/goto/f097d5b2937db80c14e95b2fbd615510",
      },
      { text: "Maplestory", url: "check" },
      { text: "twitch", url: "function" },
    ],
  }),
  mounted() {
    console.log("hi");
    this.currentItem = this.$router.query.currentItem;
  },
};
</script>

<!--

-->