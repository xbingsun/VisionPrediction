<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu></aside-menu>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>个人信息</span>
            </div>
            <div class="font">
              <el-row>
                <el-col :span="6" :offset="2">
                  <p>姓名：{{name}}</p>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="10" :offset="2">
                  <p>IP：{{ip}}</p>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="10" :offset="2">
                  <p>性别：{{sex}}</p>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="10" :offset="2">
                  <p>出生日期：{{Bir}}</p>
                </el-col>
              </el-row>
            </div>
          </el-card>
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
      ip: '',
      name: '',
      sex: '',
      Bir: ''
    }
  },
  components: {
    AsideMenu,
    HeaderMenu
  },
  mounted () {
    axios
      .get(
        this.$store.state.BASEURL +
          'user/get_user_info?' +
          'username=' +
          this.$store.state.username
      )
      .then(res => {
        this.ip = res.data[0]['S_OP_IP_Cus']
        this.name = res.data[0]['S_ME_CI_Nam']
        if (res.data[0]['S_ME_CI_Sex']) {
          this.sex = '女性'
        } else {
          this.sex = '男性'
        }
        this.Bir = res.data[0]['S_ME_CI_Bir'].slice(0, 10)
      })
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

.font {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 16px;
  color: #3f4e49;
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 800px;
  margin-left: 20px;
}

.el-card__header {
    padding: 18px 20px;
    border-bottom: 1px solid #EBEEF5;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    font-size: 25px;
}
</style>
