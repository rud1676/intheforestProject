<template>
  <div id="inspire">
    <v-navigation-drawer color="#9CCC65" clipped app
    permanent
     :mini-variant.sync="mini"
    >
      <v-sheet color="#7CB342" class="pa-4 d-flex" >
        <v-row>
          <v-col>
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <img src="../../assets/logo.png"
        />
        
        </v-avatar>
        
        </v-col>

        </v-row>
        <v-row>

          <v-col>
            <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
          </v-col>
          <v-col>
        <div>IntheForest-Project</div>
        </v-col>
        </v-row>
        
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
  mounted () {
      console.log(this.$vuetify.breakpoint.width)
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
    lev1: [
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
        title: "Admin Panal",
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
        title: "Dns Query",
        icon: "mdi-gamepad-variant-outline",
        link: "dns",
      },
      {
        no: 1,
        title: "드라이버 로드 이벤트",
        icon: "mdi-usb-flash-drive",
        link: "driverload",
      },
      {
        no: 1,
        title: "근무시간외",
        icon: "mdi-office-building-marker-outline",
        link: "timeout",
      },
      {
        no: 1,
        title: "다운로드",
        icon: "mdi-folder-download-outline",
        link: "download",
      },
      {
        no: 1,
        title: "wifi연결",
        icon: "mdi-wifi",
        link: "wifi",
      },
      {
        no: 1,
        title: "새로운 서비스 설치",
        icon: "mdi-progress-download",
        link: "newSerivce",
      },
      {
        no: 1,
        title: "RDP client 사용 여부",
        icon: "mdi-remote",
        link: "rdp",
      },
      {
        no: 2,
        title: "네트워크 연결된 프로세스들",
        icon: "mdi-shield-search",
        link: "networkconnection",
      },
      {
        no: 2,
        title: "프로세스가 만든 Thread",
        icon: "mdi-shield-search",
        link: "thread",
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
