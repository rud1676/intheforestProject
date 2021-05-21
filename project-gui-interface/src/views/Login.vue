<template>
  <v-container fill-height style="max-width: 450px">
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-3">
            <v-toolbar flat>
              <v-toolbar-title>로그인</v-toolbar-title>
            </v-toolbar>
            <img
              width="400"
              style="display: block; margin: -60px auto"
              src="../assets/logo.png"
            />
            <v-text>(admin: rud1676, password: pji123 only test!)</v-text>
            <v-alert class="mb-3" :value="isLoginError" type="error">
              아이디와 비밀번호를 확인하세요.
            </v-alert>
            <v-alert class="mb-3" :value="isLogin" type="success">
              로그인이 완료되었습니다.
            </v-alert>
            <v-text-field
              app
              v-model="id"
              label="아이디를 입력하세요."
              color="green"
              ref="inputid"
              :rules="rules.name"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="패스워드를 입력하세요."
              type="password"
              color="green"
              :rules="rules.name"
              ref="inputpassword"
              @keyup.enter.prevent="
                login({
                  id,
                  password,
                })
              "
            ></v-text-field>
            <v-row class="mx-4 my-2">
              <v-btn color="#9CCC65" depressed @click="overlay = !overlay">
                <v-icon> mdi-window-close </v-icon>Register
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                color="#9CCC65"
                class="right-align"
                depressed
                @click="
                  login({
                    id,
                    password,
                  })
                "
              >
                <v-icon> mdi-account-circle </v-icon>Sign In
              </v-btn>
            </v-row>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
    <v-overlay z-index="0" :value="overlay">
      <v-card min-width="500">
        <div class="pa-3">
          <v-card-title>사용자 등록</v-card-title>
          <v-text-field
            v-model="register.id"
            label="아이디를 입력하세요."
            color="green"
            :rules="rules.name"
          ></v-text-field>
          <v-text-field
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            @click:append="show1 = !show1"
            v-model="register.pass"
            label="비밀번호를 입력하세요"
            color="green"
            :rules="rules.name"
          ></v-text-field>
          <v-text-field
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            @click:append="show2 = !show2"
            v-model="register.passcheck"
            label="비밀번호를 다시 입력하세요"
            color="green"
            :rules="rules.name"
          ></v-text-field>
          <v-text-field
            v-model="register.name"
            label="이름을 입력하세요"
            color="green"
            :rules="rules.name"
          ></v-text-field>
          <v-text-field
            v-model="register.companyid"
            label="사원 번호를 입력하세요"
            color="green"
            :rules="rules.name"
          ></v-text-field>
          <v-text-field
            v-model="register.phone"
            label="전화번호를 입력하세요"
            color="green"
          ></v-text-field>
          <v-text-field
            v-model="register.addr"
            label="주소를 동까지 입력해주세요"
            color="green"
          ></v-text-field>
          <v-card-actions>
            <v-row class="mx-4 my-2">
              <v-btn color="#9CCC65" depressed @click="overlay = !overlay">
                <v-icon> mdi-window-close </v-icon>Close
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="#9CCC65" depressed @click="regist">
                <v-icon> mdi-window-close </v-icon>Regist
              </v-btn>
            </v-row>
          </v-card-actions>
        </div>
      </v-card>
    </v-overlay>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  components: {},
  data: () => ({
    show1: false,
    show2: false,
    register: {
      id: "",
      pass: "",
      passcheck: "",
      name: "",
      companyid: "",
      phone: "",
      addr: "",
    },
    id: null,
    password: null,
    overlay: false,
    rules: {
      name: [(val) => (val || "").length > 0 || "This field is required"],
    },
  }),
  computed: {
    ...mapState(["isLogin", "isLoginError"]),
  },
  methods: {
    ...mapActions(["login"]),
    regist() {
      if (this.$data.register.pass != this.$data.register.passcheck) {
        alert("패스워드를 확인하여 주세요!");
        return;
      }
      const credentials = {
        id: this.$data.register.id,
        password: this.$data.register.pass,
        name: this.$data.register.name,
        companyid: this.$data.register.companyid,
        phone: this.$data.register.phone,
        addr: this.$data.register.addr,
        valid: false,
        admin: false,
      };
      this.$http.post("/login/put", credentials).then((data) => {
        if (data.data.message == "이미 존재하는 아이디입니다.") {
          alert(data.data.message);
        } else {
          alert(data.data.message);
          this.$data.overlay = false;
        }
      });
    },
  },
};
</script>

<style>
</style>