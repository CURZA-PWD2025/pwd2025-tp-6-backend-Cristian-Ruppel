import type { RouteRecordRaw } from 'vue-router'

export default [
  {
    path: '/proveedores',
    name: 'Proveedores',
    component: () => import('@/views/ProveedoresView.vue'),
    meta: { auth: true, icon: 'mdi-truck-delivery' }
  },
  {
    path: '/proveedores/crear',
    name: 'CrearProveedor',
    component: () => import('@/components/proveedores/ProveedorForm.vue'),
    meta: { auth: true }
  }
] as RouteRecordRaw[]