<template>
<el-form >
<el-form-item>
       <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item v-for="item in 6" :key="item">
      <h3 class="medium">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</el-form-item>
<el-form-item>
<el-row :gutter="10">
  <el-col :span="6" offset="4">
    <el-card :body-style="{ padding: '0px' }">
      <el-button type="text" class="button" @click="IntoView">查看监控></el-button>
      <img src="../assets/logo.png" class="image">
      </el-card>
 </el-col>
    <el-col :span="6" offset="2">
    <el-card :body-style="{ padding: '0px' }">
      <el-button type="text" class="button" @click="IntoMess">查看入侵记录></el-button>
      <img src="../assets/logo.png" class="image">
      </el-card>
 </el-col>
 
</el-row>
</el-form-item>
</el-form>

</template>

<script>
export default {
data() {
    return {
      currentDate: new Date()
    };
  },
   methods:{
     IntoView(){
           this.$router.push('/monitor');      
            },
     IntoMess(){
           this.$router.push('/message');      
            }
      }
}
</script>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .card_gps{
    height: 300px;
    width: 600px;
    display: flex;
  }
  

</style>

