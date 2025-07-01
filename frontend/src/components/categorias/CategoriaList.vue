<template>
  <div class="categoria-list">
    <div class="list-header">
      <h2>Categorías</h2>
      <router-link to="/categorias/nuevo" class="new-btn">
        ＋ Nueva Categoría
      </router-link>
    </div>

    <div v-if="store.loading" class="loading">Cargando...</div>
    <div v-else-if="store.error" class="error">{{ store.error }}</div>

    <table v-else class="data-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="categoria in store.categorias" :key="categoria.id">
          <td>{{ categoria.id }}</td>
          <td>{{ categoria.nombre }}</td>
          <td>{{ categoria.descripcion || '—' }}</td>
          <td class="actions">
            <button @click="editar(categoria.id)" class="edit-btn">Editar</button>
            <button @click="eliminar(categoria.id)" class="delete-btn">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { useCategoriaStore } from '@/stores/useCategoriaStore';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const store = useCategoriaStore();
const router = useRouter();

onMounted(() => store.fetchCategorias());

const editar = (id: number) => router.push(`/categorias/editar/${id}`);
const eliminar = (id: number) => {
  if (confirm('¿Eliminar esta categoría?')) store.deleteCategoria(id);
};
</script>

<style scoped>
.categoria-list {
  padding: 1rem;
  max-width: 1000px;
  margin: 0 auto;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

h2 {
  color: #2c3e50;
  font-weight: 500;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th, .data-table td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #eaeaea;
}

.data-table th {
  background-color: #f8f9fa;
  color: #2c3e50;
  font-weight: 600;
}

.actions {
  display: flex;
  gap: 0.5rem;
}

.new-btn {
  background-color: #42b983;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.9rem;
}

.edit-btn {
  background-color: #2c3e50;
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.delete-btn {
  background-color: #e74c3c;
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.loading, .error {
  padding: 1rem;
  text-align: center;
  color: #2c3e50;
}

.error {
  color: #e74c3c;
}
</style>