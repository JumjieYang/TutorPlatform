<template>
  <div id="app">
    <nav-bar v-if="this.$store.state.token!=null"></nav-bar>
    <router-view></router-view>
    <chat v-show="isOpen"></chat>
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

