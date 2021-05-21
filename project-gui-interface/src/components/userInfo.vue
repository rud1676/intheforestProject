<template>
  <v-container class="py-2 px-1 flex" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="600" color="light-green lighten-4">
      <v-card-title>계정 정보</v-card-title>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>아이디: {{ userInfo.id }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title
            >사원번호: {{ userInfo.companyid }}</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title
            >관리자인증:
            {{ userInfo.valid ? "확인됨" : "미확인" }}</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title
            >계정권한:
            {{ userInfo.admin ? "관리자" : "사원" }}</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title
            >핸드폰 번호: {{ userInfo.phone }}</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>주소: {{ userInfo.addr }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  components: {},
  data: () => ({}),
  methods: {},
  computed: {
    ...mapState(["isLogin", "userInfo"]),
  },
  mounted() {
    console.log(this.userInfo);
  },
};
</script>