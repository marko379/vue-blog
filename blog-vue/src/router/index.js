import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleView from '../views/ArticleView.vue'
import Login from '../views/Login.vue'
import UserViewProfile from '../views/UserViewProfile.vue'
import SingupView from '../views/SingupView.vue'
import SerachResults from '../views/SerachResults.vue'
import SerachBookByGenre from '../views/SerachBookByGenre.vue'
import BuyBooksView from '../views/BuyBooksView.vue'



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
    path: '/books-checkout/',
    name: 'checkout',
    component: BuyBooksView

  },
  {
    // path: '/search-results/:data',
    path: '/search-results/:data?',
    name: 'search',
    component: SerachResults,
    props: true
  },
  {
    // path: '/search-results/:data',
    path: '/search-results-by-genre/:genre?',
    name: 'search-book-by-genre',
    component: SerachBookByGenre,
    props: true
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
