<template>
  <div id="app">
    <nav></nav>
    <router-view></router-view>
  </div>
</template>

<script>
import Nav from './components/NevBar'
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
