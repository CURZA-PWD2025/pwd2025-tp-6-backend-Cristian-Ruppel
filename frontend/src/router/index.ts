import { createRouter, createWebHistory } from 'vue-router'
import articulosRoutes from './articulos.routes'
import marcasRoutes from './marcas.routes'
import proveedoresRoutes from './proveedores.routes'
import categoriasRoutes from './categorias.routes'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/HomeView.vue'),
      meta: { auth: true, icon: 'mdi-home' }
    },
    ...articulosRoutes,
    ...marcasRoutes,
    ...proveedoresRoutes,
    ...categoriasRoutes,
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/LoginView.vue'),
      meta: { auth: false }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isAuth = localStorage.getItem('token')
  if (to.meta.auth && !isAuth) next({ name: 'Login' })
  else next()
})

export default router