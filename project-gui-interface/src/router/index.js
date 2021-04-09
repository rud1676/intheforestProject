import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store/index";
const rejectAuthUser = (to, from, next) => {
  if (store.state.isLogin === true) {
    //이미 로그인 된 유저이므로 막아야함
    alert("이미 로그인을 하였습니다.");
    next("/home");
  } else {
    next();
  }
};
const onlyAuthUser = (to, from, next) => {
  if (store.state.isLogin === false) {
    //아직 로그인이 안 된 유저
    alert("로그인이 필요한 기능입니다.");
    next("/");
  } else {
    next();
  }
};
const adminUser = (to, from, next) => {
  if (store.state.isAdmin === false) {
    alert("관리자 권한이 필요합니다.");
    next("/no-auth");
  } else {
    next();
  }
};

// const originalPush = VueRouter.prototype.push;
// VueRouter.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch(() => {
//     return window.location.reload()
//   })
// };

Vue.use(VueRouter);
const routes = [
  {
    path: "/",
    redirect: "/login"
  },
  {
    path: "*",
    component: () => import("../views/Notfoundpage.vue")
  },
  {
    path: "/home",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Homepage.vue")
  },
  {
    path: "/dashboard",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "dashmain",
        name: "dashmain",
        component: () => import("@/components/dashboard/dashMain.vue")
      },
      {
        path: "/",
        name: "dashboard",
        component: () => import("@/components/dashboard/main.vue")
      }
    ]
  },
  {
    path: "/discover",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "discover",
        component: () => import("../components/discover.vue")
      }
    ]
  },
  {
    path: "/check",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "check",
        component: () => import("../components/check.vue")
      }
    ]
  },
  {
    path: "/alert",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "alert",
        component: () => import("../components/alert.vue")
      }
    ]
  },
  {
    path: "/management",

    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "management",
        component: () => import("../components/management.vue")
      }
    ]
  },
  {
    path: "/no-auth",
    name: "noauth",
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        component: () => import("@/components/noauth.vue")
      }
    ]
  },
  {
    path: "/login",
    name: "login",
    beforeEnter: rejectAuthUser,
    component: () => import("@/views/Login.vue")
  },
  //------------------sector checkList router--------------------
  {
    path: "/driverload",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "driverload",
        component: () => import("../components/CheckList/DriverLoad.vue")
      }
    ]
  },
  {
    path: "/wifi",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "wifi",
        component: () => import("../components/CheckList/wifi.vue")
      }
    ]
  },
  {
    path: "/newserivce",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "newSerivce",
        component: () => import("../components/CheckList/newSerivce.vue")
      }
    ]
  },
  {
    path: "/timeout", //근무 시간 외에 활동 체크
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "timeout",
        component: () => import("../components/CheckList/timeout.vue")
      }
    ]
  },
  {
    path: "/download", //근무 시간 외에 활동 체크
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "download",
        component: () => import("../components/CheckList/downloadList.vue")
      }
    ]
  },
  {
    path: "/gametest", //근무 시간 외에 활동 체크
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "gametest",
        component: () => import("../components/CheckList/gametest.vue")
      }
    ]
  },
  {
    path: "/rdp",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "rdp",
        component: () => import("../components/CheckList/rdp.vue")
      }
    ]
  },
  {
    path: "/dns",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "dns",
        component: () => import("../components/CheckList/dnsquery.vue")
      }
    ]
  },

  //--------------sector for abnomal
  {
    path: "/thread",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "thread",
        component: () => import("../components/abnormal/threadCreate.vue")
      }
    ]
  },
  {
    path: "/networkconnection",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "networkconnection",
        component: () => import("../components/abnormal/networkconnection.vue")
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
