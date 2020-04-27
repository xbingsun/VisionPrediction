<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu></aside-menu>
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
                      <el-button type="text" @click="goVisual"  class="button">我有哪些验光信息？</el-button>
                    </el-col>
                    <el-col :span="6" :offset="4">
                      <img src="../image/ok.png" class="icon-img" />
                      <el-button type="text" @click="goInfo" class="button">我怎么查看我的个人信息？</el-button>
                    </el-col>
                  </el-row>
                  <br>
                  <el-row>
                    <el-col :span="6" :offset="4">
                      <img src="../image/trend.png" class="icon-img" />
                      <el-button type="text" @click="goPrediction" class="button">我未来度数的发展趋势是什么？</el-button>
                    </el-col>
                    <el-col :span="6" :offset="4">
                      <img src="../image/security.png" class="icon-img" />
                      <el-button type="text" @click="goSafe" class="button">我的信息安全吗？</el-button>
                    </el-col>
                  </el-row>
                  <br>
                  <el-row>
                    <el-col :span="6" :offset="4">
                      <img src="../image/advice.png" class="icon-img" />
                      <el-button type="text" @click="goAdvice" class="button">我能获得什么样的用眼建议？</el-button>
                    </el-col>
                    <el-col :span="6" :offset="4">
                      <img src="../image/question.png" class="icon-img" />
                      <el-button type="text" @click="goContact"  class="button">联系你们</el-button>
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
import AsideMenu from './common/AsideMenu'
import HeaderMenu from './common/HeaderMenu'
export default {
  data () {
    return {}
  },
  components: {
    AsideMenu,
    HeaderMenu
  },
  methods: {
    goVisual () {
      this.$router.push('/visualdata')
    },
    goInfo () {
      this.$router.push('/showuserinfo')
    },
    goPrediction () {
      this.$router.push('/visionprediction')
    },
    goSafe () {
      this.$alert('我们对用户的信息将进行严格的保密。', '承诺', {
        confirmButtonText: '确定'
      })
    },
    goAdvice () {
      this.$router.push('/visualadvice')
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
