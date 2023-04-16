import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import VehicleView from "@/views/VehicleView";
import BikeView from "@/views/BikeView";
import ArticleView from "@/views/ArticleView";
import ContactView from "@/views/ContactView";
import LoginView from "@/views/LoginView";
import AccountView from "@/views/AccountView";
import store from '../store/index';
import Feedback from "@/views/FeedbackView";
import FeedbackView from "@/views/FeedbackView";
import RegistrationView from "@/views/RegistrationView";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/vehicles',
        name: 'vehicles',
        component: VehicleView
    },
    {
        path: '/bikes',
        name: 'bikes',
        component: BikeView
    },
    {
        path: '/articles',
        name: 'articles',
        component: ArticleView
    },
    {
        path: '/contacts',
        name: 'contacts',
        component: ContactView
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: { requiredNotAuthenticated: true }
    },
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationView,
        meta: { requiredNotAuthenticated: true }
    },
    {
        path: '/account',
        name: 'account',
        component: AccountView,
        meta: { requiredAuth: true }
    },
    {
        path: '/feedbacks',
        name: 'feedback',
        component: FeedbackView,
        meta: { requiredAuth: true }
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
      scrollBehavior(to, from, savedPosition) {
          if (to.hash) {
              return ({
                  el: to.hash,
                  behavior: 'smooth',

              })
          } else if (savedPosition) {
              return (savedPosition);
          } else {
              return {left: 0, top: 0}
          }
      },
  routes
})

router.beforeEach(async (to, from, next) => {
    if (to.meta.requiredAuth) {
        const isAuthenticated = await store.dispatch('auth/verify');
        console.log(isAuthenticated)
        if (isAuthenticated) return next();

        return next('/login')
    } else if (to.meta.requiredNotAuthenticated) {
        const isAuthenticated = await store.dispatch('auth/verify');
        if (!isAuthenticated) return next();

        return next('/account');
    }

    return next()
})

export default router
