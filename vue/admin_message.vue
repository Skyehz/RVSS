<template>
<div>
   <el-page-header @back="goBack" content="入侵记录">
</el-page-header>
<!--卡片视图-->
<el-card>
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
      prop="time"
      label="入侵时间"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="入侵地点"
      width="300">
    </el-table-column>
    <el-table-column
      prop="mess"
      label="备注">
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <!--编辑按钮-->
        <el-tooltip effect="dark" content="编辑备注" placement="top">
        <el-button type="primary" icon="el-icon-edit" size="mini"></el-button>
        </el-tooltip>
        <!--删除按钮-->
        <el-tooltip effect="dark" content="删除" placement="top">
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
</div>
</template>

<script>
export default{
data() {
      return {
        tableData: [{
          time: '2021-7-23 21:07:00',
          address: '上海市普陀区金沙江路 1518 弄',
          mess:'无'
        }, {
          time: '2021-7-23 21:07:02',
          address: '上海市普陀区金沙江路 1519 弄',
          mess:'无'
        }, {
          time: '2021-7-23 21:07:33',
          address: '上海市普陀区金沙江路 1510 弄',
          mess:'车辆'
        }, {
          time: '2021-7-23 21:07:78',
          address: '上海市普陀区金沙江路 1524 弄',
          mess:'无'
        }]
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