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
  </v-container>
</template>
<script>
export default {
  data: () => ({
    currentItem: "Maplestory",
    items: [
      {
        text: "Sysmon-Dashboard",
        url: "http://34.64.140.231:5601/goto/aad152199ba0943a5cfbb9cf8a4a19be",
      },
      {
        text: "Wazuh-dashboard",
        url:
          "http://34.64.140.231:5601/app/wazuh#/overview/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(columns:!(_source),filters:!(('$state':(isImplicit:!t,store:appState),meta:(alias:!n,disabled:!f,index:'wazuh-alerts-*',key:manager.name,negate:!f,params:(query:wazuh-and-beat),removable:!f,type:phrase),query:(match:(manager.name:(query:wazuh-and-beat,type:phrase))))),index:'wazuh-alerts-*',interval:auto,query:(language:kuery,query:''),sort:!())&tabView=panels&tab=general",
      },
    ],
  }),
  mounted() {
    this.currentItem = this.$route.query.currentItem;
  },
};
</script>

<!--

-->