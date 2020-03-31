<template>
  <el-container>
    <el-header>
      <logo></logo>
      <h1>McGill Tutor Platform</h1>
      <el-menu  router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">
          <i class = 'el-icon-info'></i>
          About Us</el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class = 'el-icon-menu'></i>
            Sign Up/Login</template>
          <el-menu-item index="/SignUp">
            <i class = 'el-icon-unlock'></i>
            Sign Up</el-menu-item>
          <el-menu-item index="/Login">
            <i class = 'el-icon-key'></i>
            Login</el-menu-item>
        </el-submenu>
        <el-menu-item index="3" disabled>Logout</el-menu-item>
      </el-menu>
    </el-header>
    <br><br><br><br><br><br><br><br>
    <el-container>
      <el-main>
        <h2>Come and join our <br> McGIll Tutor Community</h2>
        <tutor-image></tutor-image>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  import Logo from './Logo'
  import courses from '../Courses/CourseList'
  import tutorImage from './TutorImage'
  export default {
    name: 'Homepage',
    components:{
      Logo,
      courses,
      tutorImage
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>

</style>
