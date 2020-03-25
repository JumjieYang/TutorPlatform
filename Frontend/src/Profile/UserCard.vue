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
        <div class="user-name text-center">Tester</div>
      </div>
    </div>

    <div class="desciption">
        <div class="header">
            <i class="el-icon-school"></i>
            <span>Desciption</span>
        </div>
        <div>
          <div class="text-muted">
              U1 Computer Science Student at McGill
          </div>
        </div>
    </div>

  </el-card>
</template>

<script>
export default {
  
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


