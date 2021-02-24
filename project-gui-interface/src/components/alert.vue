<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-btn>여긴 alert공간!</v-btn>
    <p>{{ this.BlackList }}</p>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    overlay: false,
    zIndex: 0,
    BlackList: [],
  }),
  mounted() {
    const URL = "http://localhost:80/processCreate/BlackList";
    console.log("Get Black List!");
    axios.get(URL).then((result) => {
      result.data.images.forEach((item) => {
        console.log(item);
        this.BlackList.push(item);
      });
    });
  },
};
//카드로 프로세스 리스트 뿌리고 - 클릭으로 삭제, add 기능으로 추가! => id를 기억해서 수정하는거 해봐야할듯
</script>
