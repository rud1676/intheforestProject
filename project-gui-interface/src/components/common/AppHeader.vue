<template>
  <div id="inspire">
    <v-navigation-drawer
      color="#9CCC65"
      clipped
      app
      permanent
      :mini-variant.sync="mini"
    >
    <v-sheet color="#7CB342">
    <v-list-item class="px-2 py-3 d-flex">
        <v-list-item-avatar color="white">
          <v-img src="../../assets/logo3.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-title>IntheForest-Project</v-list-item-title>

        <v-btn v-if="!mini" icon @click.stop="mini = !mini">
              <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>
      </v-sheet>
      <v-divider></v-divider>
        <v-list-item @click="$router.push({ name: 'integrated' })">
          <v-list-item-icon>
            <v-icon>mdi-monitor-dashboard</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="font-weight-bold">통합 대시보드</v-list-item-title>
        </v-list-item>

        <v-list-item @click="$router.push({ name: 'agent' })">
          <v-list-item-icon>
            <v-icon>mdi-desktop-classic</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="font-weight-bold">근무자 대시보드</v-list-item-title>
        </v-list-item>

      <v-list-group
        v-for="item in items"
        :key="item.title"
        :prepend-icon="item.action"
        color="green darken-3"
        v-show="isAdmin(item.admin)"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" class="font-weight-bold"></v-list-item-title>
          </v-list-item-content>
        </template>
<v-divider></v-divider>
        <v-list-item
          v-for="child in item.items"
          :key="child.title"
          link
          v-on:click="tolink(child.link)"
        >
          <v-list-item-icon>
              <v-icon>{{ child.action }}</v-icon>
            </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="child.title"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </v-list-group>
    </v-navigation-drawer>
    
  </div>
</template>

<script>
import store from "@/store/index";
export default {
  mounted() {
    console.log(this.$vuetify.breakpoint.width);
  },
  data: () => ({
    cards: ["Today", "Yesterday"],
    drawer: true,
    mini: false,
    links: [
      ["mdi-view-dashboard", "Dashboard", "dashboard", true],
      ["mdi-magnify", "Discover", "discover", true],
      ["mdi-clock", "check", "check", true],
      ["mdi-function", "function", "driverload", true], //this is test... need to 수정
      ["mdi-alarm", "alert", "alert", true],
      ["mdi-tune", "Management", "management", false],
    ],
    items:[
      {
      action: 'mdi-account',
      admin: true,
      items: [
        {
        title: "게임 관련",
        action: "mdi-gamepad-variant-outline",
        link: "gametest",
        },
        {
        title: "요청한 DNS 목록",
        action: "mdi-microsoft-internet-explorer",
        link: "dns",
        },
        {
        title: "USB 인식 감지",
        action: "mdi-usb-flash-drive",
        link: "driverload",
        },
        {
          title: "지정 시간 외 사용자 로그감지",
        action: "mdi-office-building-marker-outline",
        link: "timeout",
        },
        {
        title: "파일 다운로드 In Browser",
        action: "mdi-folder-download-outline",
        link: "download",
        },
        {
        title: "연결된 네트워크 감지",
        action: "mdi-wifi",
        link: "wifi", 
        },
        {
          title: "새로운 프로그램 설치",
        action: "mdi-progress-download",
        link: "newSerivce",
        }
        ,{
        title: "원격 데스크톱 연결 감지",
        action: "mdi-remote",
        link: "rdp",
        },
      ],
      title:'체크 리스트',
      },
      {
        action:'mdi-shield-plus-outline',
        items:[
          {
            title: "인터넷 연결된 프로세스",
        action: "mdi-shield-search",
        link: "networkconnection",
          },
          {
            title: "Thread InJection",
        action: "mdi-shield-search",
        link: "thread",
          },
          {
            title: "실행한 프로세스 목록",
        action: "mdi-shield-search",
        link: "processCreate",
          },
          {
             title: "외부 침입",
        action: "mdi-shield-check",
          }
        ],
        title:'이상 징후 분석',
        admin: true,
      },
      {
        title:'관리자 설정',
        admin: false,
        action:'mdi-wrench',
        items:[
          {
            title: "Dashboard",
        link: "dashboard",
        action: "mdi-chart-bar",
          },
          {
            title: "Discover",
        link: "discover",
        action: "mdi-magnify",
          }
        ]
      }
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

<style>
</style>
