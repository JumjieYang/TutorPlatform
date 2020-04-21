<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(order,index) of orders" :key="index"  placement="top">
        <el-card>
          <!-- <h4>{{ order}}</h4>
          <p>{{ order }}</p> -->
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
    data() {
        return {
            orders: ''
        // timeline: [
        //     {
        //     timestamp: '2019/4/20',
        //     title: 'Comp 424',
        //     content: 'Midterm Prep'
        //     },
        //     {
        //     timestamp: '2019/4/21',
        //     title: 'Comp 535',
        //     content: 'Project help'
        //     },
        //     {
        //     timestamp: '2019/4/22',
        //     title: 'Comp 421',
        //     content: 'Assignment asistance'
        //     },
        //     {
        //     timestamp: '2019/4/23',
        //     title: 'Comp 360',
        //     content: 'Tutorial'
        //     }
        // ]
        }
    },
    mounted(){
        this.axios.get("/api-order/orders/",{
            headers: { 'Authorization' : 'Token '+'2b25b6b3b6231f1905206c1b62d436194b826546'}
        })
        .then((response) => {
            this.orders = response.data
            console.log("==============order===============\n"+response.data+"\n==============order===============")
        })
        .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
        })
    }

}
</script>