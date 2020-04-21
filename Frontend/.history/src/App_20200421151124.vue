<template>
  <div id="app">
    <nav-bar v-if="this.$store.state.token!=null"></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NevBar'
export default {
  name: 'app',
  components: {
    'NavBar': NavBar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
