<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/Home' }">Home Page</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/SignUp' }">Sign Up</el-breadcrumb-item>
        </el-breadcrumb>

        <el-form>
          <div class="title-container">
            <h3 class="title">Tutor Platform</h3>
          </div>

          <el-form-item>
            <el-input
              placeholder="Username"
              v-model="username" 
              type="text"
            />
          </el-form-item>

          <el-tooltip placement="right" manual>
            <el-form-item >
              <el-input
                placeholder="Password"
                type="password"
                v-model="password"
              />
            </el-form-item>
          </el-tooltip>
        </el-form>
        <el-button type="primary" style="width:100%;margin-bottom:30px;"  @click="submit">Login</el-button>

      </div>
    </el-main>
  </el-container>

</template>

<script>
  import Logo from '../Home/Logo'   
  import router from './../router/index' 

  export default {
    name: 'Homepage',
    components: {
      Logo
    },
    data() {
      return {
        username: '',
        password: '',
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods:{
      submit() {
            const vm = this;
            //console.log(666);
            this.$store.dispatch('retrieveToken',  {
                username: this.username,
                password: this.password
            })
            .then(function (response) {
                vm.$router.push('/Home')
            })
            .catch(function (error) {
                vm.$message.error('Please try again.');
            });
        }
    }
  }
</script>
