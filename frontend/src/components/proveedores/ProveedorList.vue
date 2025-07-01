<template>
  <div class="proveedor-list">
    <div class="list-header">
      <h2>Proveedores</h2>
      <router-link to="/proveedores/nuevo" class="new-btn">
        ＋ Nuevo Proveedor
      </router-link>
    </div>

    <div v-if="store.loading" class="loading">Cargando...</div>
    <div v-else-if="store.error" class="error">{{ store.error }}</div>

    <table v-else class="data-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Teléfono</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proveedor in store.proveedores" :key="proveedor.id">
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre }}</td>
          <td>{{ proveedor.telefono || '—' }}</td>
          <td class="actions">
            <button @click="editar(proveedor.id)" class="edit-btn">Editar</button>
            <button @click="eliminar(proveedor.id)" class="delete-btn">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { useProveedorStore } from '@/stores/useProveedorStore';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const store = useProveedorStore();
const router = useRouter();

onMounted(() => store.fetchProveedores());

const editar = (id: number) => router.push(`/proveedores/editar/${id}`);
const eliminar = (id: number) => {
  if (confirm('¿Eliminar este proveedor?')) store.deleteProveedor(id);
};
</script>

<style scoped>
.proveedor-list {
  padding: 1rem;
  max-width: 1000px;
  margin: 0 auto;
}

</style>