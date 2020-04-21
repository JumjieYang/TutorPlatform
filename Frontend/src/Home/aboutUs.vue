<template>
<el-container style = "align-self: center">
  <Logo></Logo>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/Home' }">Home Page</el-breadcrumb-item>
    <el-breadcrumb-item :to="{ path: '/courses' }">Courses list</el-breadcrumb-item>
  </el-breadcrumb>
  <el-header font-size = '50px'><h2>Who are we?</h2></el-header>
  <el-main>We are three cs major undergraduates and we are about entering our junior year.<br>
  Tutor Platform provides McGill students a variety of tutoring and study material that they will absolutely benefit from.<br>
  This simple but useful web project might have a big impact on our undergraduates' community.</el-main>
  <br><br><br>
  <el-footer>Author: Junjie Yang, Yizhong Ding, Hengxian Jiang</el-footer>

</el-container>
</template>

<script>
  import Logo from './Logo';
  export default {
    name: "aboutUs",
    components:{
      Logo
    }
  }
</script>

<style scoped>

</style>
