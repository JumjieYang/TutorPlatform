<template>
  <el-container>
    <el-header><Logo></Logo></el-header>
    <br><br>
    <el-main>
      <div class="cart">
      <div style="margin: 15px 0;"></div>
      <el-checkbox-group v-model="checkedGoods" @change="handleOneChange" class="items">
        <el-checkbox v-for="course in courses" :label="course.name" :key="course.id">
          <span style="width:150px;display:inline-block">Course Number： {{course.name}}</span>
          <span style="width:150px;display:inline-block;margin-left:100px;margin-right:100px">Course Price：$ {{course.price}}</span>
          <span>
            <i class ='el-icon-shopping-cart-1'></i>Quantity:
            <el-input-number v-model="course.num" @change="handleChangeNum(course.id)" label="description" size="small"></el-input-number>
          </span>
          <span style="width:150px;display:inline-block;margin-left:100px;margin-right:100px">In total： ${{course.OnePrice}}</span>
        </el-checkbox>
      </el-checkbox-group>
      <div style="margin-top:40px;margin-left:450px;text-align:left">
        <span style="margin-right:20px;display:inline-block" v-model="allPrice">Total Price：$ {{allPrice}}</span>
        <el-button type="primary" size="small" @click="submitBtn">Check Out<i class="el-icon-upload el-icon--right"></i></el-button>
      </div>

    </div>
    </el-main>
  </el-container>

</template>

<script>
  import Logo from '../Home/Logo'
  // const goodOptions = ["哇哈哈", "辣条", "矿泉水", "西瓜", "苹果"];
  export default {
    name: "ShopingCart",
    components:{
      Logo
    },
    data() {
      return {
        courses: [
          {
            id: 1,
            name: "Comp421",
            price: 32
          },
          {
            id: 2,
            name: "Comp307",
            price: 12
          },
          {
            id: 3,
            name: "Math323",
            price: 2
          },
          {
            id: 4,
            name: "Comp251",
            price: 60
          },
          {
            id: 5,
            name: "Math324",
            price: 99
          }
        ],
        checkAll: false,
        isIndeterminate: true,
        checkedGoods: [],
        allPrice: 0
      };
    },
    methods: {
      handleAllChange(val) {
        console.log(val, "555");
        this.checkedGoods = val ? goodOptions : [];
        this.isIndeterminate = false;
        if (val) {
          this.getAllPrice();
        } else {
          this.allPrice = 0;
        }
      },
      handleOneChange(value) {
        let all = 0;
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.checkedGoods.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.checkedGoods.length;
        value.filter((it, id) => {
          if (it == this.courses[id].name) {
            if (this.courses[id].price) {
              all += this.courses[id].price;
            }
          }
        });
        this.allPrice = all;
      },
      handleChangeNum(val) {
        this.courses.filter((it, id) => {
          if (it.id == val) {
            it.OnePrice = it.num * it.price;
          }
        });
        this.getAllPrice();
      },
      getAllPrice() {
        // encapsulate getTotal Price
        let money = 0;
        this.courses.filter((it, id) => {
          if (it.OnePrice) {
            money += it.OnePrice;
          }
        });
        this.allPrice = money;
      },
      submitBtn() {
        this.$alert( "$"+this.allPrice, "The total price will be",{
          confirmButtonText: "Confirm",
          callback: action => {
            this.$message({
              type: "info",
              message: ""
            });
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
