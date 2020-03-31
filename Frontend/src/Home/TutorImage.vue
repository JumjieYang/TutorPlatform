<template>
  <div class="tutor-image">
    <div class="tutors" >
      <span class="demonstration"></span>
      <el-image
        v-for="(url,index) in urls " :key = "index"
        style="width: 300px; height: 300px"
        :src="url"
        :fit="fit"></el-image>
    </div>
  </div>
</template>

<script>
  export default {
    name: "TutorImage",
    data() {
      return {
        fit: 'fill',
        urls: ['./static/tutor1.png','./static/tutor2.png','./static/tutor3.png']
      };
    }
  }
</script>

<style scoped>

</style>
