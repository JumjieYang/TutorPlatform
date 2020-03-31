<template>
  <el-container>
    <el-header>
      <logo></logo>
      <h1>McGill Tutor Platform</h1>
    </el-header>
    <br><br><br><br><br><br><br>
    <el-table
      cell-style="font-weight: 700"
      :data="courseInfo"
      height="350"
      border
      style="width: 100%">
      <div class = 'courseNum'>
        <el-table-column
          prop="course"
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
          score-template="{value}">
          <template slot-scope="scope">
            <el-rate v-model="scope.row.value" :allow-half="true"  show-score disabled text-color="#ff9900"></el-rate>
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
  export default {
    components:{
      Logo
    },
    data() {
      return {
        courseInfo: [{
          course: 'Comp421',
          tutor: 'Stephen',
          value: 3,
          url: '/'
        }, {
          course: 'Comp307',
          tutor: 'Kevin',
          value: 4,
          url: '/'
        }, {
          course: 'Math223',
          tutor: 'Donald',
          value: 5,
          url: '/'
        }, {
          course: 'Ecse321',
          tutor: 'Lee',
          value: 4.3,
          url: '../search'
        }],

      }
    }
  }
</script>
