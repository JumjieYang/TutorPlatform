<template>
  <div id="app">
    <nav-bar v-if="this.$store.state.token!=null"></nav-bar>
    <router-view></router-view>
    <chat></chat>
  </div>
</template>

<script>
import Chat from './Chat/Chat'
import NavBar from './components/NevBar'
export default {
  name: 'app',
  components: {
    'NavBar': NavBar,
    'Chat': Chat
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
