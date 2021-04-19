<template>
  <div class="d-flex flex-wrap">
      <v-tooltip bottom      
      v-for="a in agents"
      :key="a.name">
      <template v-slot:activator="{ on, attrs }">
        <v-chip 
          v-bind="attrs"
          v-on="on"
      class="ma-2"
      :color="a.status == 'active'? 'primary' : 'error'"
      outlined
      pill
    >
      {{a.name}}
      <v-icon right>
        mdi-account-outline
      </v-icon>
    </v-chip>
    </template>
      <span>{{a.ip}}</span>
      </v-tooltip>
  </div>
</template>

<script>
//import axios from "axios";
export default {
    data: () => ({
        agents:[]
    }),
    mounted() {
        const URL = this.$store.state.pyurl+"/wazuh/agents";
        this.$http.get(URL).then((result) => {
            this.$data.agents = result.data;
        });
    }
}
</script>
