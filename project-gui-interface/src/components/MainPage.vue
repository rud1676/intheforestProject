<template>
  <div>
    <v-toolbar dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-icon color="green darken-2"> mdi-home </v-icon>home

      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-export</v-icon>
      </v-btn>
    </v-toolbar>
    <v-col class="d-felx flex-column justify-center">
      <v-layout class="d-flex justify-center mb-10">
        <img
          width="400"
          style="position: absolute; top: -30px; left: 38%"
          src="../assets/logo.png"
        />
      </v-layout>
      <v-btn v-on:click="gotomain" elevation="2" x-large fab class="static"
        >dashboard</v-btn
      >
    </v-col>
  </div>
</template>

<script>
export default {
  methods: {
    gotomain() {
      this.$route.push('/dashboard');
    },
  },
};
</script>

<style>
.static {
  display: flex;
  position: absolute;
  width: 100px;
  height: 100px;
  top: 300px;
  left: 30%;
  border-width: 15px;
}
</style>
