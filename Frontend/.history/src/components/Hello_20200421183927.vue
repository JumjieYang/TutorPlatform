<template>
  <div class="hello">
    <el-button @click="receive">Chat</el-button>
    {{chat}}
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
  methods:{
    receive(){
      this.axios.get('/chat/1').then((response) => {
            this.rooms = response.body
            console.log(response)
        })
    }
  }

}
</script>
