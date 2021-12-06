import {createWebHistory, createRouter} from 'vue-router'

import allFleet from '@/views/allFleet.vue'
import AllRiders from '@/views/AllRiders.vue'
import AllCashRequest from '@/views/AllCashRequest.vue'
import AllErrandService from '@/views/AllErrandService.vue'
import AllFrontDesk from '@/components/AllFrontDesk'
import AllShopping from '@/components/AllShopping'
import AllAdmin from '@/components/AllAdmin'
import Dashboard from '@/components/Dashboard'

Vue.use(VueRouter)

const routes = [
    { path: 'allFleet/', component: allFleet}, 
    { path: 'allRiders/', component: AllRiders},
    { path: 'cashRequest/', component: AllCashRequest},
    { path: 'errandService/', component: AllErrandService},
    {path: 'frontDesk/', component: AllFrontDesk},
    {path: 'shopping/', component: AllShopping},
    {path: 'admin/', component: AllAdmin},
    {path: '/', component: Dashboard},
]
