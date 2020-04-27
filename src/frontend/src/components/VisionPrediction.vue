<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu></aside-menu>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-col :span=12>
            <div id="myLeftDegree" :style="{width: '500px', height: '500px'}"></div>
          <div id="myRightDegree" :style="{width: '500px', height: '500px'}"></div>
          </el-col>
          <el-col :span=12>
            <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>说明</span>
            </div>
            <div class="text item">暂时只支持为验光次（年）数大于等于3次并且小于等于6次的用户进行视力预测。
              为确保预测的准确性，至少需要基于3年的数据。预测的数据分为三种：3to4、4to5、5to6。用户可根据实际验光数据进行判断。
              <br>
              等效度数计算公式：等效度数 = 球镜度数 + 1/2柱镜度数
            </div>
          </el-card>
          </el-col>
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
      optionLeftLine: {
        title: {
          text: '左眼'
        },
        tooltip: {},
        legend: {
          data: ['等效度数']
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: []
      },
      optionRightLine: {
        title: {
          text: '右眼'
        },
        tooltip: {},
        legend: {
          data: ['等效度数']
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: []
      },
      eqDegreeL: {
        name: '等效度数',
        type: 'line', // 设置图表主题
        data: []
      },
      eqDegreeR: {
        name: '等效度数',
        type: 'line', // 设置图表主题
        data: []
      }
    }
  },
  methods: {
    setData (data) {
      var t = 0
      for (var i = 0; i < data.length; i++) {
        if (i % 2 !== 0) {
          var times = '第' + (t + 1) + '年'
          t = t + 1
          this.optionLeftLine['xAxis']['data'].push(times)
          this.optionRightLine['xAxis']['data'].push(times)
        }
        if (i % 2 !== 0) {
          this.eqDegreeL['data'].push(data[i])
        }
        if (i !== 0 && i % 2 === 0) {
          this.eqDegreeR['data'].push(data[i])
        }
      }
    },
    draw () {
      // 基于准备好的dom,初始化echarts实例
      let chartLeftDegreeline = this.$echarts.init(
        document.getElementById('myLeftDegree')
      )
      let chartRightDegreeline = this.$echarts.init(
        document.getElementById('myRightDegree')
      )
      // 绘制图表
      chartLeftDegreeline.setOption(this.optionLeftLine, true)
      chartRightDegreeline.setOption(this.optionRightLine, true)
    }
  },
  mounted () {
    axios
      .get(
        this.$store.state.BASEURL +
          'user/get_prediction?' +
          'username=' +
          this.$store.state.username
      )
      .then(res => {
        this.setData(res.data)
        this.optionLeftLine['series'].push(this.eqDegreeL)
        this.optionRightLine['series'].push(this.eqDegreeR)
        this.draw()
      })
  },
  components: {
    AsideMenu,
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
.text {
  font-size: 14px;
}

.item {
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
  width: 480px;
}
</style>
