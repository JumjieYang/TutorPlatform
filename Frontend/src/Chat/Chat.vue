<template>
    <div id="chat" class="chat"></div>
</template>

<script>
import $ from 'jquery';
export default {
    mounted: function(){
        var userId = this.$store.state.userId;
        var userName = this.$store.state.userName;
        $("#chat").kendoChat();
        var chat = $("#chat").data("kendoChat");
        chat.renderMessage({
            type: "text",
            text: "Welcome to TP"
        }, {
            id: kendo.guid(),
            name: "Big brother",
            iconUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQkGsD8I5_HnpduQhd3Spc2fqboGL5wIsnkaZSFdYmSZLcVzrlK&usqp=CAU"
        });
        
        const websock = new WebSocket('ws://localhost:8000/ws/chat/1/');


        chat.bind("sendMessage", chat_sendMessage);
        function chat_sendMessage(e) {
            const message = {
                command: 'new_message',
                message: {
                    author: userId,
                    text: e.text
                }
            };
            websock.send(JSON.stringify(message))
        }
        
        websock.onmessage = function(e) {
            const message = (JSON.parse(e.data));
            if(message.message.author != userId){
                chat.renderMessage({
                    type: "text",
                    text: message.message.text
                },  {
                    //id: kendo.guid(),
                    name: message.message.author,
                    iconUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQkGsD8I5_HnpduQhd3Spc2fqboGL5wIsnkaZSFdYmSZLcVzrlK&usqp=CAU"
                });
            }
        };

        websock.onclose = function(e) {
            console.error('websock  closed unexpectedly');
        };

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
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border-radius: 10px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        animation: fadeIn;
        animation-duration: 0.3s;
        animation-timing-function: ease-in-out;
        opacity: 1;
        z-index: 1000;
    }
</style>