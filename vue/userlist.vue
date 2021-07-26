<template>
<div>
   <el-page-header @back="goBack" content="用户信息">
</el-page-header>
<!--卡片视图-->
<el-card>
    <el-button type="primary" @click= "dialogFormVisible = true" >添加用户</el-button>
    <p></p>
<el-table
    :data="tableData"
    stripe
    style="width: 100% height：100%"
    border>
    <el-table-column
      type="index"
      width="80">
    </el-table-column>
    <el-table-column
      prop="username"
      label="用户名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="email"
      label="注册邮箱"
      width="300">
    </el-table-column>
    <el-table-column
      prop="passord"
      label="密码">
    </el-table-column>
     <el-table-column
      prop="type"
      label="身份类型">
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <!--编辑按钮-->
        <el-tooltip effect="dark" content="修改信息" placement="top">
        <el-button type="primary" icon="el-icon-edit" size="mini"></el-button>
        </el-tooltip>
        <!--删除按钮-->
        <el-tooltip effect="dark" content="删除用户" placement="top">
        <el-button type="danger" icon="el-icon-delete" size="mini"></el-button>
        </el-tooltip>
      </template>
    </el-table-column>
  </el-table>
 <!--分页区域-->
  <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage4"
      :page-sizes="[1, 2, 5, 10]"
      :page-size="10"
      layout="total, sizes, prev, pager, next, jumper"
      :total="4">
    </el-pagination>
</el-card>
 <el-dialog el-dialog title="添加用户" :visible.sync= "dialogFormVisible" width="50%" append-to-body="true">
                    <el-input placeholder="">
                        <template slot="prepend">用户名</template>
                      </el-input>
                    <h1></h1>
                      <el-input placeholder="">
                        <template slot="prepend">密码</template>
                      </el-input>
                 <h1></h1>
                    <el-input placeholder="">
                        <template slot="prepend">注册邮箱</template>
                    </el-input>
                 <h1></h1>
                <div style="margin-top: 20px">
                   <el-radio-group v-model="radio" size="mini">
                      <el-radio label="1" border>管理员</el-radio>
                      <el-radio label="2" border>普通用户</el-radio>
                  </el-radio-group>
                </div>
                 <span slot="footer" class="dialog-footer">
                  <el-button @click="dialogFormVisible = false">取 消</el-button>
                  <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                 </span>   

              </el-dialog>
</div>
</template>

<script>
export default{
data() {
      return {
        tableData: [{
          username:'张林',
          email:'12345678@qq.com',
          password:'123456',
          type:'普通用户'
        }, {
          username:'畅紫涵',
          email:'123458828@qq.com',
          password:'1djhjj',
          type:'管理员'
        },{
          username:'张馨予',
          email:'1234537738@qq.com',
          password:'12akksl6',
          type:'普通用户'
        },{
          username:'李欣宇',
          email:'126718288@qq.com',
          password:'12ddjk',
          type:'普通用户'
        },],
        radio:'1',
        dialogFormVisible: false,
      }
    },
methods:{
    goBack() {
         this.$router.push("/admin_menu");
      }
}
}
</script>


<style lang="less" scoped>

</style>
</template>