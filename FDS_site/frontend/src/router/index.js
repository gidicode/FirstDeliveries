
import { createRouter, createWebHistory } from "vue-router"
import Dashboard from '../views/Dashboard.vue'
import Summary from '../views/Summarise/Summary.vue'
import Customers from '../views/Customers.vue'

const routes = [
    {
        path: '/',
        name: 'Dashboard',
        component: Dashboard
    },

    {
        path: '/summary',
        name: 'Summary',
        component: Summary
    },

    {
        path: '/customers',
        name: 'Customers',
        component: Customers
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})


export default router