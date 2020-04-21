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

              <el-tab-pane label="Tutor Setting" name="tutorsetting">
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
  
}
</script>

<style>
  .app-container{
    margin-top:515px
  }
</style>