<template>
  <el-container>
    <remote-js src="https://js.squareupsandbox.com/v2/paymentform"></remote-js>
    <el-header><logo></logo></el-header>
    <br><br><br><br>
    <el-main>
      <div id="form-container">
        <div id="sq-card-number"></div>
        <div class="third" id="sq-expiration-date"></div>
        <div class="third" id="sq-cvv"></div>
        <div class="third" id="sq-postal-code"></div>
        <button id="sq-creditcard" class="button-credit-card" onclick="onGetCardNonce(event)">Pay $1.00</button>
      </div>
    </el-main>
  </el-container>
</template>
<script>
  import Logo from "../Home/Logo";

  export default {
    components: {
      Logo,
      'remote-js': {
        render(createElement) {
          return createElement('script', {attrs: {type: 'text/javascript', src: this.src}});
        },
        props: {
          src: { type: String, required: true}
        }
      }
    }
  }

</script>


<style scoped>

</style>
