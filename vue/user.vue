<template>
<div class=".information_container">
      <div class="information_box">
          <h1>用户信息</h1>
          <el-form ref="infFormRef" :model="infForm" :class="information_form" >
              <!--用户名-->
             <p> 用户名</p>
             <el-form-item prop="name">
             <el-row :gutter="10">
                    <el-col :span="17">
                     <el-input  prefix-icon="el-icon-user" v-model="infForm.username"></el-input>
                    </el-col>
                    <el-col :span="7">
                      <el-button type="primary" @click="changename">修改用户名</el-button>
                    </el-col>
                  </el-row>
             </el-form-item>
        <!--邮箱-->
            <p>注册邮箱</p>
             <el-form-item prop="email">
               <el-input  v-model="infForm.email" disabled></el-input>
            </el-form-item>
         <!--按钮-->
            <el-form-item prop="bnts" >
                <h1></h1>
               <el-button type="primary" @click= "dialogFormVisible = true">修改密码</el-button>
               <el-button type="primary">确认</el-button>
               <el-button type="info" @click="goBack">返回</el-button>
            </el-form-item>
          </el-form>
   
          <!--修改密码对话框-->
              <el-dialog el-dialog title="修改密码" :visible.sync= "dialogFormVisible" width="50%" append-to-body="true">
                    <el-input v-model="changepasswordForm.password" placeholder="">
                        <template slot="prepend">新密码</template>
                      </el-input>
                <el-row :gutter="10">
                    <h1></h1>
                    <el-col :span="17">
                      <el-input  v-model="infForm.email" placeholder="">
                        <template slot="prepend">注册邮箱</template>
                      </el-input>
                    </el-col>
                    
                    <el-col :span="7">
                      <el-button type="primary" @click="sendkey">发送验证码</el-button>
                    </el-col>
                 </el-row>
                 <h1></h1>
                    <el-input  v-model="changepasswordForm.key" placeholder="">
                        <template slot="prepend">验证码</template>
                    </el-input>
                 <h1></h1>
                 <span slot="footer" class="dialog-footer">
                  <el-button @click="dialogFormVisible = false">取 消</el-button>
                  <el-button type="primary" @click="changepassword">确 定</el-button>
                 </span>   
              </el-dialog>
      </div>
</div>
     
</template>

<script>
export default{
  mounted(){
    console.log("send");
       this.$axios.post('/message',this.message).then(res=>{
                  this.infForm=res.data;
                console.log(this.infForm);
         });
  },
  data() {  
    return {
       message:{
        msg:'get_information'
      },
      infForm:{
        username:'',
        email:''
      },
      changepasswordForm:{
        password:'',
        email:'',
        key:''
      },
      dialogFormVisible: false,
    };
  },
  methods:{
    changename(){
      this.$axios.post('/change_name',this.infForm).then(res=>{
        if(res.data.status===200) this.$message.success('修改成功')

      })
    },
    sendkey(){
      this.changepasswordForm.email=this.infForm.email;
      this.$axios.post('/reg_verify',this.changepasswordForm).then(res=>{
        this.$message.success('发送成功');
        console.log(res);
      })
    },
    changepassword(){
      this.$axios.post('/change_password',this.changepasswordForm).then(res=>{
          if(res.data.status===200) {
            this.$message.success('修改成功');
            dialogFormVisible = false
          }
          else this.$message.error('修改失败')
      } )
    },
    goBack(){
        this.$router.push("/menu");
    }
  }
}
</script>

<style lang="less" scoped>

.information_box{
  width:600px;
  height:100%;
  background-color:rgba(255, 255, 255, 0);
  border-radius: 3px;
  position:absolute;
  left:50%;
  top:80%;
  transform:translate(-50%,-50%);
}

 
.information_container{
    background-color:#cad6ca;
    height: 100%;
}

.information_form{
    position:absolute;
    bottom:20%;
    width:100%;
    padding: 0 20px;
    box-sizing: border-box;
}

.btns{
  display:flex;
  justify-content: center;
  position: relative;
  left:50px;

}

.dialog_box{
  height: 50vh;overflow: auto;
}

h1{
    font-size:20px ;
    position: relative;
    left: 250px;
}
</style>
