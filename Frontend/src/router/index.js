import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Profile from '@/Profile/Profile'
import Login from '@/Registration/Login'
import SignUp from '@/Registration/Signup'
import CourseList from '@/Courses/CourseList'
import Search from '@/Courses/Search'
import HomePage from '@/Home/HomePage'
import logo from '@/Home/Logo'
import ShoppingCart from '@/Courses/ShopingCart'
import CourseDetail from "../Courses/CourseDetail";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/SignUp',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/Courses',
      name: 'Courses',
      component: CourseList
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search
    },
    {
      path: '/Home',
      name: 'HomePage',
      component: HomePage
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
    }

  ]
})
