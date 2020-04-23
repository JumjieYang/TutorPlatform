<template>
<el-card style="margin-bottom:20px;">
    <div slot="header" class="clearfix">
    <span>About me</span>
    </div>

    <div class="user-profile">
    <div class="box-center">
        <div class="block"><el-avatar :size="50" ></el-avatar></div>
    </div> 
    <div class="box-center">
        <div class="user-name text-center">{{this.name}}</div>
    </div>
    </div>

    <div class="desciption">
        <div class="header">
            <i class="el-icon-school"></i>
            <span>Personal Info</span>
        </div>
        <div>
        <div class="text-muted">
            {{'Age: '+this.age}}
            <br>
            {{'Phone: '+this.phoneNumber}}
        </div>
        </div>
    </div>

</el-card>
</template>

<script>
export default {
    data() {
        return {
            username: this.$store.state.userName,
            name: '',
            age:'',
            phoneNumber:''
        }
    },
    mounted(){
    this.axios.get('/api-user/profile/'+this.$store.state.userId+'/',{
        headers: { 'Authorization' : 'Token '+ this.$store.state.token}
    })
    .then((response) => {
        //console.log(response.data)
        this.name = response.data.firstName+' '+response.data.lastName
        this.age = response.data.age
        this.phoneNumber = response.data.phoneNumber
        this.$store.commit('setIsTutor',response.data.isTutor)
    })
    .catch((error) => {
        console.log(error);
        this.$message.error('Please try again.');
    })
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


