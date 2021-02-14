<template>
  <v-container class="align-center">
    <v-col>
      <v-card class="d-flex flex-wrap mx-auto" max-width="865">
        <v-toolbar color="indigo" dark>
          <v-toolbar-title
            >Process Create Event - 실행된 프로그램 감지</v-toolbar-title
          >
        </v-toolbar>
        <v-container fluid>
          <v-row>
            <v-col>
              <v-card class="flex-wrap d-flex align-content-start">
                <v-btn
                  v-for="user in users"
                  :key="user.hostname"
                  class="pa-3 my-4 mx-12"
                  v-on:click="FilterAdd(user.hostname)"
                  >{{ user.name }}</v-btn
                >
              </v-card>
              <v-col>
                <v-card>{{ filterstr }}</v-card>
              </v-col>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-col>

    <v-col>
      <v-btn v-on:click="checkHash" class="mr-5"
        >Process Create 해쉬값 체크</v-btn
      >
      <v-btn class="mr-5" v-on:click="openProcessCreate"
        >Process Create 이벤트</v-btn
      >
      <v-btn class="mr-5">DNS query 이벤트</v-btn>
    </v-col>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',

  data: () => {
    return {
      users: [
        { hostname: 'DESKTOP-CGRM1HV', name: '임유섭', selected: false },
        { hostname: 'DESKTOP-4KEM7G3', name: '주경진', selected: false },
      ],
      filterstr: '',
    };
  },
  created() {
    const fs = require('fs');
    console.log(fs);
    console.log(fs.readFileSync('../assets/userlist.txt', 'utf-8'));
  },
  methods: {
    FilterAdd: function(hostname) {
      /*나중에 seleted로 gui button 구현할 예정*/
      let selectedUser = this.users.find(user => user.hostname == hostname);
      if (selectedUser.selected == false) {
        selectedUser.selected = true;
      } else {
        selectedUser.selected = false;
      }
      console.log(selectedUser);
      this.filterstr = '';
      this.users.forEach(user => {
        if (user.selected == true) {
          this.filterstr += user.hostname;
          this.filterstr += ' ';
        }
      });
      this.filterstr = this.filterstr.slice(0, -1);
      console.log(this.filterstr);
    },
    checkHash: function() {
      let path =
        'http://' + window.location.hostname + ':80/ProcessCreate/userslist';
      axios
        .post(path, {
          users: this.filterstr,
        })
        .then(res => {
          console.log(res);
        });
    },
    openProcessCreate: function() {
      console.log('새창열기실행중');
      const url = `http://34.64.102.4:5601/app/dashboards#/view/4bc0a2b0-41f9-11eb-972d-b5b93cf41ed8?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15d,to:now))&_a=(description:'%EB%B0%94%ED%83%95%ED%99%94%EB%A9%B4%20%EC%8B%A4%ED%96%89,%20%ED%8C%8C%EC%9D%BC%20%EC%9D%B8%ED%84%B0%EB%84%B7%20%EB%8B%A4%EC%9A%B4%20%EA%B0%90%EC%A7%80',filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:f4ab6b90-41d0-11eb-972d-b5b93cf41ed8,key:agent.hostname,negate:!f,params:(query:'${this.filterstr}'),type:phrase),query:(match:(agent.hostname:'${this.filterstr}')))),fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!t),query:(language:kuery,query:''),timeRestore:!f,title:'%EC%A0%95%EC%83%81%ED%96%89%EC%9C%84%20%ED%83%90%EC%A7%80',viewMode:view)`;
      window.open(url, '_blank');
    },
  },
};
</script>
