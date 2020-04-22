<template>
  <el-container>
    <el-container>
      <el-main>
        <h2>Come and join our <br> McGIll Tutor Community</h2>
        <tutorImage></tutorImage>
        <div class = 'coursesList'>
          <el-link href = '#/Courses'>Courses Preview</el-link>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  import Logo from './Logo'
  import tutorImage from './TutorImage'
  import CourseList from "../Courses/CourseList";
  export default {
    name: 'Homepage',
    components:{
      Logo,
      tutorImage,
      CourseList
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>

</style>
