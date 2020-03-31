<template>
  <div class="demo-image">
    <div class="block" >
      <span class="demonstration"></span>
      <el-image
        style="width: 100px; height: 100px"
        :src="url"
        :fit="fits"></el-image>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        fits: 'contain',
        url: './static/TP_logo.jpg'
      }
    }
  }
</script>

<style scoped>

</style>
