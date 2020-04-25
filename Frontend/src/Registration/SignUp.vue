<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/Login' }"><i class="el-icon-thumb"></i>Login</el-breadcrumb-item>
        </el-breadcrumb>
        <el-form>
          <div class="title-container">
            <h3 class="title">Sign Up page</h3>
          </div>

          <el-form-item id = 'username'>
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
      </div>
    </el-main>
    <el-container style="align-self: center">
      <el-button type="primary" style="width:100%;margin-bottom:30px;"  @click="submit" >Sign Up</el-button>
    </el-container>
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
            username: '',
            password: '',
            activeIndex: '1',
            activeIndex2: '1',
        };
    },
    methods:{
        submit() {
            console.log(666);
            const vm = this;
            this.axios.post("/api-auth/register/", {
                username: this.username,
                password: this.password
            })
            .then(function (response) {
                console.log(response);
                vm.login()
                vm.$message({
                    message: 'Sign up sussessfully! Please create your personal profile.',
                    type: 'success'
                });
            })
            .catch(function (error) {
                vm.$message.error('Error. Please try again.');
                console.log(error);
            });
        },
        login(){
          const vm = this;
          this.$store.dispatch('retrieveToken',  {
            username: this.username,
            password: this.password
          })
          .then(function (response) {
            vm.$router.push('/CreateProfile')
          })
          .catch(function (error) {
            vm.$message.error('Please try again.');
          });
        }
    },

  }
</script>
