import {createRouter, createWebHashHistory} from 'vue-router'
import indexView from "@/views/indexView";
import adminView from "@/views/adminView";
import overView from "@/views/overView";
import codeView from "@/views/codeView";

const routes = [
    {
        path: '/',
        name: 'indexView',
        components: {indexView}
    }, {
        path: '/admin',
        name: 'adminView',
        components: {adminView}
    }, {
        path: '/overview/:folder',
        name: 'overView',
        components: {overView}
    },{
        path: '/overview/compare_code/:id/:first/:second',
        name: 'codeView',
        components: {codeView}
    },
]

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router
