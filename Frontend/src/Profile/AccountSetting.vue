<template>
    <div>
        <el-collapse v-model="activeNames" accordion>

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

            <el-collapse-item title="Change Profile Photo" name="4">
                <el-col :span="12">
                    <input type="file" @click="sendFile">
                    <el-upload
                        class="avatar-uploader"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        :show-file-list="false"
                        :http-request="sendFile"
                        :on-success="handleAvatarSuccess"
                        :before-upload="beforeAvatarUpload">
                        <img v-if="imageUrl" :src="imageUrl" class="avatar">
                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                </el-col>
                <el-col :span="12" style="text-align: left; margin-bottom:10px;">Slect a photo</el-col>
            </el-collapse-item>


            <el-collapse-item title="Role setting" name="5">
                <el-col :span="20" style="text-align: left; margin-bottom:10px;">Become a tutor</el-col>
                <el-col :span="4">
                    <el-switch
                        v-model="becomeTutor">
                    </el-switch>
                </el-col>
            </el-collapse-item>

            <el-collapse-item title="Log out" name="6">
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
                     <el-button size="mini" slot="reference">Yes</el-button>
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
            becomeTutor:this.$store.state.isTutor,
            activeNames: ['0'],
            imageUrl: '',
            file: null
        }
    },
    methods: {
        sendFile(){
            console.log(this.file)
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
                    image: this.file,
                },
                method: "PATCH",
            })
            .then((response) => {
                console.log(response.data);
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
            })
            .catch((error) => {
                console.log("file "+error);
                this.$message.error('Please try again.');
            })
        },
        handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
            this.file = file.raw
            //console.log(file.raw)

        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG) {
            this.$message.error('上传头像图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
            this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
        },
        logOut(){
            this.$store.dispatch('signOut')
        },
        submitInfo(){
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
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
            this.logOut()
            this.$router.push('/Login')
        },
        cancelDelete(){
            this.activeNames = ['0'];
        },
        deleteAccount(){
            this.logOut()
            this.$router.push('/Login')
        }
    },
    mounted(){
        
    },
    watch: {
        becomeTutor: function () {
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
                    isTutor: this.becomeTutor,
                },
                method: "PATCH",
            })
            .then((response) => {
                console.log(response.data);
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.$store.commit('setIsTutor', this.becomeTutor)
                this.activeNames = ['0'];
            })
            .catch((error) => {
                console.log("file "+error);
                this.$message.error('Please try again.');
            })
        }
    },
    
}
</script>

<style>
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
.avatar-uploader .el-upload:hover {
    border-color: #409EFF;
}
.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    line-height: 100px;
    text-align: center;
}
.avatar {
    width: 100px;
    height: 100px;
    display: block;
}
</style>