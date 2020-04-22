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
    <el-col :span="20">
        <img src='../../../static/TP_logo.jpg' alt="" class="navbar__logo">
    <el-col :span="20">
    </el-container>
    
            


<!-- 


    <el-menu  router :default-active="$route.path" class="el-menu-demo" mode="horizontal" >
        <el-menu-item index="/aboutUs">
            <i class = 'el-icon-info'></i>
            About Us
        </el-menu-item>

        <el-submenu index="/aboutUs">

            <template slot="title" >
                <i class = 'el-icon-menu'></i>
                Sign Up/Login</template>

            <el-menu-item index="/SignUp">
                <i class = 'el-icon-unlock'></i>
                Sign Up
            </el-menu-item>
            
            <el-menu-item index="/Login">
                <i class = 'el-icon-key'></i>
                Login
            </el-menu-item>
        </el-submenu>
        <el-menu-item index="/Profile" >
            <i class = 'el-icon-s-custom'></i>
            Personal Profile</el-menu-item>
    </el-menu> -->
</template>