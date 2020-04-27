<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu-doc></aside-menu-doc>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-divider content-position="left">新建用户</el-divider>
          <br />
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="用户IP">
              <el-col :span="5">
                <el-input v-model="form.ipCus"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="用户姓名">
              <el-col :span="5">
                <el-input v-model="form.name"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="用户性别">
              <el-select v-model="form.sex" placeholder="请选择性别">
                <el-option label="男性" value="male"></el-option>
                <el-option label="女性" value="female"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="出生日期">
              <el-date-picker v-model="form.bir" type="date" placeholder="出生日期" value-format="yyyy-MM-dd"></el-date-picker>
            </el-form-item>
            <el-form-item label="密码">
              <el-col :span="5">
                <el-input placeholder="初始：123" v-model="form.pw" :disabled="true"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">立即创建</el-button>
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideMenuDoc from './common/AsideMenuDoc'
import HeaderMenu from './common/HeaderMenu'
const axios = require('axios')
export default {
  data () {
    return {
      form: {
        ipCus: '',
        name: '',
        sex: 'male',
        bir: '',
        pw: ''
      }
    }
  },
  methods: {
    resetForm () {
      this.form.ipCus = ''
      this.form.name = ''
      this.form.sex = 'male'
      this.form.bir = ''
      this.form.pw = ''
    },
    onSubmit () {
      const url = this.$store.state.BASEURL + 'user/add_user'
      axios.post(url, JSON.stringify(this.form)).then(
        res => {
          if (res.data === 'add user successful') {
            this.$message('添加用户成功')
          } else {
            this.$message('添加用户失败')
          }
        }
      )
    }
  },
  components: {
    AsideMenuDoc,
    HeaderMenu
  }
}
</script>

<style scoped>
.el-header {
  background-color: #96c7b754;
  color: #333;
  line-height: 60px;
}

.guide-font {
  font-size: 30px;
  color: #50a588;
  font-weight: 100px;
}

.icon-img {
  height: 80px;
}

.el-divider__text {
  position: absolute;
  background-color: #fff;
  padding: 0 20px;
  color: #385f38;
  font-size: x-large;
}
</style>
