<template>
  <div id="app">
    <nav-bar v-if="this.$store.state.token!=null"></nav-bar>
    <router-view></router-view>
    <chat></chat>
    <div class="sc-launcher"  @click.prevent="isOpen = !isOpen" :style="{backgroundColor:'#4e8cff'}">
      <!-- <div v-if="newMessagesCount > 0 && !isOpen" class="sc-new-messsages-count">
        {{newMessagesCount}}
      </div> -->
      <img v-if="isOpen" class="sc-closed-icon" :src="icons.close.img"  :alt="icons.close.name" />
      <img v-else class="sc-open-icon" :src="icons.open.img"  :alt="icons.open.name" />
    </div>

  </div>
</template>

<script>
import CloseIcon from './Chat/close-icon.png'
import OpenIcon from './Chat/logo-no-bg.svg'
import Chat from './Chat/Chat'
import NavBar from './components/NevBar'
export default {
  name: 'app',
  components: {
    'NavBar': NavBar,
    'Chat': Chat
  },
  methods: {},
  data() {
        return {
            isOpen: false
        }
    },
  props: {
        icons:{
        type: Object,
        required: false,
        default: function () {
            return {
                open: {
                img: OpenIcon,
                name: 'default',
                },
                close: {
                img: CloseIcon,
                name: 'default',
                },
            }
        }
        },
    },
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.sc-launcher {
  width: 60px;
  height: 60px;
  background-position: center;
  background-repeat: no-repeat;
  position: fixed;
  right: 25px;
  bottom: 25px;
  border-radius: 50%;
  box-shadow: none;
  transition: box-shadow 0.2s ease-in-out;
  cursor: pointer;
}
.sc-launcher:before {
  content: '';
  position: relative;
  display: block;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  transition: box-shadow 0.2s ease-in-out;
}
.sc-launcher .sc-open-icon,
.sc-launcher .sc-closed-icon {
  width: 60px;
  height: 60px;
  position: fixed;
  right: 25px;
  bottom: 25px;
  transition: opacity 100ms ease-in-out, transform 100ms ease-in-out;
}
.sc-launcher .sc-closed-icon {
  transition: opacity 100ms ease-in-out, transform 100ms ease-in-out;
  width: 60px;
  height: 60px;
}
.sc-launcher .sc-open-icon {
  padding: 20px;
  box-sizing: border-box;
  opacity: 1;
}
.sc-launcher.opened .sc-open-icon {
  transform: rotate(-90deg);
  opacity: 1;
}
.sc-launcher.opened .sc-closed-icon {
  transform: rotate(-90deg);
  opacity: 1;
}
.sc-launcher.opened:before {
  box-shadow: 0px 0px 400px 250px rgba(148, 149, 150, 0.2);
}
.sc-launcher:hover {
  box-shadow: 0 0px 27px 1.5px rgba(0,0,0,0.2);
}
.sc-new-messsages-count {
  position: absolute;
  top: -3px;
  left: 41px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  border-radius: 50%;
	width: 22px;
  height: 22px;
  background: #ff4646;
  color: white;
  text-align: center;
  margin: auto;
  font-size: 12px;
  font-weight: 500;
}
</style>