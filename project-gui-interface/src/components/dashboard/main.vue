<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="300" tile>
      <v-list rounded>
        <v-list-item-group color="primary">
          <v-list-item v-for="(item, i) in items" :key="i" @click="print(item)">
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
        text: "Sysmon-All-Dashboard",
        icon: "mdi-clock",
        router_name: "sysmon",
      },
      { text: "LOL", icon: "mdi-account", router_name: "sysmon" },
      { text: "Maplestory", icon: "mdi-flag", router_name: "check" },
      { text: "twitch", icon: "mdi-flag", router_name: "function" },
    ],
  }),
  methods: {
    print: function (item) {
      console.log(this.$router.push({ name: item.router_name }));
    },
  },
};
</script>