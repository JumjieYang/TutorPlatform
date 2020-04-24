<template>
    <div>
        <el-card class="box-card">
            <el-form style="margin-top:10px;">

                <el-form-item >
                    <el-col :span="20" style="text-align: left; margin-bottom:10px;">Is this course available?</el-col>
                    <el-col :span="4">
                        <el-switch
                            v-model="isAvailable">
                        </el-switch>
                    </el-col>
                </el-form-item>

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
                    placeholder="Price for this course"
                    v-model="price"
                    />
                </el-form-item>

                <el-form-item >
                    <el-input
                    placeholder="Term"
                    v-model="term"
                    />
                </el-form-item>

                <el-form-item >
                    <el-input
                    placeholder="Course description"
                    v-model="description"
                    />
                </el-form-item>
            </el-form>
            <el-button class="reset-password" type="primary" style="width:50%; margin-bottom:10px;"  @click="submit">submit</el-button>
        </el-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
            update: '',
            courseName: '',
            number : '',
            term: '',
            description: '',
            price:'',
            subject:'',
            isAvailable:true,
            time_chosed:'',
            image: ''
        }
    },
    methods: {
        colseCollapseItem(){
        },
        submitCourse(){
            //this.getCoursePhoto()
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            //console.log(this.$store.state.userName);
            instance({
                url: '/api-course/course/',
                data: {
                    'subject': this.subject,
                    'number': this.number,
                    'term': this.term,
                    'description': this.description,
                    'isAvailable': this.isAvailable,
                    'price': this.price,
                    'image': this.image,
                    'tutor': userId,
                },
                method: "post",
            })
            .then((response) => {
                console.log(response.data);
                this.$message({
                    message: 'Posted sussessfully!',
                    type: 'success'
                });
                this.$emit("colseCollapseItem", ['2']);
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        },
        submit(){
            this.axios.get("https://api.unsplash.com/photos/random?query=canada&client_id=NgLD4aZRV1pErx3APaS_K9HnLj9QzIEebw3gmF6a2vc")
            .then((response) => {
                this.image = response.data.urls.regular
                //console.log(this.image)
                this.submitCourse()
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        }
    }
}
</script>