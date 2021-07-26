<template> 
    <el-container class="home_container">
     <!--头部-->
  <el-header>
            <div>
          <img src="" alt="">
          <span>RVSS 实时视频监控系统</span>
      </div>
        <h1>欢迎管理员</h1>
        <el-button type="info" @click="logout">返回</el-button>
      
</el-header>
     <!--页面主体-->
  <el-container>
      <!--侧边栏-->
    <el-aside width="70px">
     <el-menu background-color="#3b693b"   active-text-color="#fff"  router>
   <el-menu-item index="/admin_user" >
    <i class="el-icon-user"></i>
  </el-menu-item>
  <el-menu-item index="/admin_menu">
    <i class="el-icon-menu"></i>
  </el-menu-item>
  <el-menu-item index="/admin_view1" >
    <i class="el-icon-camera"></i>
  </el-menu-item>
  <el-menu-item index="/admin_view2" >
    <i class="el-icon-s-tools"></i>
  </el-menu-item>
  <el-menu-item index="/admin_message" >
    <i class="el-icon-document"></i>
  </el-menu-item>
  <el-menu-item index="/userlist">
    <i class="el-icon-s-custom"></i>
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
    created(){
        const loginForm=this.$route.query.loginForm;
    },
     data() {
      return {
        isCollapse: true
      };
    },
methods:{
    logout(){
        this.$router.push("/admin_menu");
    }
}
};
</script>

<style lang="less" scoped>
.home_container{
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
h1{
    font-size: 12px;
}
</style>