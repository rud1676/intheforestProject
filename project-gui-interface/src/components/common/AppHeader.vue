<template>
  <div id="inspire">
    <v-navigation-drawer color="#9CCC65" clipped app>
      <v-sheet color="#7CB342" class="pa-4 justify-center">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <img src="../../assets/logo.png"
        /></v-avatar>

        <div>IntheForest-Project</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-item @click="$router.push({ name: 'integrated' })">
          <v-list-item-icon>
            <v-icon>mdi-monitor-dashboard</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Integrated Dashboard</v-list-item-title>
        </v-list-item>
        <v-list-item @click="$router.push({ name: 'agent' })">
          <v-list-item-icon>
            <v-icon>mdi-desktop-classic</v-icon>
          </v-list-item-icon>
          <v-list-item-title>AGENT Dashboard</v-list-item-title>
        </v-list-item>
        <v-list-group
          v-for="lev1 in lev1"
          :key="lev1.no"
          v-show="isAdmin(lev1.admin)"
          color="green darken-3"
        >
          <template v-slot:activator>
            <v-list-item-content>
              <strong>
                <v-icon>{{ lev1.icon }} </v-icon>
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
              <v-icon>{{ lev2.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="lev2.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
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
      {
        title: "사용자 행동패턴 분석",
        no: 1,
        admin: true,
      },
      {
        title: "이상 징후 분석",
        no: 2,
        admin: true,
      },
      {
        title: "관리자 설정",
        icon: "mdi-wrench",
        no: 3,
        admin: false,
      },
    ],
    lev2: [
      {
        no: 1,
        title: "게임 관련",
        icon: "mdi-gamepad-variant-outline",
        link: "gametest",
      },
      {
        no: 1,
        title: "요청한 DNS 목록",
        icon: "mdi-gamepad-variant-outline",
        link: "dns",
      },
      {
        no: 1,
        title: "USB 인식 감지",
        icon: "mdi-usb-flash-drive",
        link: "driverload",
      },
      {
        no: 1,
        title: "지정 시간 외 사용자 로그감지",
        icon: "mdi-office-building-marker-outline",
        link: "timeout",
      },
      {
        no: 1,
        title: "파일 다운로드 In Browser",
        icon: "mdi-folder-download-outline",
        link: "download",
      },
      {
        no: 1,
        title: "연결된 네트워크 감지",
        icon: "mdi-wifi",
        link: "wifi",
      },
      {
        no: 1,
        title: "새로운 프로그램 설치",
        icon: "mdi-progress-download",
        link: "newSerivce",
      },
      {
        no: 1,
        title: "원격 데스크톱 연결 감지",
        icon: "mdi-remote",
        link: "rdp",
      },
      {
        no: 2,
        title: "인터넷 연결된 프로세스",
        icon: "mdi-shield-search",
        link: "networkconnection",
      },
      {
        no: 2,
        title: "Thread InJection",
        icon: "mdi-shield-search",
        link: "thread",
      },
      {
        no: 2,
        title: "실행한 프로세스 감지",
        icon: "mdi-shield-search",
        link: "ProcessCreate",
      },
      {
        no: 2,
        title: "외부 침입",
        icon: "mdi-shield-check",
      },
      {
        no: 3,
        title: "Dashboard",
        link: "dashboard",
        icon: "mdi-chart-bar",
      },
      {
        no: 3,
        title: "Discover",
        link: "discover",
        icon: "mdi-magnify",
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
