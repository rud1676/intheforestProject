<template>
  <v-item-group>
    <v-container grid-list-md>
      <v-layout wrap>
        <v-flex v-for="[text, l, img] in links"
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
export default {
data(){ 
    return{
      //일반 유저별 모듈 추가 및 제거 가능(현재 management 빼고 관리)
      links: [
      [ 'Dashboard', '/dashboard',require("../../assets/dashboard.png")],
      [ 'Discover', '/discover',require("../../assets/search.png")],
      [ 'check', '/check',require("../../assets/check.png")],
      [ 'function', '/function',require("../../assets/function.png")],
      [ 'alert', '/alert', require("../../assets/alert.png")],
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