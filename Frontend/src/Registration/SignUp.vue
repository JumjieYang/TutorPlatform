<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/Home' }">Home Page</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/Login' }">Login</el-breadcrumb-item>
        </el-breadcrumb>
        <el-form @submit.prevent.native="validateEmail()">
          <div class="title-container">
            <h3 class="title">Tutor Platform</h3>
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
            this.axios.post("http://localhost:8000/api-auth/register/", {
                username: this.username,
                password: this.password
            })
            .then(function (response) {
                console.log(response);
                vm.$router.push('/Login')
                vm.$message({
                    message: 'Sign up sussessfully! Please log in.',
                    type: 'success'
                });
            })
            .catch(function (error) {
                vm.$message.error('Error. Maybe you entered a existing username.');
                console.log(error);
            });
        },
      validateEmail(){
        let email = document.getElementById('username').value;
        let re = /\S+@\S+\.\S+/;
        if(!re.test(email)){
          alert("You entered incorrect format for email, try again!");
        }
        return re.test(email);
      }
    },

  }
</script>
