
<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <h4>McGill Tutor Platform</h4>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/SignUp' }"><i class = 'el-icon-thumb'></i>Sign Up</el-breadcrumb-item>
        </el-breadcrumb>

        <el-form>
          <div class="title-container">
            <h3 class="title">Login page</h3>
          </div>

          <el-form-item>
            <el-input
              placeholder="Username"
              v-model="username"
              type="text"
            />
          </el-form-item>

          <el-tooltip placement="right" manual>
            <el-form-item v-if="visible">
              <el-input type="password" v-model="password" placeholder="Password">
                <i slot="suffix" title="show pass" @click="showPass('show')" style="cursor:pointer;"
                   class="el-icon-view"></i>
              </el-input>
            </el-form-item>
            <el-form-item v-else>
              <el-input
                placeholder="Password"
                v-model="password">
                <i slot="suffix" title="hide pass" @click="showPass('hide')" style="cursor:pointer;"
                   class="el-icon-view"></i>
              </el-input>
            </el-form-item>
          </el-tooltip>
        </el-form>
      </div>
    </el-main>
    <el-container style="align-self: center">
      <el-button type="primary" size="large" @click="submit">login</el-button>
    </el-container>
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
        visible: true
      };
    },
    methods:{
      submit() {
        const vm = this;
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
      },
      validateEmail(email){
        let re = /\S+@\S+\.\S+/;
        return re.test(email);
      },
      showPass(value) {
        this.visible = !(value === 'show');
      },
    }
  }

</script>
