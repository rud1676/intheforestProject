import Vue from "vue";
import VueRouter from "vue-router";

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
        path: "sysmon",
        name: "sysmon",
        component: () => import("@/components/dashboard/testdashboard.vue")
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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
