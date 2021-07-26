<template>
<div class="view_container">
 <el-page-header @back="goBack" content="设置入侵区域"></el-page-header>
  <el-card class="view_box"></el-card>
</div>
</template>

<script>
export default {
    methods:{
    goBack() {
         this.$router.push("/admin_menu");
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
  width:80%;
  height:80%;
  background-color:#fff;
  border-radius: 3px;
  position: absolute;
  left:50%;
  top:55%;
  transform: translate(-50%,-50%);
}



</style>