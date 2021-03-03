<template>
  <v-item-group>
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l] in links"
        :key="l"
        link
        >
       
          <v-item>
            <v-card
              slot-scope="{ active }"
              :color="active ? 'primary' : ''"
              height="200"
              width="200"
              @click="tolink(l)"
              align="center">
            {{ text }}
            <img
          width="200"
          style=" margin: -30px auto;"
          src="../../assets/logo.png"
        />
            </v-card>
          </v-item>
        </v-flex>
      </v-layout>
    </v-container>
  </v-item-group>
</template>

<script>
export default {
data(){ 
    return{
      links: [
      [ 'Dashboard', '/dashboard'],
      [ 'Discover', '/discover'],
      [ 'check', '/check'],
      [ 'function', '/function'],
      [ 'alert', '/alert'],
      [ 'Management', '/Management'],
      ]
    }
  },
  methods: {
    tolink(l){
      this.$router.push({ path: l});
    }
  },
}
</script>

<style>

</style>