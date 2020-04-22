<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1">处理中心</el-menu-item>
    <el-submenu index="2">
        <template slot="title">我的工作台</template>
        <el-menu-item index="2-1">选项1</el-menu-item>
        <el-menu-item index="2-2">选项2</el-menu-item>
        <el-menu-item index="2-3">选项3</el-menu-item>
        <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
        </el-submenu>
    </el-submenu>
    <el-menu-item index="3" disabled>消息中心</el-menu-item>
    <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
    </el-menu>


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