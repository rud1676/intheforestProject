<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-btn class="mb-3" @click="overlay = true">Employee</v-btn>
    <v-overlay :value="overlay" :z-index="zIndex">
      <v-card width="300">
        <v-card-title>employee list</v-card-title>
        <v-list-item v-for="e in users" v-bind:key="e.hostname">
          <v-list-item-content>
            <v-list-time-title> {{ e.name }}</v-list-time-title>
            <v-list-time-subtitle> {{ e.host }}</v-list-time-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-card-actions class="pt-0">
          <v-btn class="white--text" color="teal" @click="overlay = false"
            >닫기</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-overlay>
    <iframe
      width="100%"
      height="100%"
      src="http://34.64.102.4:5601/goto/75d43987a77c3ae92b6ed23f47b3ed79"
      @load="load"
      v-if="isLoading"
    ></iframe>
    <loading v-else></loading>
  </v-container>
</template>

<script>
import axios from 'axios';
import Loading from '../common/Loading.vue';
export default {
  components: { Loading },
  data: () => ({
    overlay: false,
    zIndex: 0,
    users: [],
    isLoading: false,
  }),
  mounted() {
    const URL = 'http://localhost:80/employee/get';
    axios.get(URL).then(result => {
      result.data.users.forEach(item => {
        console.log(item);
        this.users.push(item);
      });
      console.log(this.users);
    });
  },
  method: {
    load: function(){
      this.isLoading = false;
    }
  }
};
</script>
