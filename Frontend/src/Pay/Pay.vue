<template>
  <el-container>
    <remote-js src="https://js.squareupsandbox.com/v2/paymentform"></remote-js>
    <link type="text/css" src="mysqpaymentform.css"rel="stylesheet">
<!--    <script type="text/javascript" src="./static/payment.js"></script>-->
    <el-header><logo></logo></el-header>
    <br><br><br><br>
    <el-main>
      <VueCardPayment :settings="{
    labels: {
        cardNumber: 'Card number',
        month: 'Month',
        year: 'Year',
        cardHolder: 'Cardholder name',
        button: 'Double check information!'
    },
    placeholders: {
        cardNumber: '0000 0000 0000 0000',
        month: '00',
        year: '00',
        cardHolder: 'Holder name',
        cvv: '000'
    },
    showBank: true,
    showPaymentSystem: true
  }" @card-submit=''></VueCardPayment>
      <div id="form-container">
        <div id="sq-card-number"></div>
        <div class="third" id="sq-expiration-date"></div>
        <div class="third" id="sq-cvv"></div>
        <div class="third" id="sq-postal-code"></div>
        <el-button type="primary" style="align-self: center" size="small" @click="alert()">Pay</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script type="text/javascript">
  import Logo from "../Home/Logo";
  export default {
    components: {
      Logo,
    },

    methods:{
      alert(){
        alert("payment success")
        this.$router.push({path: '/Profile'})
      }
    }
  }
</script>

<style scoped>

</style>
