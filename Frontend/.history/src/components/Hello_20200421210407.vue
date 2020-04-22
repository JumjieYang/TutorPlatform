<template>
  <div class="hello">
    <el-button @click="receive">Chat</el-button>
    {{chat}}
    <p id="chat-thread-1"></p>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      chat: ''
    }
  },
  mounted(){
    const thread = document.getElementById('chat-thread-1')
    const conn = new WebSocket('ws://127.0.0.1:8000/chat/1')


    conn.onclose = function(event) {
      console.log('Connection closed')
    }

    conn.onmessage = function(event) {
      console.log('Message received.')
      const message = document.createElement('p')
      message.textContent = event.data
      thread.append(message)
    }
  },
  methods:{
    receive(){
      this.axios.get('/chat/1').then((response) => {
            this.chat = response.data.data
            console.log(response)
        })
    },

  }

}
</script>
