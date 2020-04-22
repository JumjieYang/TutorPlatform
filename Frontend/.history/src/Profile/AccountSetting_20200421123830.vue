<template>
    <div>
        <el-collapse v-model="activeNames" @change="handleChange" accordion>

            <el-collapse-item title="Edit info" name="1">
                <el-card class="box-card">
                    <el-form class="reset-password" style="margin-top:10px;">
                        <el-form-item>
                        <el-input
                            placeholder="First Name"
                            v-model="firstName" 
                            type="text"
                        />
                        </el-form-item>
                        <el-form-item>
                        <el-input
                            placeholder="Last Name"
                            v-model="lastName" 
                            type="text"
                        />
                        </el-form-item><el-form-item>
                        <el-input
                            placeholder="Phone Number"
                            v-model="phoneNumber" 
                            type="text"
                        />
                        </el-form-item><el-form-item>
                        <el-input
                            placeholder="Age"
                            v-model="age" 
                            type="text"
                        />
                        </el-form-item>
                        <!--photo 
                            <el-form-item >
                            <el-input
                            placeholder="Password"
                            v-model="password"
                            />
                        </el-form-item> -->
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:10px;"  @click="submitInfo">submit</el-button>
                </el-card>
            </el-collapse-item>

            <el-collapse-item title="Reset password" name="2">
                <el-card class="box-card">
                    <el-form class="reset-password" style="margin-top:10px;">
                        <el-form-item >
                            <el-input
                            placeholder="New Password"
                            v-model="password"
                            />
                        </el-form-item>
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:10px;"  @click="submitReset">submit</el-button>
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
            password: '',
            email:'',
            firstName: '',
            lastName: '',
            phoneNumber: '',
            age:'',
            becomeTutor:'',
            activeNames: ['0'],
        }
    },
    methods: {
        handleChange(val) {
            //console.log(val);
        },
        submitInfo(){
            // this.axios.get("http://localhost:8000/api-user/profile/4",{
            //     headers: { 'Authorization' : 'Token '+'2b25b6b3b6231f1905206c1b62d436194b826546'}
            //     })

            //instance.defaults.headers.common['Authorization'] = this.$store.state.token;
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'

            },
            });
            instance({
                url: '/api-user/profile/' + userId + '/',
                data: {
                    user: ""+userId,
                    firstName: this.firstName,
                    lastName: this.lastName,
                    age: this.age,
                    phoneNumber: this.phoneNumber
                },
                method: "put",
            })
            .then((response) => {
                console.log(response.data);
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                this.firstName = ''
                this.lastName = ''
                this.age = ''
                this.phoneNumber = ''
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        },
        submitReset(){
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            console.log(this.$store.state.userName);
            instance({
                url: '/api-user/users/' + userId ,
                data: {
                    username: this.$store.state.userName,
                    password: this.password
                },
                method: "put",
            })
            .then((response) => {
                console.log(response.data);
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                //this.$store.commit('retrieveToken', null) //TODO
                this.$router.push('/Login')
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        },
        cancelDelete(){
            this.activeNames = ['0'];
        },
        deleteAccount(){
            alert("See ya");
        }
    },
    mounted(){
        //initialize personal data 
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