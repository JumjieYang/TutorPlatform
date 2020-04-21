<template>
  <el-container>
    <el-header>
      <logo></logo>
      <h1>McGill Tutor Platform</h1>
      <el-menu  router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="/aboutUs">
          <i class = 'el-icon-info'></i>
          About Us</el-menu-item>
        <el-submenu index="/aboutUs">
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
        <el-menu-item index="/Profile" >
          <i class = 'el-icon-s-custom'></i>
          Personal Profile</el-menu-item>
      </el-menu>
    </el-header>
    <br><br><br><br><br><br><br><br>
    <el-container>
      <el-main>
        <h2>Come and join our <br> McGIll Tutor Community</h2>
        <tutorImage></tutorImage>
        <div class = 'coursesList'>
          <el-link href = '#/Courses'>Courses Preview</el-link>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  import Logo from './Logo'
  import tutorImage from './TutorImage'
  import CourseList from "../Courses/CourseList";
  export default {
    name: 'Homepage',
    components:{
      Logo,
      tutorImage,
      CourseList
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
