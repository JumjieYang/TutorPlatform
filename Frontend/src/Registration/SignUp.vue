<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/Home' }">Home Page</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/SignUp' }">Login</el-breadcrumb-item>
        </el-breadcrumb>
        <el-form>
          <div class="title-container">
            <h3 class="title">Tutor Platform</h3>
          </div>

          <el-form-item>
            <el-input
              placeholder="Username"
              type="text"
              @keyup.enter = 'submit'
            />
          </el-form-item>

          <el-tooltip placement="right" manual>
            <el-form-item prop="password">
              <el-input
                placeholder="Password"
                name="password"
                @keyup.enter = "submit"
              />
            </el-form-item>
          </el-tooltip>
        </el-form>
        <el-button type="primary" style="width:100%;margin-bottom:30px;"  @click="submit" >Sign Up</el-button>

      </div>
    </el-main>
  </el-container>

</template>

<script>
  import Logo from '../Home/Logo'
  export default {
    name: 'Homepage',
    components: {
      Logo
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods:{
      submit() {
        console.log(666)
      }
    }
  }
</script>
