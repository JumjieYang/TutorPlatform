<template>
  <div class="block">
    <el-card v-if="this.orders == null" shadow="always">
      <div>
        No order history. Place your first order!
      </div>
    </el-card>
    <el-timeline>
      <el-timeline-item v-for="(order,index) of orders" :key="index"  placement="top">
        <el-card>
            <h4>{{'Order Amount: ' + order.amount}}</h4>
            <p>{{ 'Order Address ' +order.address }}</p>
            <p>{{ 'Order Date ' +order.date }}</p>

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
        }
    },
    mounted(){
        this.axios.get("/api-order/orders/",{
            headers: { 'Authorization' : 'Token '+ this.$store.state.token}
        })
        .then((response) => {
            this.orders = response.data
        })
        .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
        })
    }

}
</script>