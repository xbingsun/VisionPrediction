<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu></aside-menu>
      <el-container>
        <el-header >
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-divider content-position="left">修改密码</el-divider>
          <br />
          <el-form ref="form" :model="form" label-width="130px">
            <el-form-item label="旧密码">
              <el-col :span="5">
                <el-input type="password" v-model="form.oldpass"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="新密码">
              <el-col :span="5">
                <el-input type="password" v-model="form.newpass"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="请再次输入新密码">
              <el-col :span="5">
                <el-input type="password" v-model="form.newpasssec"></el-input>
              </el-col>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="onSubmit">立即修改</el-button>
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideMenu from './common/AsideMenu'
import HeaderMenu from './common/HeaderMenu'
const axios = require('axios')
export default {
  data () {
    return {
      form: {
        oldpass: '',
        newpass: '',
        newpasssec: '',
        username: ''
      }
    }
  },
  components: {
    AsideMenu,
    HeaderMenu
  },
  methods: {
    resetForm () {
      this.form.oldpass = ''
      this.form.newpass = ''
      this.form.newpasssec = ''
      this.form.username = ''
    },
    onSubmit () {
      if (this.form.newpass !== this.form.newpasssec) {
        this.$message('两次密码输入不一致')
        this.resetForm()
      } else {
        this.form.username = this.$store.state.username
        const url = this.$store.state.BASEURL + 'user/modify_user_pass'
        axios.post(url, JSON.stringify(this.form)).then(
          res => {
            if (res.data === 'Wrong Password') {
              this.$message('原密码输入错误')
            } else if (res.data === 'User not Found') {
              this.$message('用户不存在')
            } else if (res.data === 'Modify failed') {
              this.$message('修改失败')
            } else if (res.data === 'Modify successful') {
              this.$message('修改成功')
            }
            this.resetForm()
          }
        )
      }
    }
  }
}
</script>

<style scoped>
.el-header {
  background-color: #96c7b754;
  color: #333;
  line-height: 60px;
}

.el-divider__text {
  position: absolute;
  background-color: #fff;
  padding: 0 20px;
  color: #385f38;
  font-size: x-large;
}
</style>
