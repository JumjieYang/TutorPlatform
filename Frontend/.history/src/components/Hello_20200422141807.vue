<template>
  <div class="hello">
    <el-button></el-button>
    <p>Chat Content: </p>
  </div>
</template>


<script src="https://cdn.jsdelivr.net/npm/reconnecting-websocket@4.1.10/dist/reconnecting-websocket-cjs.min.js"></script>
    
      <script src="https://cdn.jsdelivr.net/npm/vue-websocket@0.2.3/dist/vue-websocket.min.js"></script>
<script>
export default {
  name: 'hello',
  data () {
    return {
      websock: null,
    }
  },
  created() {
    this.initWebSocket();
  },
  destroyed() {
    this.websock.close() //离开路由之后断开websocket连接
  },
  methods: {
    initWebSocket(){ //初始化weosocket
      //const wsuri = "ws://localhost:6379";
      this.websock = new WebSocket('ws://localhost:8000/ws/chat/2/');
      this.websock.onmessage = this.websocketonmessage;
      this.websock.onopen = this.websocketonopen;
      this.websock.onerror = this.websocketonerror;
      this.websock.onclose = this.websocketclose;
    },
    websocketonopen(){ //连接建立之后执行send方法发送数据
      let actions = {"message":"12345"};
      this.websocketsend(JSON.stringify(actions));
    },
    websocketonerror(){//连接建立失败重连
      this.initWebSocket();
    },
    websocketonmessage(e){ //数据接收
      const redata = JSON.parse(e.data);
    },
    websocketsend(Data){//数据发送
      this.websock.send(Data);
    },
    websocketclose(e){  //关闭
      console.log('断开连接',e);
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
