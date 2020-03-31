import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Profile from '@/Profile/Profile'
import Login from '@/Registration/Login'
import SignUp from '@/Registration/Signup'
import CourseList from '@/Courses/CourseList'
import Rating from '@/Courses/Rating'
import Search from '@/Courses/Search'
import HomePage from '@/Home/HomePage'
import logo from '@/Home/Logo'

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
      path: '/Signup',
      name: 'Signup',
      component: SignUp
    },
    {
      path: '/Courses',
      name: 'Courses',
      component: CourseList
    },
    {
      path: '/Rating',
      name: 'Rating',
      component: Rating
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
    }
  ]
})
