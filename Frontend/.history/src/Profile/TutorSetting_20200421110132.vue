<template>
    <div>
        <el-collapse v-model="activeNames" accordion>

            <el-collapse-item title="Post a course" name="1">
                <course @colseCollapseItem="update"></course>
            </el-collapse-item>

            <el-collapse-item title="My courses" name="2" >
                  <el-timeline >
                    <el-dialog title="Edit Course" :visible.sync="dialogVisible">
                        <span>{{subject}} {{number}}</span>
                        <el-form style="margin-top:10px;">
                            <el-form-item >
                            <el-col :span="20" style="text-align: left; margin-bottom:10px;">Is this course available?</el-col>
                            <el-col :span="4">
                                <el-switch
                                    v-model="isAvailable">
                                </el-switch>
                                </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Price</el-col>
                            <el-col :span="20">
                                <el-input v-model="price"/>
                            </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Term</el-col>
                            <el-col :span="20">
                                <el-input v-model="term"/>
                            </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Descript</el-col>
                            <el-col :span="20">
                                <el-input v-model="description"/>
                            </el-col>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button size="mini" @click="dialogVisible = false">取 消</el-button>
                            <el-button size="mini" type="primary" @click="dialogVisible = false">确 定</el-button>
                        </div>
                    </el-dialog>

                    <el-timeline-item v-for="course in courses"  v-bind:key="course.id" placement="top">
                    <el-card class="box-card" >
                        <div slot="header" class="clearfix">
                            <span>{{course.subject}} {{course.number}}</span>
                            <el-button @click="editCourse(course)" style="float: right; padding: 3px 0" type="text">Edit</el-button>
                        </div>
                        <p class="text item">
                            {{'Term: ' + course.term}}
                            <br>
                            {{'Price: ' + course.price}}
                            <br>
                            {{'Is available: ' + course.isAvailable}}
                            <br>
                            {{'Description: '+course.escription}}
                            <br><br>
                            <el-rate
                                v-model= course.rating
                                disabled
                                show-score
                                text-color="#ff9900"
                                score-template="{value}">
                            </el-rate>                            
                        </p>
                        </el-card>
                    </el-timeline-item>
                </el-timeline>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>


<script>
import Course from './Course'
export default {
    data() {
        return {
            course: null,
            number : '',
            term: '',
            description: '',
            price:'',
            subject:'',
            isAvailable:true,
            activeNames: ['0'],
            courses: '',
            dialogVisible: false
        }
    },
    methods: {
        editCourse(course){
            console.log(course.number)
            this.number = course.number,
            this.term = course.term,
            this.description = course.description,
            this.price = course.price,
            this.subject = course.subject,
            this.isAvailable = course.isAvailable,
            this.dialogVisible = !this.dialogVisible
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
        update(activeNames){
            this.activeNames = activeNames
        },
        updateCourse(){
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            console.log(this.$store.state.userName);
            instance({
                url: '/api-course/courses/',
                method: "get",
            })
            .then((response) => {
                this.courses = response.data
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        }
    },
    mounted(){
        updateCourse()
    },
    watch: {},
    components:{
        Course
    }
}
</script>

<style>

</style>