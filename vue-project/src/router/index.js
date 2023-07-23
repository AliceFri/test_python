import { createRouter, createWebHashHistory } from "vue-router";
import layout from "../components/Layout/Layout.vue";

const routes = [
  {
    path: "/",
    name: "layout",
    component: layout,
    redirect: "/introduction",
    children: [
      {
        path: "/introduction",
        name: "introduction",
        component: () => import("../components/pages/introduction.vue")
      },
      {
        path: "/bigPetDogs",
        name: "bigPetDogs",
        component: () => import("../components/pages/bigPetDogs.vue")
      },
      {
        path: "/middlePetDogs",
        name: "middlePetDogs",
        component: () => import("../components/pages/middlePetDogs.vue")
      },
      {
        path: "/smallPetDogs",
        name: "smallPetDogs",
        component: () => import("../components/pages/smallPetDogs.vue")
      },
      {
        path: "/news",
        name: "news",
        component: () => import("../components/pages/news.vue")
      },
      {
        path: "/leaveMessage",
        name: "leaveMessage",
        component: () => import("../components/pages/leaveMessage.vue")
      }
    ]
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
