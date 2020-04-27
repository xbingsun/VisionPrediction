<template>
<div class="aside">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu router :default-openeds="['1', '4']" :default-active="this.$route.path">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-s-home"></i>主页
        </template>
        <el-menu-item-group>
          <el-menu-item index="indexdoc">
            <i class="el-icon-s-home"></i>home
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-s-custom"></i>个人中心
        </template>
        <el-menu-item-group>
          <el-menu-item index="modifydocpass">
            <i class="el-icon-edit"></i>修改密码
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-view"></i>用户信息
        </template>
        <el-menu-item-group>
          <el-menu-item index="newuser">
            <i class="el-icon-document"></i>注册用户
          </el-menu-item>
          <el-menu-item index="adduserinfo">
            <i class="el-icon-top-right"></i>新增验光信息
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </el-aside>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.el-aside {
  color: #333;
}

.aside /deep/ .el-menu-item-group__title {
  padding: 0;
}
</style>
