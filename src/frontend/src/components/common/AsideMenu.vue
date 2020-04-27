<template>
<div class="aside">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu router :default-openeds="['1', '4']" :default-active="this.$route.path">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-s-home"></i>主页
        </template>
        <el-menu-item-group>
          <el-menu-item index="index">
            <i class="el-icon-s-home"></i>home
          </el-menu-item>
          <el-menu-item index="index">
            <i class="el-icon-s-promotion"></i>快速导航
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-s-custom"></i>个人中心
        </template>
        <el-menu-item-group>
          <el-menu-item index="showuserinfo">
            <i class="el-icon-user"></i>个人信息
          </el-menu-item>
          <el-menu-item index="modifyuserpass">
            <i class="el-icon-edit"></i>修改信息
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-view"></i>视力情况
        </template>
        <el-menu-item-group>
          <el-menu-item index="visualdata">
            <i class="el-icon-document"></i>验光情况
          </el-menu-item>
          <el-menu-item index="visionprediction">
            <i class="el-icon-top-right"></i>视力预测
          </el-menu-item>
          <el-menu-item index="visualadvice">
            <i class="el-icon-star-on"></i>用眼建议
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title">
          <i class="el-icon-s-data"></i>统计信息
        </template>
        <el-menu-item-group>
          <el-menu-item index="statisticsinfo">
            <i class="el-icon-search"></i>统计信息
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </el-aside>
  </div>
</template>

<script>
export default {
  methods: {
    goContact () {
      this.$alert('759677946@qq.com', '联系方式', {
        confirmButtonText: '确定'
      })
    }
  }
}
</script>

<style scoped>
.el-aside {
  color: #333;
}

.aside /deep/ .el-menu-item-group__title {
  padding: 0;
}
</style>
