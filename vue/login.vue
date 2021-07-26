<template>
    <div class="login_container">
        <div id="Ring3"></div>
        <div id="Ring2"></div>
        <div id="Ring1"></div>
        <div class="logo_box">
            <h1>RVSS</h1>
            <h2>实时视频监测系统</h2>
        </div>
        <div class="login_box">
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
            </div>
            <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
                <!--选择权限-->
                <el-form-item class="rds" @change="changeType">
                     <el-radio v-model="loginForm.type" label="admin" @change="changeType">管理员</el-radio>
                     <el-radio v-model="loginForm.type" label="user" @change="changeType">普通用户</el-radio>
                </el-form-item>
                <!--用户名-->
                <p> 请输入邮箱</p>
                <el-form-item prop="email">
                    <el-input v-model="loginForm.email" prefix-icon="el-icon-user"></el-input>
                </el-form-item>
                <!--密码-->
                <p> 请输入密码</p>
                <el-form-item  prop="password">
                    <el-input v-model="loginForm.password" prefix-icon="el-icon-key" type="password"></el-input>
                </el-form-item>
                 <!--注册-->
                <el-link type="danger" :underline="true" @click="register">点此注册</el-link>
                 <!--按钮-->
                <el-form-item class="btns">
                      <el-button type="primary"  :round="true" @click="login">登录</el-button>
                      <el-button type="info" :round="true" @click="resetLoginForm">重置</el-button>
                </el-form-item>
               
            </el-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default{
   data(){
       return{
          //登陆表单数据绑定对象
          loginForm:{
              email:'czh15296700133@163.com',
              password:'123456',
              type:'admin',
          } ,
          //登陆表单验证登陆对象
          loginFormRules:{
              email:[
                  { required: true, message: '请输入邮箱', trigger: 'blur' },
                  { min: 5, max: 30, message: '长度在 3 到 10 个字符', trigger: 'blur' }
                  ], 
              password:[
                   { required: true, message: '请输入登录密码', trigger: 'blur' },
                   { min: 4, max: 30, message: '长度在 6 到 15 个字符', trigger: 'blur' }
                   ] 

          },
       };
   },
   methods:{
       //点击重置按钮重置表单
       resetLoginForm(){
          // console.log(this);
          this.$refs.loginFormRef.resetFields();
       },
        login(){
          this.$refs.loginFormRef.validate(valid=>{
              if(!valid)return this.$message.error('登陆失败');
              const{ res:data }=this.loginForm;
             //登录请求
              this.$axios.post('/login',this.loginForm).then(
                  res=>{
                      
                      console.log(res);
                      const token=res.data.token;
                      console.log(token);
                      window.sessionStorage.setItem("token",token);
                      if(res.data.status===200){
                           this.$message.success('登录成功');
                       if(this.loginForm.type==='user')
           this.$router.push({
               path: "/home",
               query:{loginForm: this.loginForm}
           });
           if(this.loginForm.type==='admin')this.$router.push({
               path: "/admin_home",
               query:{loginForm: this.loginForm}
           });
                }  else{
               return this.$message.error('登陆失败');
           }

                  })
          });
        
       },
       register(){
           this.$router.push('/register');       },
        changeType(){
            console.log(this.loginForm.type);
        }
   }
};
</script>

<style lang="less" scoped>
.login_container{
    background-color: #2b4b2b;
    height:100%;
}

.login_box{
    width: 450px;
    height: 600px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 70%;
    top: 50%;
    transform: translate(-50%,-50%);

    .avatar_box{
        height: 130px;
        width:130px;
        border:1px solid #eee;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 0 10px #ddd;
        position: absolute;
        left: 50%;
        transform: translate(-50%,-50%);
        img{
             width: 100%;
            height: 100%;
            border-radius: 50%;
            background-color: #eee;
        }
    }
}
.login_form{
    position:absolute;
    bottom:20%;
    width: 100%;
    padding:0 20px;
    box-sizing: border-box;

}

.btns{
    position: relative;
    top: 50px;
    display: flex;
    justify-content: center;

}

.rds{
    display: flex;
    justify-content: center;
}

.logo_box{
    width: 400px;
    height: 300px;
    border-radius: 3px;
    position: absolute;
    left: 20%;
    top: 30%;
    transform: translate(-50%,-50%);
    h1{
        color: #fff;
        font: 10em Lucida Console;
        font-style:italic;
        text-shadow: 0 1px 0 #ccc,
        0 2px 0 #c9c9c9,
        0 3px 0 #bbb,
        0 4px 0 #b9b9b9,
        0 5px 0 #aaa,
        0 6px 1px rgba(0,0,0,.1),
        0 0 5px rgba(0,0,0,.1),
        0 1px 3px rgba(0,0,0,.3),
        0 3px 5px rgba(0,0,0,.2),
        0 5px 10px rgba(0,0,0,.25),
        0 10px 10px rgba(0,0,0,.2),
        0 20px 20px rgba(0,0,0,.15);
    }
    h2{
        position: relative;
        left: 70px;
        color: #fff;
        font: 3em Lucida Console;
        font-style:italic;
        text-shadow: 0 1px 0 #ccc,
        0 2px 0 #c9c9c9,
        0 3px 0 #bbb,
        0 4px 0 #b9b9b9,
        0 5px 0 #aaa,
        0 6px 1px rgba(0,0,0,.1),
        0 0 5px rgba(0,0,0,.1),
        0 1px 3px rgba(0,0,0,.3),
        0 3px 5px rgba(0,0,0,.2),
        0 5px 10px rgba(0,0,0,.25),
        0 10px 10px rgba(0,0,0,.2),
        0 20px 20px rgba(0,0,0,.15);

    }
    
}

#Ring1 {
    position:absolute;
    top:90%;
    left: 10%;
    transform: translate(-50%,-50%);
    width: 800px;
    height: 800px;
    float: left;
    border-radius: 640px;
    border:50px #ffffff96 solid;
   }


#Ring2 {
    position:absolute;
    top:90%;
    left: 10%;
    transform: translate(-50%,-50%);
    width: 600px;
    height: 600px;
    float: left;
    border-radius: 480px;
    border:50px #ffffff96 solid;
   }

#Ring3 {
    position:absolute;
    top:90%;
    left: 10%;
    transform: translate(-50%,-50%);
    width: 400px;
    height: 400px;
    float: left;
    border-radius: 320px;
    border:50px #ffffff96 solid;
   }


</style>