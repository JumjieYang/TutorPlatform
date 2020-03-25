<template>
    <div>
        <el-table 
            style="width: 100%"
            :data="tableData">
            <el-table-column
                label="Setting"
                prop="name">
            </el-table-column>
            <el-table-column align="right">
                <template>
                    <el-button
                    size="mini">Edit</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>


<script>
export default {
     data() {
      return {
        tableData: [{
          name: 'Password',
        }, {
          name: 'Email Setting',
        }, {
          name: 'Become A Tutor',
        }, {
          name: 'Whatever'
        }]
      }
    }
}
</script>