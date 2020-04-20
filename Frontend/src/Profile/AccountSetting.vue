<template>
    <div>
        <el-collapse v-model="activeNames" @change="handleChange" accordion>

            <el-collapse-item title="Reset password" name="1">
                <el-card class="box-card">
                    <el-form class="reset-password" style="margin-top:10px;">
                        <el-form-item>
                        <el-input
                            placeholder="Username"
                            v-model="username" 
                            type="text"
                        />
                        </el-form-item>

                        <el-tooltip placement="right" manual>
                        <el-form-item >
                            <el-input
                            placeholder="Password"
                            v-model="password"
                            />
                        </el-form-item>
                        </el-tooltip>
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:10px;"  @click="submitReset">submit</el-button>
                </el-card>
            </el-collapse-item>

            <el-collapse-item title="Email Setting" name="2">
                <el-card class="box-card">
                    <el-form class="reset-password" style="margin-top:30px;">
                        <el-form-item>
                        <el-input
                            placeholder="New email"
                            v-model="email" 
                            type="text"
                        />
                        </el-form-item>
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:30px;"  @click="submitEmail">submit</el-button>
                </el-card>
            </el-collapse-item>


            <el-collapse-item title="Role setting" name="3">
                <el-col :span="20" style="text-align: left; margin-bottom:10px;">Become a tutor</el-col>
                <el-col :span="4">
                    <el-switch
                        v-model="becomeTutor">
                    </el-switch>
                </el-col>
            </el-collapse-item>

            <el-collapse-item title="Delete Account" name="4">
                <el-col :span="20" style="text-align: left; margin-bottom:10px;">Are you sure?</el-col>
                <el-col :span="4">
                    <el-popconfirm
                        confirmButtonText='Yes'
                        cancelButtonText='No'
                        icon="el-icon-info"
                        iconColor="red"
                        title="Are you sure?"
                        @onCancel="cancelDelete"
                        @onConfirm="deleteAccount"
                    >
                     <el-button size="mini" slot="reference">删除</el-button>
                    </el-popconfirm>

                </el-col>
            </el-collapse-item>

            
        </el-collapse>
    </div>
</template>


<script>
export default {
     data() {
        return {
            username: '',
            password: '',
            email:'',
            becomeTutor:'',
            activeNames: ['0'],
        }
    },
    methods: {
        handleChange(val) {
            console.log(val);
        },
        submitEmail(){
            // const base = {
            //     baseURL: this.$store.state.endpoints.baseUrl,
            //     headers: {
            //         Authorization: this.$store.state.token,
            //         'Content-Type': 'application/json'
            //     },
            //     xhrFields: {
            //         withCredentials: true
            //     }
            // };
            // const axiosInstance = axios.create(base)
            // axiosInstance({
            //     url: "/user/",
            //     method: "get",
            //     params: {}
            // })
            // .then((response) => {
            //     this.$store.commit("setAuthUser",
            //         {authUser: response.data, isAuthenticated: true}
            //     )
            //     this.$router.push({name: 'Home'})
            // })
            // .catch((error) => {
            //     console.log(error);
            // })

            if(true){
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                this.email = '';
            }
            else{
                this.$message.error('Please try again.');
            }
        },
        submitReset(){
            // this.axios.get("http://localhost:8000/api-user/profile/{user}/").then((response) => {
            //     console.log(response.data)
            // })
            if(true){
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                this.username = '';
                this.password = '';
            }
            else{
                this.$message.error('Please try again.');
            }
        },
        cancelDelete(){
            this.activeNames = ['0'];
        },
        deleteAccount(){
            alert("See ya");
        }
    },
    watch: {
        becomeTutor: function () {
            if(true){
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
            }
            else{
                this.$message.error('Please try again.');
            }
        }
    },
    
}
</script>

<style>

</style>