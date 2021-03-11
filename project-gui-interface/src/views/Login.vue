<template>
  <div>
      <v-container fill-height style="max-width:450px;">
          <v-layout align-center row wrap>
              <v-flex xs12>
                  <v-card>
                      <div class="pa-3">
                          <v-toolbar flat>
                              <v-toolbar-title>로그인</v-toolbar-title>
                          </v-toolbar>
                        <img
                            width="400"
                            style="display: block; margin: -60px auto;"
                            src="../assets/logo.png"
                            />
                            <v-alert
                            class="mb-3"
                            :value="isLoginError"
                            type="error">
                                아이디와 비밀번호를 확인하세요.
                            </v-alert>
                            <v-alert
                            class="mb-3"
                            :value="isLogin"
                            type="success">
                                로그인이 완료되었습니다.
                            </v-alert>
                            <v-text-field app
                            v-model="id"
                                label="아이디를 입력하세요."
                                color="green"
                                :rules="rules.name"
                            ></v-text-field>
                            <v-text-field
                            v-model="password"
                                label="패스워드를 입력하세요."
                                type="password"
                                color="green"
                                :rules="rules.name"
                                @keyup.enter.prevent="login({
                                    id,
                                    password
                                })"
                            ></v-text-field>
                            <v-btn
                                color="#9CCC65"
                                large
                                block
                                depressed
                                @click="login({
                                    id,
                                    password
                                })">
                                로그인
                            </v-btn>
                        </div>
                    </v-card>
              </v-flex>
          </v-layout>
      </v-container>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
export default {
  components: {  },
  data: () => ({
      id: null,
      password: null,
      
      rules: {
           name: [val => (val || '').length > 0 || 'This field is required'],
      }
  }),
  computed:{
      ...mapState(["isLogin", "isLoginError"])
  },
  methods:{
      ...mapActions(["login"]),
  }

}
</script>

<style>

</style>