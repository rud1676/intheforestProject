<template>
  <div id="inspire">
    <v-navigation-drawer color="#9CCC65" clipped app>
      <v-sheet color="#7CB342" class="pa-4 justify-center">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <img src="../../assets/logo.png"
        /></v-avatar>

        <div>intheForest-Project</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-group
          v-for="lev1 in lev1"
          :key="lev1.no"
          v-show="isAdmin(lev1.admin)"
        >
          <!--v-on:click="tolink(lev1.link)" 삭제 필요...-->
          <template v-slot:activator>
            <v-list-item-content>
              <strong>
                {{ lev1.title }}
              </strong>
            </v-list-item-content>
          </template>
          <v-divider></v-divider>
          <v-list-item
            prepend-icon="mdi-check-circle"
            v-for="lev2 in lev2"
            :key="lev2.title"
            link
            v-show="lev2.no == lev1.no"
            v-on:click="tolink(lev2.link)"
          >
            <v-list-item-icon>
              <v-icon>mdi-check-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="lev2.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
        <!-- <v-list-item
          v-for="[icon, text, l, admin] in links"
          :key="l"
          link
          v-on:click="tolink(l)"
          v-show="isAdmin(admin)"
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item> -->
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import store from "@/store/index";
export default {
  data: () => ({
    cards: ["Today", "Yesterday"],
    drawer: null,
    links: [
      ["mdi-view-dashboard", "Dashboard", "dashboard", true],
      ["mdi-magnify", "Discover", "discover", true],
      ["mdi-clock", "check", "check", true],
      ["mdi-function", "function", "driverload", true], //this is test... need to 수정
      ["mdi-alarm", "alert", "alert", true],
      ["mdi-tune", "Management", "management", false],
    ],
    lev1: [
      //admin true인것은 무엇인가?
      {
        title: "No.1",
        no: 1,
        admin: true,
      },
      {
        title: "No.2",
        no: 2,
        admin: true,
      },
      {
        title: "관리자",
        no: 3,
        admin: false,
      },
    ],
    //라우터 링크 추가하기
    lev2: [
      {
        no: 1,
        title: "게임 관련",
        //link:"/dashboard",
      },
      {
        no: 1,
        title: "USB, Bluetooth 연결 감지(DriverLoad)",
        link: "driverload",
      },
      {
        no: 2,
        title: "이상행위",
      },
      {
        no: 2,
        title: "외부 침입",
      },
      {
        no: 3,
        title: "Dashboard",
        link: "dashboard",
      },
      {
        no: 3,
        title: "Discover",
        link: "discover",
      },
      {
        no: 3,
        title: "Check",
        link: "check",
      },
      {
        no: 3,
        title: "Function",
        link: "function",
      },
      {
        no: 3,
        title: "Alert",
        link: "alert",
      },
    ],
  }),
  methods: {
    tolink: function (l) {
      this.$router.push({ name: l }); //link에 path가 아닌 router name으로 링크 이동하게 바꿈(라우팅이 child가 있기때문에 의미가 확실한 이름으로 바꿈)
    },
    isAdmin(admin) {
      if (store.state.isAdmin) return true;
      else {
        return admin;
      }
    },
  },
};
</script>

<style></style>
