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
              <span>用眼小贴士</span>
            </div>
            <div class="text item">{{ advice }}</div>
          </el-card>
          <br>
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>保护眼睛的方法</span>
            </div>
            <div v-for="o in help" :key="o" class="text item">{{ o }}</div>
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
      help: ['1、 光线充足', '光线要充足舒适，（光线太弱，字体看不清楚，就会越看越近视）。 ',
        '2、 反光要避免', '书桌应有边灯装置，其目的在减少反光，以降低对眼睛的伤害。 ',
        '3、 阅读时间勿太长', '无论做功课或看电视，时间不可太长，每一小时左右休息片刻为佳。 ',
        '4、 坐姿要端正 ', '不可弯腰驼背，靠得很近或趴着做功课，这样易造成睫状肌紧张过度而引起疲劳，进而造成成近视。 在阅读操作过程中，应经常眨眨眼睛或闭目休息一会儿，以调节和改善视力，预防视力减退。',
        '5、睡眠不可少，作息有规律 ', '睡眠不足身体易疲劳，易造成假性近视。',
        '6、多做户外运动，并常做眼保健操', '经常眺望远处放松眼肌，防止近视，与大自然多接触，青山绿野有益于眼睛的健康。',
        '7、营养摄取应均衡', '营养摄取应均衡。'
      ],
      advice: ''
    }
  },
  mounted () {
    axios.get(this.$store.state.BASEURL +
    'user/get_user_age?' +
    'username=' +
    this.$store.state.username
    ).then(
      res => {
        if (res.data <= 1) {
          this.advice = '由出生到1周岁这段时间不要包着孩子看过强的光线，以防损伤视力；不要让孩子看固定不变的东西，以免引起斜视。'
        } else if (res.data <= 7) {
          this.advice = '1至7周岁的儿童，主要是玩耍，所以，为了保护眼睛，必须注意选择不带刃以及没有锐角的玩具；同时，家长和保教人员要经常教育孩子，不要做危险性的游戏，看书时光线要充足，但应避开强烈的阳光，眼与物体要保持一定的距离（以1市尺左右为宜）；如有斜视，应及时去医院矫治；并要培养良好的卫生习惯，不用手指揉眼，不用别人的手巾擦眼睛。 '
        } else if (res.data <= 18) {
          this.advice = '看书的姿势要正确，书与眼的远近要适宜，光线要充足，不要在走路或乘车时看书，同时要注意眼病的预防和治疗。 '
        } else {
          this.advice = '成年人，身体各部已经基本发育成熟，眼睛也是这样，所以对各种环境，条件的适应能力也比较强了。这时保护眼睛，主要应从免受外伤方面注意，在各种劳动中要遵守安全操作规程。同时要注意疾病的预防、治疗。'
        }
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
  color: green;
}
.clearfix:after {
  clear: both;
  color: green;
}

.box-card {
  width: 600px;
}
</style>
