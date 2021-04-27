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
    path: "/login",
    name: "login",
    beforeEnter: rejectAuthUser,
    component: () => import("@/views/Login.vue")
  },
  {
    path: "/main",
    component: () => import("@/views/Mainpage.vue"),
    children: [
      //about admin pannel
      {
        path: "dashmain",
        name: "dashmain",
        beforeEnter: adminUser,
        component: () => import("@/components/adminpannel/dashMain.vue")
      },
      {
        path: "/dashboard",
        name: "dashboard",
        beforeEnter: adminUser,
        component: () => import("@/components/adminpannel/main.vue")
      }, {
        path: "/discover",
        name: "discover",
        beforeEnter: adminUser,
        component: () => import("../components/adminpannel/discover.vue")
      },
      //intergrated dashboard!
      {
        path: "/integrated",
        name: "integrated",
        component: () => import("../components/dashboard/Integrated_dashboard.vue")
      },
      //------------------sector checkList router--------------------
      {
        path: "/driverload",
        name: "driverload",
        component: () => import("../components/CheckList/DriverLoad.vue")
      },
      {
        path: "/wifi",
        name: "wifi",
        component: () => import("../components/CheckList/wifi.vue")
      },
      {
        path: "/newSerivce",
        name: "newSerivce",
        component: () => import("../components/CheckList/newSerivce.vue")
      },
      {
        path: "/timeout",
        name: "timeout",
        component: () => import("../components/CheckList/timeout.vue")
      },
      {
        path: "/download",
        name: "download",
        component: () => import("../components/CheckList/downloadList.vue")
      },
      {
        path: "/gametest",
        name: "gametest",
        component: () => import("../components/CheckList/gametest.vue")
      },
      {
        path: "/rdp",
        name: "rdp",
        component: () => import("../components/CheckList/rdp.vue")
      },
      {
        path: "/dns",
        name: "dns",
        component: () => import("../components/CheckList/dnsquery.vue")
      },
      //--------------sector for abnomal
      {
        path: "/thread",
        name: "thread",
        component: () => import("../components/abnormal/threadCreate.vue")
      },
      {
        path: "/networkconnection",
        name: "networkconnection",
        component: () => import("../components/abnormal/networkconnection.vue")
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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
