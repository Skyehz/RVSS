<template>
<div class="view_container">
  <el-page-header @back="goBack" content="实时监控"></el-page-header>
  <el-card class="view_box"></el-card>
  <el-card class="view_box1"></el-card>
</div>
</template>

<script>
export default {
  created(){
   const loginForm=this.$route.query.loginForm;
   console.log(loginForm)
    },
 methods:{
   goBack() {
    this.$router.push("/menu");
      }
 }
}
</script>

<style lang="less" scoped>
.view_container{
  background-color: #cad6ca;
  height: 100%;
}
.view_box{
  width:60%;
  height:80%;
  background-color:#fff;
  border-radius: 3px;
  position: absolute;
  left:40%;
  top:55%;
  transform: translate(-50%,-50%);
}
.view_box1{
  width:20%;
  height:80%;
  background-color:#fff;
  border-radius: 3px;
  position: absolute;
  left:85%;
  top:55%;
  transform: translate(-50%,-50%);
}


</style>