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
      height="350"
      border
      style="width: 100%">
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
        prop = 'detail'
        label = 'Course Detail'>
          <template slot-scope="scope">
            <el-col :span="6">
              <el-link icon="el-icon-info" type="primary" :href= "scope.row.url"></el-link>&nbsp;
            </el-col>
          </template>
        </el-table-column>
    </el-table>
  </el-container>
</template>
<script>
  import Logo from '../Home/Logo'
  import Search from "./Search";
  export default {
    components:{
      Logo,
      Search
    },
    data() {
      return {
        courses: [{
          value: 'Comp421',
          tutor: 'Stephen',
          rating: 3,
          url: '/'
        }, {
          value: 'Comp307',
          tutor: 'Kevin',
          rating: 4,
          url: '/'
        }, {
          value: 'Math223',
          tutor: 'Donald',
          rating: 5,
          url: '/'
        }, {
          value: 'Ecse321',
          tutor: 'Lee',
          rating: 4.3,
          url: '../search'
        }],
        state: '',
        timeout:  null,
        displayList: []
      }
    },
    created: function(){
      this.loadCourse();
    },
    methods: {
      // these are test data
      loadCourse(){
        this.axios.get("/api-course/courses/",{
            headers: { 'Authorization' : 'Token '+ this.$store.state.token}
        })
        .then((response) => {
            var courses = response.data
            for (var course of courses) {
                var courseInfo = {'course': course.subject + '' + course.number,
                                'tutor': course.tutor, 'rating': course.rating, url: '/'}
                console.log(courseInfo)
                this.displayList.push(courseInfo)
            }
        })
        .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
        })
        //this.displayList = this.courses;
      },
      loadAll() {
        return [
          { "value": "Comp421", "tutor": "Lee" },
          { "value": "Comp307", "tutor": "Cornell" },
          { "value": "Math323", "tutor": "Kobe" }
        ];
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
      refresh(){
        this.displayList = [];
        for(let i = 0; i < this.courses.length; ++i){
          this.displayList.push(this.courses[i]);
          console.log(this.displayList[i]);
        }
      }

    },
  }
</script>
