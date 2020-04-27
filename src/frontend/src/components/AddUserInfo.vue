<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu-doc></aside-menu-doc>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-divider content-position="left">新增用户信息</el-divider>
          <br />
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="用户IP" prop="IP">
              <el-col :span="5">
                <el-input v-model="form.ipCus"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="用户姓名">
              <el-col :span="5">
                <el-input v-model="form.name"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="检查日期">
              <el-date-picker v-model="form.checkdate" type="date" placeholder="检查日期" value-format="yyyy-MM-dd"></el-date-picker>
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
            <el-form-item label="左眼球镜">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.balL"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="右眼球镜">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.balR"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="左眼眼轴">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.axeL"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="右眼眼轴">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.axeR"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="左眼柱镜">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.posL"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="左眼柱镜">
              <el-col :span="5">
                <el-input type="number" v-model.number="form.posR"></el-input>
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
        checkdate: '',
        balL: '',
        balR: '',
        axeL: '',
        axeR: '',
        posL: '',
        posR: ''
      }
    }
  },
  methods: {
    resetForm () {
      this.form.ipCus = ''
      this.form.name = ''
      this.form.sex = 'male'
      this.form.bir = ''
      this.form.checkdate = ''
      this.form.balL = ''
      this.form.balR = ''
      this.form.axeL = ''
      this.form.axeR = ''
      this.form.posL = ''
      this.form.posR = ''
    },
    onSubmit () {
      const url = this.$store.state.BASEURL + 'user/add_user_info'
      axios.post(url, JSON.stringify(this.form)).then(
        res => {
          if (res.data === 'add userInfo successful') {
            this.$message('添加成功')
          } else {
            this.$message('添加失败')
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
