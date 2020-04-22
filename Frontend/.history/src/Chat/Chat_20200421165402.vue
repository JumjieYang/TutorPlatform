<template>
    <div id="chat" class="chat"></div>
</template>

<script>
import $ from 'jquery';
export default {
    methods: { },
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
        background: black;
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