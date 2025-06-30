import type { RouteRecordRaw } from 'vue-router'

export default [
  {
    path: '/categorias',
    name: 'Categorias',
    component: () => import('@/views/CategoriasView.vue'),
    meta: { auth: true, icon: 'mdi-shape-outline' }
  },
  {
    path: '/categorias/crear',
    name: 'CrearCategoria',
    component: () => import('@/components/categorias/CategoriaForm.vue'),
    meta: { auth: true }
  }
] as RouteRecordRaw[]