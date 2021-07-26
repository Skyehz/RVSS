<template> 
    <el-container class="monitor_container">
     <!--头部-->
  <el-header>
            <div>
          <img src="" alt="">
          <span>RVSS 实时视频监控系统</span>
      </div>
        <el-button type="info" @click="returnMenu">返回</el-button>
      
</el-header>
     <!--页面主体-->
  <el-container>
      <!--侧边栏-->
    <el-aside width="70px">
    <el-menu background-color="#3b693b"   active-text-color="#fff" router>
   <el-menu-item index="/user" >
    <i class="el-icon-user"></i>
  </el-menu-item>
  <el-menu-item index="/menu">
    <i class="el-icon-menu"></i>
  </el-menu-item>
    <el-menu-item index="/view" >
    <i class="el-icon-camera"></i>
  </el-menu-item>
  <el-menu-item index="/message" >
    <i class="el-icon-document"></i>
  </el-menu-item>
 
</el-menu>

</el-aside>
    <!--右侧内容主体-->
    <el-main>
        <!--路由占位符-->
    <router-view></router-view>
        

    </el-main>
  </el-container>
</el-container>

</template>

<script>
export default{
     data() {
      return {
        isCollapse: true
      };
    },
methods:{
    returnMenu(){
        this.$router.push("/home");
    }
}
};
</script>

<style lang="less" scoped>
.monitor_container{
    height: 100%;
}
.el-header{
    background-color: #2b4b2b;
    display: flex;
    justify-content: space-between;
    padding-left:0px;
    align-items: center;
    color: #fff;
    font-size: 20px;
    >div{
        display: flex;
        align-items: center;
    }
}
.el-aside{
    background-color: #3b693b;
    .el-menu{
        border-right: none;
    }
}
.el-main{
    background-color: #cad6ca;
}
</style>