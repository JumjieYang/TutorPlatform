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
        /* margin-right: 25px;
        margin-top: 0%; */
        width: 350px;
        box-shadow: 0 0px 27px 1.5px rgba(0,0,0,0.2);
    }
</style>