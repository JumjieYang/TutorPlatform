<template>
  <div class="block">
    <el-dialog title="Rating" :visible.sync="dialogVisible">
        <span>Please rate this order</span>
        <el-form style="margin-top:10px;">
            <el-form-item >
                    <el-rate v-model="value"></el-rate>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button size="mini" type="primary" @click="submitEdit">save change</el-button>
        </div>
    </el-dialog>
    <el-timeline>
      <el-timeline-item v-for="(order,index) of orders" :key="index"  placement="top">
        <el-card>
            <h4>{{'Order Amount: ' + order.amount}}</h4>
            <p>{{ 'Order Address ' +order.address }}</p>
            <p>{{ 'Order Date ' +order.date }}</p>
            <el-rate
                v-model="order.rating"
                show-score
                text-color="#ff9900">
            </el-rate>
            <el-button @click="editCourse(order)" style="float: right; padding: 3px 0" type="text">Edit</el-button>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
    data() {
        return {
            orders: '',
            value: 0,
            dialogVisible: false,
            myOrder : null
        }
    },
    methods:{
        submitEdit(){
            this.dialogVisible = false
            const userId = this.$store.state.userId
            const instance = this.axios.create({
                headers: {
                    Authorization: 'Token '+ this.$store.state.token,
                    'Content-Type': 'application/json'
                },
            });
            instance({
                url: '/api-order/order/'+this.myOrder.id,
                data: {
                    rating : this.value
                },
                method: "PATCH",
            })
            .then((response) => {
                this.$message({
                    message: 'Edited sussessfully!',
                    type: 'success'
                });
                this.value = 0
                this.updateOrder()
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        },
        editCourse(order){
            this.myOrder = order
            this.dialogVisible = true
        },
        updateOrder(){
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
    },
    mounted(){
        this.updateOrder()
    }

}
</script>
