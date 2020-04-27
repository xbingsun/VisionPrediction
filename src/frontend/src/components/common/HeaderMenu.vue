<template>
  <div style="text-align: right; font-size: 12px">
    <el-dropdown>
      <i class="el-icon-setting" style="margin-right: 15px"></i>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item @click.native="goexit">退出</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <span class="logo-font">FOR EYE</span>
  </div>
</template>

<script>
export default {
  methods: {
    goexit () {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.logo-font {
  font-size: 16px;
  color: #4d6b61;
  font-weight: bold;
}
</style>
