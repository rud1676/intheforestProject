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
    name: "dashboard",
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
        component: () => import("@/components/dashboard/main.vue")
      }
    ]
  },
  {
    path: "/discover",
    name: "discover",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        component: () => import("../components/discover.vue")
      }
    ]
  },
  {
    path: "/check",
    name: "check",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        component: () => import("../components/check.vue")
      }
    ]
  },
  {
    path: "/alert",
    name: "alert",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        component: () => import("../components/alert.vue")
      }
    ]
  },
  {
    path: "/management",
    name: "management",
    beforeEnter: adminUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
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
    path: "/adnormal",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        name: "adnormal",
        component: () => import("../components/CheckList/abnormal.vue")
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
