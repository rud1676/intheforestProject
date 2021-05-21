<template>
  <v-container
    class="py-2 px-1 d-flex align-center"
    fluid
    style="height: 100vh"
  >
    <v-card class="mx-auto" max-width="300" tile>
      <v-list rounded>
        <v-list-item-group color="primary">
          <v-list-item v-for="(item, i) in items" :key="i" @click="link(item)">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        text: "Sysmon-Dashboard",
        icon: "mdi-calendar-account",
        descript:
          "Integrated dashboard about Sysmon - ProcessCreate,DNSQuery,FileCreate and so on..",
        url: "http://34.64.140.231:5601/goto/aad152199ba0943a5cfbb9cf8a4a19be",
      },
      {
        text: "Wazuh-dashboard",
        icon: "mdi-account",
        descript:
          "Integrated dashboard about Sysmon - ProcessCreate,DNSQuery,FileCreate and so on..",
        url:
          "http://34.64.140.231:5601/app/wazuh#/overview/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(columns:!(_source),filters:!(('$state':(isImplicit:!t,store:appState),meta:(alias:!n,disabled:!f,index:'wazuh-alerts-*',key:manager.name,negate:!f,params:(query:wazuh-and-beat),removable:!f,type:phrase),query:(match:(manager.name:(query:wazuh-and-beat,type:phrase))))),index:'wazuh-alerts-*',interval:auto,query:(language:kuery,query:''),sort:!())&tabView=panels&tab=general",
      },
    ],
  }),
  methods: {
    link: function (item) {
      window.open(item.url);
    },
  },
};
</script>