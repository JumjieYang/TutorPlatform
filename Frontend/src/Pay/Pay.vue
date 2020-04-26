<template>
  <el-container>
    <el-header><logo></logo></el-header>
    <el-main>
      <div class="login-container">
        <el-form>
          <div class="title-container">
            <h3 class="title">Please enter your address</h3>
          </div>

          <el-form-item id = 'username'>
            <el-input
              placeholder="Address"
              v-model="address"
              type="text"
            />
          </el-form-item>
        </el-form>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  import Logo from '../Home/Logo'
  export default {
    name: "Pay",
    components: {
      Logo
    },
    data() {
      return {
        address: ''
      };
    },
  }
</script>

<style scoped>

</style>
