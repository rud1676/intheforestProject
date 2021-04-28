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
      },
      { text: "Wazuh-dashboard", icon: "mdi-account" },
    ],
  }),
  methods: {
    link: function (item) {
      console.log(
        this.$router.push({
          name: "dashmain",
          query: { currentItem: item.text },
        })
      );
    },
  },
};
</script>