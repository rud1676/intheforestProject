<template>
  <v-container class="py-2 px-1 flex" fluid style="height: 100vh">
    <v-card class="mx-auto" max-width="600" color="light-green lighten-4">
      <v-card-title>가입한 계정 관리</v-card-title>
      <v-expansion-panels>
        <v-expansion-panel v-for="(user, i) in users" :key="i">
          <v-expansion-panel-header> {{ user.id }} </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title
                  >사원번호: {{ user.companyid }}</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title
                  >관리자인증:
                  {{ user.valid ? "확인됨" : "미확인" }}</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title
                  >핸드폰 번호: {{ user.phone }}</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>주소: {{ user.addr }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  components: {},
  data: () => ({
    users: [],
  }),
  methods: {},
  computed: {
    ...mapState(["isLogin", "userInfo"]),
  },
  async mounted() {
    await this.$http.get("/login/getusers").then((r) => {
      this.$data.users = r.data;
    });
  },
};
</script>