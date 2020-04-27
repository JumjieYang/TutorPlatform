<template>
  <el-container>
    <el-header>
       <logo></logo>
      <h1>Courses List</h1>
    </el-header>
    <br><br><br><br>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item  :to="{ path: '/Home' }"><i class = "el-icon-caret-left"></i>Home Page</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/shopingCart' }">ShoppingCart</el-breadcrumb-item>
    </el-breadcrumb>
    <br><br><br>
    <h2 style="align-self: flex-start">Search Bar</h2>
    <div @click="refresh" >
      <i class="el-icon-refresh">refresh courses list</i>
    </div>
    <el-autocomplete
      v-model="state"
      :fetch-suggestions="querySearchAsync"
      placeholder="type the course information"
      @select="handleSelect"
      @click = "handleClick"
    ></el-autocomplete>
    <el-table
      :data="displayList"
      border
      style="width: 100% ;height: 100% "
      empty-text="No course found">
      <div class = 'courseNum'>
        <el-table-column
          prop="value"
          label="Course_Number"
          width="250">
        </el-table-column>
        <i class = 'el-icon-info'></i>
      </div>
      <el-table-column
        prop="tutor"
        label="Tutor"
        width="250">
      </el-table-column>
        <el-table-column
          prop="evaValue"
          label="Rating"
          score-template="{rating}">
          <template slot-scope="scope">
            <el-rate v-model="scope.row.rating" :allow-half="true"  show-score disabled text-color="#ff9900"></el-rate>
          </template>
        </el-table-column>

        <el-table-column
        prop = 'id'
        label = 'Course Detail'>
          <template slot-scope="displayList">
            <el-col :span="6">
              <el-button @click="showDetail(displayList.row.id)">course detail</el-button>
            </el-col>
          </template>
        </el-table-column>
    </el-table>
  </el-container>
</template>
<script>
  import Logo from '../Home/Logo'
  import Search from "./Search";
  import CourseDetail from './CourseDetail'
  export default {
    components: {
      Logo,
      Search,
      CourseDetail
    },
    data() {
      return {
        courses: [],
        state: '',
        timeout: null,
        displayList: [],
        names: []
      }
    },
    created: function () {
      this.loadCourse();
    },
    methods: {
      loadCourse() {
        this.axios.get("/api-course/courses/", {
          headers: {'Authorization': 'Token ' + this.$store.state.token}
        })
          .then((response) => {
            let courses = response.data
            for (let course of courses) {
              let courseInfo = {
                'value': course.subject + '' + course.number,
                'tutor': course.tutor, 'rating': course.rating, 'id': course.id
              }
              this.axios.get("/api-user/tutor/"+courseInfo.tutor,{
                headers: {'Authorization': 'Token ' + this.$store.state.token}
              })
                .then((response) => {
                  let profile = response.data
                  courseInfo.tutor = profile.firstName+' '+profile.lastName
                })
              this.displayList.push(courseInfo)
              this.courses.push(courseInfo)
            }
    })
          .catch((error) => {
            console.log(error);
            this.$message.error('Course loading encountered a problem.');
          })
      },
      castTutorName(){
        for(let course of this.courses){
          let courseWithTutor = {

          }
        }
      },
      querySearchAsync(queryString, cb) {
        let courses = this.courses;
        let results = queryString ? courses.filter(this.createStateFilter(queryString)) : courses;

        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 300 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
        this.displayList = [];
        this.displayList.push(item);
        console.log(item);
      },
      handleClick() {
        this.displayList = this.courses;
      },
      refresh() {
        this.displayList = [];
        for (let i = 0; i < this.courses.length; ++i) {
          this.displayList.push(this.courses[i]);
          console.log(this.displayList[i]);
        }
      },
      showDetail(id) {
        this.$router.push({name: 'CourseDetail',params: { id: id }})
      },
    }
  }
</script>
