<template>
  <v-container class="py-2 px-1" fluid style="height: 96vh">
    <v-toolbar flat height="3vh">
      <template v-slot:extension>
        <v-tabs v-model="currentItem" slider-color="white">
          <v-tab v-for="item in items" :key="item.text">
            <p>{{ item.text }}</p>
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
    <v-tabs-items v-model="currentItem">
      <v-tab-item v-for="item in items" :key="item.text" fluid height="100vh">
        <iframe width="100%" :src="item.url"></iframe>
      </v-tab-item>
    </v-tabs-items>
    <!--  -->
  </v-container>
</template>
<script>
export default {
  data: () => ({
    currentItem: "sysmon-all-dashboard",
    items: [
      {
        text: "Sysmon-All-Dashboard",
        icon: "mdi-dashboard",
        descript:
          "Integrated dashboard about Sysmon - ProcessCreate,DNSQuery,FileCreate and so on..",
        router_name: "sysmon",
        url: "http://34.64.140.231:5601/goto/e5d1eb97d811ddf8da258c3809387a70",
      },
      { text: "LOL", icon: "mdi-account", router_name: "sysmon" },
      { text: "Maplestory", icon: "mdi-flag", router_name: "check" },
      { text: "twitch", icon: "mdi-flag", router_name: "function" },
    ],
  }),
};
</script>

<!--

-->