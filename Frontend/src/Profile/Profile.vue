<template>
  <div class="app-container"> 
    <div>
      <el-row :gutter="20">

        <el-col :span="6" :xs="24">
          <user-card/>
        </el-col>

        <el-col :span="18" :xs="24">
          <el-card>
            <el-tabs v-model="activeTab">
              <el-tab-pane label="Order History" name="orderhistory">
                <order-history/>
              </el-tab-pane> 
              
              <el-tab-pane label="Account Setting" name="accountsetting">
                <account-setting/>
              </el-tab-pane> 

              <el-tab-pane v-if="this.$store.state.isTutor" label="Tutor Setting" name="tutorsetting">
                <tutor-setting/>
              </el-tab-pane> 
            </el-tabs>
          </el-card>
        </el-col>

      </el-row>
    </div>
  </div>
</template>

<script>
import UserCard from './UserCard'
import AccountSetting from './AccountSetting'
import TutorSetting from './TutorSetting'
import OrderHistory from './OrderHistory'
export default {
  name: 'Profile',
  components: { 
    UserCard,
    OrderHistory,
    AccountSetting,
    TutorSetting
  },
  data() {
    return {
      user: {},
      activeTab: 'orderhistory'
    }
  },
  mounted(){
    this.axios.get('/api-user/profile/'+this.$store.state.userId+'/',{
        headers: { 'Authorization' : 'Token '+ this.$store.state.token}
    })
    .then((response) => {
        this.$store.commit('setIsTutor',response.data.isTutor)
        this.$store.commit('setProfileImage',response.data.image)
        this.$store.commit('setInfo',{
            firstName: response.data.firstName,
            lastName: response.data.lastName,
            phone: response.data.phoneNumber,
            age: response.data.age})
        this.image = this.$store.state.profileImage
        this.info = this.$store.state.info
    })
    .catch((error) => {
        console.log(error);
        this.$message.error('Please try again.');
    })
    },
  
}
</script>

<style>
  .app-container{
    margin-top:15px;
    margin-left: 15px;
    margin-right: 15px;
    
  }
</style>