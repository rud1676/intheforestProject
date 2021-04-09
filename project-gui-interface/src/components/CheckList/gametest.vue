<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="1000" color="light-green lighten-4">
      <v-card-title>실행된 게임관련 리스트</v-card-title>
      <v-chip
        class="mx-5"
        v-for="game in GameList"
        v-bind:key="game.image"
        v-bind:dark="game.notSelected"
        close
        @click:close="game.notSelected = !game.notSelected"
        >{{ game.image }}</v-chip
      >
      <v-divider class="mx-5 mt-4"></v-divider>
      <v-data-table
    :headers="headers"
    :items="game_list"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data () {
      return {
        headers: [
          {
            text: 'Detected Games',
            align: 'start',
            sortable: false,
            value: 'Detected Games',
          },
          { text: 'Detected Game Name', value: 'Detected Game Name' },
          { text: 'PC with run detected', value: 'name' },
          { text: 'Detected Time', value: 'Detected Time' }
        ],
        game_list: [
          {
            'Detected Games': 'LeagueClient.exe',
            'Detected Game Name' : 'League of Legend',
            'name': 'Desktop-YU',
            'Detected Time' : '03/31/2021/13:45:13'
          }
        ]
      }
    },
  mounted() {
    const URL = "http://127.0.0.1/gamelist/gamelist";
    console.log("Get Gamelist!");
    axios.get(URL).then((result) => {
      console.log(result);
      console.log(result.data.images);
      this.$data.game_list = result.data.images;
    });
  },
};
</script>
