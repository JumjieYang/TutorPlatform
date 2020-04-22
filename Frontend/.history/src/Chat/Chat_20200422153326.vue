<template>
    <div id="chat" class="chat"></div>
</template>

<script>
import $ from 'jquery';
export default {
    data () {
        return {
            websock:null
        }
    },
    methods: {
        initWebSocket(){ 
            console.log("socket created")
            this.websock = new WebSocket('ws://localhost:8000/ws/chat/1/');
            this.websock.onmessage = this.websocketonmessage;
            //this.websock.onopen = this.websocketonopen;
            //this.websock.onerror = this.websocketonerror;
            //this.websock.onclose = this.websocketclose;
        },
        websocketonerror(){
            this.initWebSocket();
        },
        websocketonmessage(e){
            //this.$set(this.redata, Object.keys(redata).length, e.data)
            const message = (JSON.parse(e.data));
            var chat = $("#chat").data("kendoChat");
            chat.renderMessage({
                type: "text",
                text: message.message
            }, chat.getUser());
        },
        websocketsend(Data){//数据发送
            this.websock.send(Data);
        },
        websocketclose(e){  //关闭
            console.log('断开连接',e);
        },
    },
    mounted: function(){
        $("#chat").kendoChat();
        var chat = $("#chat").data("kendoChat");
        chat.renderMessage({
            type: "text",
            text: "Hello World"
        }, {
            id: kendo.guid(),
            name: "Tester",
            iconUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQkGsD8I5_HnpduQhd3Spc2fqboGL5wIsnkaZSFdYmSZLcVzrlK&usqp=CAU"
        });

        this.websock = new WebSocket('ws://localhost:8000/ws/chat/1/');
        this.websock.onmessage = this.websocketonmessage;
        this.websock.onopen = this.websocketonopen;
        this.websock.onerror = this.websocketonerror;
        this.websock.onclose = this.websocketclose;

                //send message
        chat.bind("sendMessage", sendMessage);
        function sendMessage(e) {
            var message = {"test": e.text};
            this.websocketsend(JSON.stringify(message));
        }

    }
}
</script>

<style>
    .chat{
        width: 370px;
        height: calc(100% - 120px);
        max-height: 590px;
        position: fixed;
        right: 25px;
        bottom: 100px;
        box-sizing: border-box;
        box-shadow: 0px 7px 40px 2px rgba(148, 149, 150, 0.1);
        /* background: white; */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border-radius: 10px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        animation: fadeIn;
        animation-duration: 0.3s;
        animation-timing-function: ease-in-out;
        opacity: 1;
    }
</style>