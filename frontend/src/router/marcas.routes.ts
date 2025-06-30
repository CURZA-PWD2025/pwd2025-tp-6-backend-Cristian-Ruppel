import type { RouteRecordRaw } from 'vue-router'

export default [
  {
    path: '/marcas',
    name: 'Marcas',
    component: () => import('@/views/MarcasView.vue'),
    meta: { auth: true, icon: 'mdi-tag' }
  },
  {
    path: '/marcas/crear',
    name: 'CrearMarca',
    component: () => import('@/components/marcas/MarcaForm.vue'),
    meta: { auth: true }
  }
] as RouteRecordRaw[]