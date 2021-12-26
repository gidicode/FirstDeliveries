
import { createRouter, createWebHistory } from "vue-router"
import Dashboard from '../views/Dashboard.vue'
import Summary from '../views/Summarise/Summary.vue'
import Customers from '../views/Customers/Customers.vue'
import CustomerDetails from '../views/Customers/CustomerDetails.vue'
import RidersSummary from '../views/Riders/RidersSummary.vue'

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
        component: Customers,
        children: [
            {
                path: 'customers/:id',
                name: 'CustomerDetails',
                component:CustomerDetails
            }
        ],
    }, 
    
    {
        path: '/riders',
        name: 'Riders',
        component: RidersSummary,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})


export default router