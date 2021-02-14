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
    </v-col>

    <v-item-group>
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l] in links"
        :key="l"
        link
        v-on:click="tolink(l)">
          <v-item>
            <v-card
              slot-scope="{ active, toggle }"
              :color="active ? 'primary' : ''"
              dark
              height="200"
              width="200"
              @click="toggle"
              align="center"
            >
              <p class="text-sm-center">{{ text }}</p>
            </v-card>
          </v-item>
        </v-flex>
      </v-layout>
    </v-container>
  </v-item-group>
  </div>
</template>

<script>
export default {
  data(){
    return{
      links: [
      [ 'Dashboard', '/dashboard'],
      [ 'Discover', '/discover'],
      [ 'check', '/check'],
      ]
    }
  },
  methods: {
    gotomain() {
      this.$router.push('/dashboard');
    },
    tolink(l){
      this.$router.push({ path: l});
    }
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
