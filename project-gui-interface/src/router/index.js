import Vue from "vue";
import VueRouter from "vue-router";
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(() => {
    return window.location.reload()
  })
};

Vue.use(VueRouter);
const routes = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    component: () => import("@/views/Homepage.vue")
  },
  {
    path: "/dashboard",
    name: "dashboard",
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
    component: () => import("@/views/Mainpage.vue"),
    children: [
      {
        path: "/",
        component: () => import("../components/alert.vue")
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
