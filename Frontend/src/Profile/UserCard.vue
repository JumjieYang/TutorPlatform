<template>
<el-card style="margin-bottom:20px;">
    <div slot="header" class="clearfix">
    <span>About me</span>
    </div>

    <div class="user-profile">
    <div class="box-center">
        <div class="block"><el-avatar :src="this.image" :size="50" ></el-avatar></div>
    </div> 
    <div class="box-center">
        <div class="user-name text-center">{{this.info.firstName}} {{this.info.lastName}}</div>
    </div>
    </div>

    <div class="desciption">
        <div class="header">
            <i class="el-icon-school"></i>
            <span>Personal Info</span>
        </div>
        <div>
        <div class="text-muted">
            {{'Age: '+this.info.age}}
            <br>
            {{'Phone: '+this.info.phone}}
        </div>
        </div>
    </div>

</el-card>
</template>

<script>
export default {
    data() {
        return {
            image: '',
            info: ''
        }
    },
    mounted(){
        this.$store.watch(
            (state)=>{
                return this.$store.state.info
            },
            (newValue, oldValue)=>{
                this.info = newValue
        },)

        this.$store.watch(
            (state)=>{
                return this.$store.state.profileImage
            },
            (newValue, oldValue)=>{
                this.image = newValue
            },
        )
    }

}
</script>

<style scoped>

.desciption {
    margin-top: 20px;
    color: #606266;
}

.header{
    border-bottom: 1px solid #dfe6ec;
    padding-bottom: 10px;
    margin-bottom: 10px;
    font-weight: bold;
}
</style>


