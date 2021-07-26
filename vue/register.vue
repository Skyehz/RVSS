<template> 
    <div class="reg_container">
         <div class="reg_box">
             <h1>注册</h1>
            <el-form ref="regFormRef" :model="regForm" :rules="regFormRules" label-width="0px" class="reg_form">
                <!--选择权限-->
                <el-form-item class="rds" @change="changeType">
                     <el-radio v-model="regForm.type" label="admin" @change="changeType">管理员</el-radio>
                     <el-radio v-model="regForm.type" label="user" @change="changeType">普通用户</el-radio>
                </el-form-item>
                <!--用户名-->
                <p> 请输入用户名</p>
                <el-form-item prop="username">
                    <el-input v-model="regForm.username" prefix-icon="el-icon-user"></el-input>
                </el-form-item>
                <!--密码-->
                <p> 请输入密码</p>
                <el-form-item  prop="password">
                    <el-input v-model="regForm.password" prefix-icon="el-icon-key" type="password"></el-input>
                </el-form-item>
                 <!--邮箱-->
                 <p> 请输入验证邮箱</p>
                <el-form-item  prop="email" >
                     <el-input placeholder="请输入内容" v-model="regForm.email">
                     <el-button slot="append" @click="sendkey">发送验证码</el-button>
                     </el-input>
                     
                     
                </el-form-item>
                <!--验证码-->
                <p> 请输入验证码</p>
                <el-form-item  prop="key">
                    <el-input v-model="regForm.key" type="验证码"></el-input>
                </el-form-item>
                 <!--按钮-->
                <el-form-item class="btns">
                      <el-button type="primary" :round="true" @click="register">注册</el-button>
                      <el-button type="info" :round="true" @click="resetLoginForm">重置</el-button>
                      <el-button type="info" :round="true" @click="regReturn">返回</el-button>
                </el-form-item>
               
            </el-form>
        </div>
        
    </div>
</template>

<script>
export default {
 data(){
       return{
          //注册表单数据绑定对象
          regForm:{
              username:'',
              password:'',
              email:'',
              key:'',
              type:'admin'
          } ,
          //注册表单验证登陆对象
          regFormRules:{
              username:[
                  { required: true, message: '请输入用户名', trigger: 'blur' },
                  { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
                  ], 
              password:[
                   { required: true, message: '请输入登录密码', trigger: 'blur' },
                   { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
                   ] ,
             email:[
                   { required: true, message: '请输入邮箱', trigger: 'blur' },
                   { min: 0, max: 30, message: '请输入正确的邮箱', trigger: 'blur' }
                   ] ,
             key:[
                   { required: true, message: '请输入验证码', trigger: 'blur' },
                   { min: 0, max: 6, message: '请输入正确的验证码', trigger: 'blur' }
                   ] 

          },
          radio:'admin'
       };
   },
   methods:{
       sendkey(){
        if(this.regForm.email){
         this.$message.success('发送成功');
          this.$axios.post('/reg_verify',this.regForm).then(res=>{
                     const key=res.data.key;
                     console.log(key);
          })     }
          else this.$message.error('发送失败');
           
       },
       //注册
       register(){
             this.$refs.regFormRef.validate(valid=>{
              if(!valid)return this.$message.error('注册失败');
             //注册请求
              this.$axios.post('/register',this.regForm).then(
                  res=>{
                      console.log(res.data.status);
                      if(res.data.status===200){
                           this.$message.success('注册成功');
                           this.$router.push('/login');
                      }
                     else
                           this.$message.error('注册失败');
                  })
          });

       },
       //点击重置按钮重置表单
       resetLoginForm(){
          // console.log(this);
          this.$refs.regFormRef.resetFields();
       },
       regReturn(){
           this.$router.push("/login");
       },
        changeType(){
            console.log(this.regForm.type);
        }
}
}
</script>

<style lang="less" scoped>
.reg_container{
    background-color: #2b4b2b;
    height:100%;
}

.reg_box{
    width: 800px;
    height: 600px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}

.reg_form{
    position:absolute;
    bottom:0%;
    width: 100%;
    padding:0 40px;
    box-sizing: border-box;
}


.btns{
    display: flex;
    justify-content: center;

}

.rds{
    display: flex;
    justify-content: center;
}

h1{
    position: relative;
    left: 380px;
}
</style>