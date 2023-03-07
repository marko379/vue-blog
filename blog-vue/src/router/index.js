import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleView from '../views/ArticleView.vue'
import UserView from '../views/UserView.vue'
import Login from '../views/Login.vue'
import UserViewProfile from '../views/UserViewProfile.vue'
import SingupView from '../views/SingupView.vue'



const routes = [
  {
    path: '/home-page/',      // '/home-page/:member?/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:slug/',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/users/',
    name: 'user',
    component: UserView
  },
  {
    path: '/login/',
    name: 'log-in',
    component: Login
  },
  {
    path: '/user-profile/',
    name: 'profile',
    component: UserViewProfile
  },
  {
    path: '/register/',
    name: 'singup',
    component: SingupView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
