<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="800" color="light-green lighten-4">
      <v-card-title>Driver Load 이벤트 감지</v-card-title>
      <v-data-table
        dense
        :headers="headers"
        :items="events"
        item-key="name"
        class="elevation-1"
      ></v-data-table>
      <v-divider class="mx-5 mt-4"></v-divider>
      <v-row>
        <v-col class="ml-5" cols="8">
          <v-text-field
            v-model="image"
            :counter="10"
            label="Please Input Image"
            required
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-actions>
            <v-btn
              class="mx-5 mt-2"
              color="light-green lighten-1"
              @click="InputImage"
              >ADD</v-btn
            >
            <v-btn class="mt-2" color="light-green lighten-1" @click="submit"
              >Submit</v-btn
            >
          </v-card-actions>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    overlay: false,
    zIndex: 0,
    events: [
      { timestamp: "21:10:05", hostname: "DKDFS-dfa", driver: "Samsung" },
    ],
    headers: [
      {
        text: "TimeStamp",
        align: "start",
        sortable: false,
        value: "timestamp",
      },
      { text: "Hostname", value: "hostname" },
      { text: "Driver Cop.", value: "driver" },
    ],
    image: "",
  }),
  methods: {
    InputImage: function () {
      //중복 추가 x하는 부분 만들어야됨.
      for (const black of this.BlackList) {
        console.log("hi");
        if (black.image == this.image) {
          alert("Image가 중복됩니다!");
          return;
        }
      }
      let temp = new Object();
      temp.image = this.image;
      temp.notSelected = false;
      this.BlackList.push(temp);
      this.image = "";
    },
    submit: function () {
      let checkImage = [];
      for (const black of this.BlackList) {
        if (black.notSelected == false) {
          checkImage.push(black.image);
        }
      }
      //axios로 backend랑 통신해서 alert로 추가하는 부분
      const URL = "http://localhost:80/processCreate/BlackList";
      console.log("Push Black List");
      axios({
        method: "put",
        url: URL,
        data: {
          images: checkImage,
        },
      }).then((result) => {
        console.log(result.data);
        alert("적용이 완료되었습니다!");
        window.location.reload();
      });
    },
  },
  mounted() {
    const URL = "http://127.0.0.1:80/driverload/event";
    console.log("get Driver Event");
    axios.get(URL).then((result) => {
      console.log(this.$data.events);
      this.$data.events = result.data;
    });
  },
};
//카드로 프로세스 리스트 뿌리고 - 클릭으로 삭제, add 기능으로 추가! => id를 기억해서 수정하는거 해봐야할듯
</script>
