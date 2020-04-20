<template>
    <div>
        <el-collapse v-model="activeNames" @change="handleChange" accordion>

            <el-collapse-item title="Post a course" name="1">
                <el-card class="box-card">
                    <el-form style="margin-top:10px;">
                        <el-form-item>
                        <el-input
                            placeholder="Course subject"
                            v-model="subject" 
                            type="text"
                        />
                        </el-form-item>

                        <el-form-item >
                            <el-input
                            placeholder="Course number"
                            v-model="number"
                            />
                        </el-form-item>

                        <el-form-item >
                            <el-input
                            placeholder="Course description"
                            v-model="description"
                            />
                        </el-form-item>
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:10px;"  @click="submitPost">submit</el-button>
                </el-card>
            </el-collapse-item>

            <el-collapse-item title="Set price" name="2">
                <el-card class="box-card">
                    <el-form class="reset-password" style="margin-top:30px;">
                        <el-form-item>
                        <el-input
                            placeholder="What is your rate (per hour)?"
                            v-model="price" 
                            type="text"
                        />
                        </el-form-item>
                    </el-form>
                    <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:30px;"  @click="submitPrice">submit</el-button>
                </el-card>
            </el-collapse-item>


            <el-collapse-item title="set availability" name="3">
                <el-col :span="20" style="text-align: left; margin-bottom:10px;">Are you available to provide tutor services?</el-col>
                <el-col :span="4">
                    <el-switch
                        v-model="availability">
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
            courseName: '',
            number : '',
            description: '',
            price:'',
            availability:'',
            activeNames: ['0']
        }
    },
    methods: {
        handleChange(val) {
            console.log(val);
        },
        submitPost(){
            if(true){
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                this.courseName = '';
                this.number = '';
                this.description = '';
            }
            else{
                this.$message.error('Please try again.');
            }
        },
        submitPrice(){
            if(true){
                this.$message({
                    message: 'Sussess!',
                    type: 'success'
                });
                this.activeNames = ['0'];
                this.price = '';
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
        availability: function () {
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