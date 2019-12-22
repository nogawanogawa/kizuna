import HomePage from "@/components/pages/HomePage.vue"
import RegisterPage from "@/components/pages/RegisterPage.vue"
import SearchPage from "@/components/pages/SearchPage.vue"
import DetailPage from "@/components/pages/DetailPage.vue"
import UpdatePage from "@/components/pages/UpdatePage.vue"
import AnalysisPage from "@/components/pages/AnalysisPage.vue"
import KeywordPage from "@/components/pages/KeywordPage.vue"

export default [{
    path: '/',
    redirect: 'Home'
}, {
    path: '/Home',
    component: HomePage
}, {
    path: '/Search',
    component: SearchPage
}, {
    path: '/Register',
    component: RegisterPage
}, {
    path: '/Detail',
    component: DetailPage
}, {
    path: '/Update',
    component: UpdatePage
}, {
    path: '/Analysis',
    component: AnalysisPage
}, {
    path: '/Keyword',
    component: KeywordPage
}, {
    path: '*',
    redirect: '/'
}]
