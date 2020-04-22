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
        height: 500px;
        width: 350px;
    }
</style>