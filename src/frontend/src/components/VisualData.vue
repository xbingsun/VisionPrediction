<template>
  <div class="index">
    <el-container style="height: 100%; border: 1px solid #eee">
      <aside-menu></aside-menu>
      <el-container>
        <el-header>
          <header-menu></header-menu>
        </el-header>
        <el-main>
          <el-checkbox
            :indeterminate="isIndeterminate"
            v-model="checkAll"
            @change="handleCheckAllChange"
          >全选</el-checkbox>
          <div style="margin: 15px 0;"></div>
          <el-checkbox-group v-model="checkedInfo" @change="handleCheckedInfoChange">
            <el-checkbox v-for="oneinfo in Info" :label="oneinfo" :key="oneinfo">{{oneinfo}}</el-checkbox>
            <el-button @click="onsubmit" size="medium">确认</el-button>
          </el-checkbox-group>
          <div id="myLeftDegree" :style="{width: '500px', height: '500px'}"></div>
          <div id="myRightDegree" :style="{width: '500px', height: '500px'}"></div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideMenu from './common/AsideMenu'
import HeaderMenu from './common/HeaderMenu'
const axios = require('axios')
const infoOptions = ['球镜', '眼轴', '柱镜', '等效度数']
export default {
  data () {
    return {
      optionLeftLine: {
        title: {
          text: '左眼'
        },
        tooltip: {},
        legend: {
          data: ['球镜']
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
          data: ['球镜']
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: []
      },
      checkAll: false,
      checkedInfo: ['球镜'],
      Info: infoOptions,
      isIndeterminate: true,
      balL:
      {
        name: '球镜',
        type: 'line', // 设置图表主题
        data: []
      },
      balR:
      {
        name: '球镜',
        type: 'line', // 设置图表主题
        data: []
      },
      axeL:
      {
        name: '眼轴',
        type: 'line', // 设置图表主题
        data: []
      },
      axeR:
      {
        name: '眼轴',
        type: 'line', // 设置图表主题
        data: []
      },
      posL:
      {
        name: '柱镜',
        type: 'line', // 设置图表主题
        data: []
      },
      posR:
      {
        name: '柱镜',
        type: 'line', // 设置图表主题
        data: []
      },
      eqDegreeL:
      {
        name: '等效度数',
        type: 'line', // 设置图表主题
        data: []
      },
      eqDegreeR:
      {
        name: '等效度数',
        type: 'line', // 设置图表主题
        data: []
      }
    }
  },
  methods: {
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
    },
    handleCheckAllChange (val) {
      this.checkedInfo = val ? infoOptions : []
      this.isIndeterminate = false
    },
    handleCheckedInfoChange (value) {
      let checkedCount = value.length
      this.checkAll = checkedCount === this.Info.length
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.Info.length
    },
    handleLine () {
      this.optionLeftLine['series'] = []
      this.optionRightLine['series'] = []
      console.log(this.optionLeftLine['series'])
      if (this.checkedInfo.includes('球镜')) {
        this.optionLeftLine['series'].push(this.balL)
        this.optionRightLine['series'].push(this.balR)
      }
      if (this.checkedInfo.includes('眼轴')) {
        this.optionLeftLine['series'].push(this.axeL)
        this.optionRightLine['series'].push(this.axeR)
      }
      if (this.checkedInfo.includes('柱镜')) {
        this.optionLeftLine['series'].push(this.posL)
        this.optionRightLine['series'].push(this.posR)
      }
      if (this.checkedInfo.includes('等效度数')) {
        this.optionLeftLine['series'].push(this.eqDegreeL)
        this.optionRightLine['series'].push(this.eqDegreeR)
      }
    },
    onsubmit () {
      console.log('submit')
      this.optionLeftLine['legend']['data'] = this.checkedInfo
      this.optionRightLine['legend']['data'] = this.checkedInfo
      this.handleLine()
      this.draw()
    },
    setData (data) {
      for (var i = 0; i < data.length; i++) {
        var times = '第' + (i + 1) + '次'
        this.optionLeftLine['xAxis']['data'].push(times)
        this.optionRightLine['xAxis']['data'].push(times)
        this.balL['data'].push(data[i]['S_OP_IP_Bal'])
        this.balR['data'].push(data[i]['S_OP_IP_Bal1'])
        this.axeL['data'].push(data[i]['S_OP_IP_Axe'])
        this.axeR['data'].push(data[i]['S_OP_IP_Axe1'])
        this.posL['data'].push(data[i]['S_OP_IP_Pos'])
        this.posR['data'].push(data[i]['S_OP_IP_Pos1'])
        this.eqDegreeL['data'].push(data[i]['Eq_Degree'])
        this.eqDegreeR['data'].push(data[i]['Eq_Degree1'])
      }
    }
  },
  mounted () {
    axios.get(this.$store.state.BASEURL +
    'user/get_visual_data?' +
    'username=' +
    this.$store.state.username
    ).then(
      res => {
        this.setData(res.data)
        this.optionLeftLine['series'].push(this.balL)
        this.optionRightLine['series'].push(this.balR)
        this.draw()
      }
    )
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
.el-button--medium, .el-button--medium.is-round {
    padding: 9px 15px;
    margin-left: 40px;
    margin-bottom: 20px;
}
</style>
