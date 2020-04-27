<template>
  <div>
    <vue-particles
      color="#dedede"
      :particleOpacity="0.7"
      :particlesNumber="80"
      shapeType="circle"
      :particleSize="4"
      linesColor="#dedede"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="3"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
    ></vue-particles>
    <div class="title">FOREYE</div>
    <el-row>
      <el-col :span="15" :offset="9">
        <el-input v-model="name" placeholder="请输入用户名"></el-input>
      </el-col>
      <el-col :span="15" :offset="9">
        <el-input type="password" v-model="password" placeholder="请输入密码"></el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6" :offset="11">
        <el-radio v-model="radio" label="user">用户</el-radio>
        <el-radio v-model="radio" label="docter">医生</el-radio>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6" :offset="11">
        <button v-on:click="logIn">登录</button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
const axios = require('axios')
export default {
  data () {
    return {
      name: '',
      password: '',
      radio: 'user'
    }
  },
  methods: {
    logIn () {
      if (this.radio === 'user') {
        axios.get(this.$store.state.BASEURL +
      'user/login_user?' +
      'username=' +
      this.name +
      '&password=' +
      this.password
        ).then(
          res => {
            if (res.data === 'loginUserSuccess') {
              this.$message('登录成功')
              this.$store.state.username = this.name
              this.$router.push('/index')
            } else {
              this.$message('登录失败')
            }
          }
        )
      } else {
        axios.get(this.$store.state.BASEURL +
      'user/login_admin?' +
      'username=' +
      this.name +
      '&password=' +
      this.password
        ).then(
          res => {
            if (res.data === 'loginAdminSuccess') {
              this.$message('登录成功')
              this.$store.state.username = this.name
              this.$router.push('/indexdoc')
            } else {
              this.$message('登录失败')
            }
          }
        )
      }
    }
  }
}
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
}
.title {
  font-size: 5rem;
  font-family: Teko, sans-serif;
  color: rgb(255, 255, 255);
  text-shadow: 4px 4px rgba(6, 114, 64, 0.459);
  text-transform: uppercase;
  text-align: center;
  padding-top: 200px;
  margin-bottom: 20px;
}
#particles-js {
  background-color: #64ceaa;
  position: absolute;
  z-index: -10000;
  height: 100%;
  width: 100%;
}
.el-input {
  width: 40%;
  margin-bottom: 20px;
}
button {
  border: none;
  text-align: center;
  text-decoration: none;
  height: 40px;
  width: 90px;
  background-color: rgb(61, 125, 115);
  color: white;
  border-radius: 5px;
  font-size: 16px;
  margin: 20px;
  margin-top: 20px;
  box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;
  outline: none;
}
button:hover {
  background-color: rgba(61, 125, 115, 0.644);
  color: white;
}

.el-input__inner {
    -webkit-appearance: none;
    background-color: #FFF;
    background-image: none;
    border-radius: 4px;
    border: 1px solid #DCDFE6;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    color: #606266;
    display: inline-block;
    font-size: inherit;
    height: 40px;
    line-height: 40px;
    outline: 0;
    padding: 0 15px;
    -webkit-transition: border-color .2s cubic-bezier(.645,.045,.355,1);
    transition: border-color .2s cubic-bezier(.645,.045,.355,1);
    width: 100%;
}
</style>
