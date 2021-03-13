<template>
  <v-item-group>
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l, img, admin] in links"
        :key="l"
        link
        >
       
          <v-item>
            <v-card v-if="isAdmin(admin)"
              slot-scope="{ active }"
              :color="active ? 'primary' : ''"
              height="200"
              width="200"
              @click="tolink(l)"
              align="center">
            {{ text }}
            <div>{{ description }}</div>
            <img
          width="150"
          style=" margin: 15px auto;"
          :src="img"
        />
            </v-card>
          </v-item>
        </v-flex>
      </v-layout>
    </v-container>
  </v-item-group>
</template>

<script>
import store from "@/store/index"
export default {
data(){ 
    return{
      links: [
      [ 'Dashboard', '/dashboard',require("../../assets/dashboard.png"),true],
      [ 'Discover', '/discover',require("../../assets/search.png"),true],
      [ 'check', '/check',require("../../assets/check.png"),true],
      [ 'function', '/function',require("../../assets/function.png"),true],
      [ 'alert', '/alert', require("../../assets/alert.png"),true],
      [ 'Management', '/Management',require("../../assets/management.png"),false],
      ]
    }
  },
  methods: {
    tolink(l){
      this.$router.push({ path: l});
    },
    isAdmin(admin){
      if(store.state.isAdmin) return true;
      else{
        return admin
      }
    },
  },
}
</script>

<style>

</style>