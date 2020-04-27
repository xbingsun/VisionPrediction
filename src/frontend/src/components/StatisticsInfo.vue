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
            <div id="sexInfo" :style="{width: '500px', height: '500px'}"></div>
          </el-col>
          <el-col :span=12>
            <div id="ageInfo" :style="{width: '500px', height: '500px'}"></div>
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
      sexInfo: {
        title: {
          text: '近视人群性别分布',
          x: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          bottom: 'bottom',
          data: ['女性', '男性']
        },
        series: [
          {
            name: '性别分布',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
            ],
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      },
      ageInfo: {
        title: {
          text: '近视人群年龄分布',
          x: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          bottom: 'bottom',
          data: ['0~12岁', '12~18岁', '18~24岁', '24岁以上']
        },
        series: [
          {
            name: '年龄分布',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
            ],
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      },
      female: {
        value: 0,
        name: '女性'
      },
      male: {
        value: 0,
        name: '男性'
      },
      age0to12: {
        value: 0,
        name: '0~12岁'
      },
      age12to18: {
        value: 0,
        name: '12~18岁'
      },
      age18to24: {
        value: 0,
        name: '18~24岁'
      },
      age24to: {
        value: 0,
        name: '24岁以上'
      }
    }
  },
  methods: {
    setData (data) {
      this.female['value'] = data['female']
      this.male['value'] = data['male']
      this.age0to12['value'] = data['age0to12']
      this.age12to18['value'] = data['age12to18']
      this.age18to24['value'] = data['age18to24']
      this.age24to['value'] = data['age24to']
      this.sexInfo['series'][0]['data'].push(this.female)
      this.sexInfo['series'][0]['data'].push(this.male)
      this.ageInfo['series'][0]['data'].push(this.age0to12)
      this.ageInfo['series'][0]['data'].push(this.age12to18)
      this.ageInfo['series'][0]['data'].push(this.age18to24)
      this.ageInfo['series'][0]['data'].push(this.age24to)
    },
    draw () {
      // 基于准备好的dom,初始化echarts实例
      let sexInfo = this.$echarts.init(
        document.getElementById('sexInfo')
      )
      let ageInfo = this.$echarts.init(
        document.getElementById('ageInfo')
      )
      // 绘制图表
      sexInfo.setOption(this.sexInfo, true)
      ageInfo.setOption(this.ageInfo, true)
    }
  },
  mounted () {
    axios
      .get(
        this.$store.state.BASEURL +
          'user/get_stat'
      )
      .then(res => {
        this.setData(res.data)
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
</style>
