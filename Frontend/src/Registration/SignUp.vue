<template>
  <div class="login-container">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/Home' }">Home Page</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/Login' }">Login</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form >
      <div class="title-container">
        <h3 class="title">Tutor Platform</h3>
      </div>
      <el-form-item>
        <el-input
          placeholder="Username"
          type="text"
        />
      </el-form-item>

      <el-tooltip placement="right" manual>
        <el-form-item prop="password">
        <el-input
            placeholder="Password"
            name="password"
        />
        </el-form-item>
      </el-tooltip>

      <el-button type="primary" style="width:100%;margin-bottom:30px;" >Sign Up</el-button>


    </el-form>

  </div>
</template>
