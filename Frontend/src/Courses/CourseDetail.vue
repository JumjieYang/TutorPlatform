<template>
  <el-container>
    <el-header>
      <logo></logo>
      <h1>Course Description</h1>
    </el-header>
    <br><br><br><br> <br><br>
    <el-table
      id = 'courses'
      :data="course"
      height="350"
      border
      style="width: 100%">
      <div class = 'Instructor'>
        <el-table-column
          prop="description"
          label="Instructor Information"
          width="400"
        >
        </el-table-column>
        <i class = 'el-icon-info'>info</i>
      </div>
      <el-table-column
        prop="evaValue"
        label="Rating"
        score-template="{rating}">
        <template slot-scope="course">
          <el-rate v-model="course.row.rating" :allow-half="true"  show-score disabled text-color="#ff9900"></el-rate>
        </template>
      </el-table-column>
      <el-table-column
        prop = 'chat'
        label = 'Chat With Tutor'
        width="150">
        <template slot-scope="course">
          <el-col :span="6">
            <el-button icon="el-icon-s-comment" type="primary" @click = "chat()"></el-button>&nbsp;
          </el-col>
        </template>
      </el-table-column>
    </el-table>
    <el-container style="align-self: center">
      <el-button type="primary" style="float: right" size="small" @click="addToCart()">Add to cart<i class="el-icon-upload el-icon--right"></i></el-button>
    </el-container>
  </el-container>
</template>

<script>
  import Logo from "../Home/Logo";
  import Search from "./Search";
  import ShopingCart from "./ShopingCart";
  export default {
    name: "CourseDetail",
    components:{
      Logo,
      Search,
      ShopingCart
    },
    data(){
      return{
        cargo:[
          {
            title: 'Comp421 Final Review',
            price: 149,
            quantity: 1,
            totalPrice: 149,
          },
          {
            title: 'Comp307 Project Help',
            price: 29,
            quantity: 1,
            totalPrice: 29,
          }
        ],
        title: '',
        price: '',
        course: [{}],
        id: this.$route.params.id
      }
    },
    created: function () {
      this.loadCourse(this.$route.params.id);
    },
    methods:{
      loadCourse(id){
        this.axios.get("/api-course/courses/"+id+'/', {
          headers: {'Authorization': 'Token ' + this.$store.state.token}
        })
          .then((response) => {
            this.course.push(response.data)
          })
          .catch((error) => {
            console.log(error);
            this.$message.error('Course loading encountered a problem.');
          })
      },
       addToCart(){
        console.log(this.id)
        const instance = this.axios.create({
          headers: {
            Authorization: 'Token '+ this.$store.state.token,
            'Content-Type': 'application/json'
          },
        });
        instance({
          url: '/api-course/carts/',
          data: {
            number: this.course.number,
            total: this.course.price,
            user: this.$store.state.userId,
            course: this.course.subject,
          },
          method: "POST",
        })
          .then((response) => {
            console.log(response.data);
            this.$message({
              message: 'add to cart sussessfully!',
              type: 'success'
            });
          })
          .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
          })
      },
      chat(){
        this.$router.push({path: '/chat'})
      }
    },
  }
</script>
