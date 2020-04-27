<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu-doc></aside-menu-doc>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-row>
            <el-col :span="22" :offset="1">
              <el-card :body-style="{ padding: '0px' }">
                <div style="padding: 14px;">
                  <span class="guide-font">快速导航</span>
                  <el-divider></el-divider>
                  <el-row>
                    <el-col :span="6" :offset="4">
                      <img src="../image/log.png" class="icon-img" />
                      <el-button type="text" class="button" @click="goNewUser">新建用户</el-button>
                    </el-col>
                    <el-col :span="6" :offset="4">
                      <img src="../image/ok.png" class="icon-img" />
                      <el-button type="text" class="button" @click="goAddUserInfo">添加验光信息</el-button>
                    </el-col>
                  </el-row>
                  <br>
                  <el-row>
                    <el-col :span="6" :offset="4">
                      <img src="../image/advice.png" class="icon-img" />
                      <el-button type="text" class="button" @click="goModify">修改信息</el-button>
                    </el-col>
                    <el-col :span="6" :offset="4">
                      <img src="../image/question.png" class="icon-img" />
                      <el-button type="text" class="button" @click="goContact">联系我们</el-button>
                    </el-col>
                  </el-row>
                  <br>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideMenuDoc from './common/AsideMenuDoc'
import HeaderMenu from './common/HeaderMenu'
export default {
  data () {
    return {}
  },
  components: {
    AsideMenuDoc,
    HeaderMenu
  },
  methods: {
    goNewUser () {
      this.$router.push('/newuser')
    },
    goAddUserInfo () {
      this.$router.push('/adduserinfo')
    },
    goModify () {
      this.$router.push('/modifydocpass')
    },
    goContact () {
      this.$alert('759677946@qq.com', '联系方式', {
        confirmButtonText: '确定'
      })
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

.guide-font {
  font-size: 30px;
  color: #50a588;
  font-weight: 100px;
}

.icon-img {
  height: 80px;
}
</style>
