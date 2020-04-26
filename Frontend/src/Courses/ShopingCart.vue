<template>
  <div id = 'app'>
    <logo></logo>
    <br><br>
    <el-breadcrumb separator="|">
      <el-breadcrumb-item  :to="{ path: '/Home' }"><i class = "el-icon-caret-left"></i>Home Page</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/Profile' }">Profile</el-breadcrumb-item>
    </el-breadcrumb>
    <br>
    <el-table :data="cartInfo" border style="width: 100%" @selection-change="selected"empty-text="No item found">
      <el-table-column type="selection" width="50"> </el-table-column>
      <el-table-column label="Course Title" width="500" align="align-self: center">
        <template slot-scope="cartInfo">
          <div style="margin-left: 50px">
            <span style="font-size: 18px;padding-left: 200px;">{{cartInfo.row.title}}</span>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Price" width="150" prop="price">
        <template slot-scope="cartInfo">
          <div style="margin-left: 50px">
            <span style="font-size: 18px;padding-left: 200px;">{{cartInfo.row.title}}</span>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Quantity" width="200">

        <template slot-scope="cartInfo">
          <div>
            <el-input v-model="cartInfo.row.quantity" @change="handleInput(cartInfo.row)">
              <el-button slot="prepend" @click="del(cartInfo.row)">
                <i class="el-icon-minus"></i>
              </el-button>
              <el-button slot="append" @click="add(cartInfo.row)">
                <i class="el-icon-plus"></i>
              </el-button>
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Total" width="150" prop="totalPrice"> </el-table-column>
      <el-table-column label="Edit">
        <template scope="scope">
          <el-button type="danger" @click="handleDelete(scope.$index, scope.row)"> Delete
            <i class="el-icon-delete2 el-icon--right"></i>
          </el-button>
        </template>
      </el-table-column>
    </el-table> <br>
    <el-button type="info" >{{"Total Price：" + moneyTotal}}</el-button>
    <el-button type="primary" style="float: right" size="small" @click="submitBtn()">Check Out<i class="el-icon-upload el-icon--right"></i></el-button>
  </div>
</template>
<script>
  import Logo from '../Home/Logo'
  export default {
    name: "ShopingCart",
    components: {
      Logo
    },
    data() {
      return {
        tableData: [
          {
            title: 'Comp421 Final Review',
            price: 149,
            quantity: 1,
            totalPrice: 149,
          },
        ],
          cartInfo: [],
        moneyTotal: 0,
        multipleSelection: [],
      }
    },
    methods: {
      loadCart(){
        this.axios.get("/api-course/carts/",{
          headers: { 'Authorization' : 'Token '+ this.$store.state.token}
        })
          .then((response) => {
            let carts = response.data
            for (let cart of carts) {
              this.cartInfo.push({'title': cart.user + '',
                'price':cart.total, 'quantity': 1, 'totalPrice':cart.total})
            }
          })
          .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
          })
      },
      handleDelete(index, row) {
        this.$confirm('Are you sure about delete that course？', 'Warning', {
          confirmButtonText: 'confirm',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          this.cartInfo.splice(index,1);
          this.$message({type: 'success', message: 'Deletion success!'});
        }).catch(() => {
          this.$message({type: 'info', message: 'Deletion canceled'});
        });
      },
      handleInput: function (value) {
        if (null == value.quantity || value.quantity == "") {
          value.quantity = 1;
        }
        if(value.quantity < 0){
          this.$message({type: 'info', message: 'Negative Quantity is not allowed'});
          value.quantity = 0;
        }
        value.totalPrice = (value.quantity * value.price);
        this.selected(this.multipleSelection);
      },
      add: function (addGood) {
        //v-model achive double data bind
        if (typeof addGood.quantity == 'string') {
          addGood.quantity = parseInt(addGood.quantity);
        };
        addGood.quantity += 1;
        addGood.totalPrice += addGood.price;
      },
      del: function (delGood) {
        // parse string input to integer first
        if (typeof delGood.quantity == 'string') {
          delGood.quantity = parseInt(delGood.quantity);
        }
        ;
        if (delGood.quantity > 0) {
          delGood.quantity -= 1;
          delGood.totalPrice -= delGood.price;
        }
      },
      selected: function (selection) {
        this.multipleSelection = selection;
        this.moneyTotal = 0;
        for (let i = 0; i < selection.length; i++) {
          //to see if the return data tyoe is string
          if (typeof selection[i].totalPrice == 'string') {
            selection[i].totalPrice = parseInt(selection[i].totalPrice);
          }
          ;
          this.moneyTotal += selection[i].totalPrice;

        }
      },
      submitBtn: function (){
          // this.$router.push({path:'/index.html'})
      }
    }
  }
</script>

<style>
</style>
