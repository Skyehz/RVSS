import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login.vue'
import home from '../components/home.vue'
import register from '../components/register.vue'
import menu from '../components/menu.vue'
import user from '../components/user.vue'
import monitor from '../components/monitor.vue'
import message from '../components/message.vue'
import view from '../components/view.vue'
import help from '../components/help.vue'
import admin_home from '../components/admin_home.vue'
import admin_menu from '../components/admin_menu.vue'
import userlist from '../components/userlist.vue'
import admin_monitor from '../components/admin_monitor.vue'
import admin_message from '../components/admin_message.vue'
import admin_user from '../components/admin_user.vue'
import admin_view1 from '../components/admin_view1.vue'
import admin_view2 from '../components/admin_view2.vue'
import admin_help from '../components/admin_help.vue'

Vue.use(Router)

const router= new Router({
    routes:[
      {path: '/login',component:login},
      {path: '/home',
      component: home , 
      redirect: '/menu',
      children:  [
        {path: '/menu',component: menu},
        {path: '/user',component: user},
        {path:'/help',component: help}
      ]
      },
      {path:'/register',component:register},
      {path:'/monitor',
      component:monitor,
      redirect: '/view',
      children:[
        {path:'/menu',component:menu},
        {path:'/user',component:user},
        {path:'/message',component:message},
        {path:'/view',component:view}
      ]
    },
    {path:'/admin_home',
    component:admin_home,
    redirect: 'admin_menu',
    children:  [
      {path: '/admin_menu',component: admin_menu},
      {path: '/admin_user',component: admin_user},
      {path:'/admin_help',component: admin_help}
    ]
  },
  {path:'/admin_monitor',
  component:admin_monitor,
  redirect: '/admin_view1',
  children:[
    {path:'/admin_menu',component:admin_menu},
    {path:'/admin_user',component:admin_user},
    {path:'/admin_message',component:admin_message},
    {path:'/admin_view1',component:admin_view1},
    {path:'/admin_view2',component:admin_view2},
    {path:'/userlist',component:userlist}

  ]
}
     
    ]
})

//挂载导航守卫
router.beforeEach((to,from,next)=>{
//to 要访问的路径
//from 代表从哪个路径来
//next 放行函数
if(to.path==='/view')return next()
 if(to.path==='/message')return next()
 if(to.path==='/monitor')return next()
 if(to.path==='/register')return next()
 if(to.path==='/login')return next()
 //获取token
 const tokenStr=window.sessionStorage.getItem('token')
if(!tokenStr)return next('/login')
 next();
})

export default router



