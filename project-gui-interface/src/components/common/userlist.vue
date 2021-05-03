<template>
  <div class="d-flex flex-wrap">
    <v-tooltip bottom v-for="a in agents" :key="a.name">
      <template v-slot:activator="{ on, attrs }">
        <v-chip
          v-bind="attrs"
          v-on="on"
          class="ma-2"
          @click="clickevent(a)"
          :color="a.status == 'active' ? 'primary' : 'error'"
          outlined
          pill
        >
          {{ a.name }}
          <v-icon right> mdi-account-outline </v-icon>
        </v-chip>
      </template>
      <span>{{ a.ip }}</span>
    </v-tooltip>
  </div>
</template>

<script>
//import axios from "axios";
export default {
  data: () => ({
    agents: [{ name: "TEST", ip: "123.123.123.123", active: "error" }],
  }),
  methods: {
    clickevent: function (l) {
      console.log(l);
      this.$emit("clickEvent", l.name);
    },
  },
  mounted() {
    this.$http
      .get("/wazuh/agents")
      .then((result) => {
        this.$data.agents = result.data;
        console.log("wazuiagent call!");
      })
      .catch(() => {
        console.log("testing... or Not found api Server..  ");
      });
  },
};
</script>
