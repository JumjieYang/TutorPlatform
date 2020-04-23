import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Profile from '@/Profile/Profile'
import Login from '@/Registration/LogIn'
import SignUp from '@/Registration/SignUp'
import CourseList from '@/Courses/CourseList'
import Search from '@/Courses/Search'
import HomePage from '@/Home/HomePage'
import logo from '@/Home/Logo'
import ShoppingCart from '@/Courses/ShopingCart'
import Chat from '@/Chat/Chat'
import CourseDetail from "../Courses/CourseDetail";
import aboutUs from "../Home/aboutUs";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/Chat',
      name: 'Chat',
      component: Chat,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login,
      meta: {
        requiresVisitor: true,
      }
    },
    {
      path: '/SignUp',
      name: 'SignUp',
      component: SignUp,
      meta: {
        requiresVisitor: true,
      }
    },
    {
      path: '/Courses',
      name: 'Courses',
      component: CourseList,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/Home',
      name: 'HomePage',
      component: HomePage,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/aboutUs',
      name: 'aboutUs',
      component: aboutUs,
      meta:{
        requireAuth: true,
      }
    },

    {
      path: '/logo',
      name: 'logo',
      component: logo
    },
    {
      path: '/shopingCart',
      name: 'shopingCart',
      component: ShoppingCart
    },
    {
      path: '/CourseDetail',
      name: 'CourseDetail',
      component: CourseDetail
    },
    {
      path :'/Chat',
      name: 'Chat',
      component: Chat
    }

  ]
})
