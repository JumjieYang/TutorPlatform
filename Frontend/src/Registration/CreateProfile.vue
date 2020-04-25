<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <!-- <h4>Please Create your profile</h4> -->
        <el-form>
          <div class="title-container">
            <h3 class="title">Please Create your profile</h3>
          </div>

          <el-form-item id = 'username'>
            <el-input
              placeholder="firstName"
              v-model="firstName"
              type="text"
            />
          </el-form-item>

            <el-form-item >
              <el-input
                placeholder="lastName"
                type="text"
                v-model="lastName"
              />
            </el-form-item>

            <el-form-item >
              <el-input
                placeholder="age"
                type="number"
                v-model="age"
              />
            </el-form-item>

            <el-form-item >
              <el-input
                placeholder="phoneNumber"
                type="number"
                v-model="phoneNumber"
              />
            </el-form-item>

            <el-col :span="20" style="text-align: left; margin-bottom:10px;">Become a tutor</el-col>
            <el-col :span="4">
                <el-switch
                    v-model="isTutor">
                </el-switch>
            </el-col>

        </el-form>
        
      </div>
    </el-main>
    <el-container style="align-self: center">
      <el-button type="primary" style="width:100%;margin-bottom:30px;"  @click="submit" >Create</el-button>
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
            firstName: '',
            password: '',
            lastName:'',
            phoneNumber: '',
            age: '',
            isTutor: false
        };
    },
    methods:{
        submit() {
            const userId = this.$store.state.userId
            //console.log(userId)
            const vm = this;
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            instance({
                url: '/api-user/profiles/',
                data: {
                    user: userId,
                    firstName: this.firstName,
                    lastName: this.lastName,
                    age: this.age,
                    phoneNumber: this.phoneNumber,
                    isTutor: this.isTutor,
                    //image: ...,
                },
                method: "POST",
            })
            .then(function (response) {
                console.log(response);
                vm.$router.push('/Home')
                vm.$message({
                    message: 'Created sussessfully!',
                    type: 'success'
                });
            })
            .catch(function (error) {
                vm.$message.error('Error. Please try again');
                console.log(error);
            });
        },
    },

  }
</script>
