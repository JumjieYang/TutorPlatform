<template>
    <el-container>
    <el-col :span="20">
        <el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal">
            <el-menu-item index="/aboutUs">About us</el-menu-item>
            <el-submenu index="2">
                <template slot="title">Courses</template>
                <el-menu-item index="/Courses">View Courses</el-menu-item>
                <el-menu-item index="/Search">Search</el-menu-item>
                <el-menu-item index="/shopingCart">shopingCart</el-menu-item>
            </el-submenu>
            <el-menu-item index="/Profile">Profile</el-menu-item>
        </el-menu>
    </el-col>
    <el-col :span="4">
        <img src='./../assets/logo.jpg' alt="" class="navbar__logo">
    </el-col>
    </el-container>
    

</template>

<script>
import logo from './../assets/logo.jpg'
export default {
    
}
</script>

<style>
.navbar__logo {
    display: block;
    height: 60px;
    margin-left: auto;
    margin-right: auto;
}
</style>