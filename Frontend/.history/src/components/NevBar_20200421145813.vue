<template>
    <div>
    <el-header>
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
        
    </div>
</template>