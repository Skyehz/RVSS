import Vue from 'vue'

import{Button,Form,FormItem,Input,Message,Container,Header,Aside,Main,Menu,MenuItem,Tooltip,Col,Row,Dialog,Pagination}from "element-ui"


Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Tooltip)
Vue.use(Col)
Vue.use(Row)
Vue.use(Dialog)
Vue.use(Pagination)
//全局挂载
Vue.prototype.$message=Message
