import Login from '../components/Login'
import Index from '../components/Index'
import VisualData from '../components/VisualData'
import IndexDoc from '../components/IndexDoc'
import NewUser from '../components/NewUser'
import AddUserInfo from '../components/AddUserInfo'
import ModifyDocPass from '../components/ModifyDocPass'
import VisionPrediction from '../components/VisionPrediction'
import ModifyUserPass from '../components/ModifyUserPass'
import ShowUserInfo from '../components/ShowUserInfo'
import VisualAdvice from '../components/VisualAdvice'
import StatisticsInfo from '../components/StatisticsInfo'
const routers = [
  {
    path: '/',
    name: 'login',
    component: Login,
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/index',
    name: 'index',
    component: Index
  },
  {
    path: '/visualdata',
    name: 'visualdata',
    component: VisualData
  },
  {
    path: '/indexdoc',
    name: 'indexdoc',
    component: IndexDoc
  },
  {
    path: '/newuser',
    name: 'newuser',
    component: NewUser
  },
  {
    path: '/adduserinfo',
    name: 'adduserinfo',
    component: AddUserInfo
  },
  {
    path: '/modifydocpass',
    name: 'ModifyDocPass',
    component: ModifyDocPass
  },
  {
    path: '/visionprediction',
    name: 'VisionPrediction',
    component: VisionPrediction
  },
  {
    path: '/modifyuserpass',
    name: 'ModifyUserPass',
    component: ModifyUserPass
  },
  {
    path: '/showuserinfo',
    name: 'ShowUserInfo',
    component: ShowUserInfo
  },
  {
    path: '/visualadvice',
    name: 'VisualAdvice',
    component: VisualAdvice
  },
  {
    path: '/statisticsinfo',
    name: 'StatisticsInfo',
    component: StatisticsInfo
  }
]
export default routers
