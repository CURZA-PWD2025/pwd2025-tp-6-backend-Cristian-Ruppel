<template>
  <div class="marca-list">
    <div class="list-header">
      <h2>Marcas</h2>
      <router-link to="/marcas/nuevo" class="new-btn">
        ＋ Nueva Marca
      </router-link>
    </div>

    <div v-if="store.loading" class="loading">Cargando...</div>
    <div v-else-if="store.error" class="error">{{ store.error }}</div>

    <table v-else class="data-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Origen</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="marca in store.marcas" :key="marca.id">
          <td>{{ marca.id }}</td>
          <td>{{ marca.nombre }}</td>
          <td>{{ marca.origen || '—' }}</td>
          <td class="actions">
            <button @click="editar(marca.id)" class="edit-btn">Editar</button>
            <button @click="eliminar(marca.id)" class="delete-btn">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { useMarcaStore } from '@/stores/useMarcaStore';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const store = useMarcaStore();
const router = useRouter();

onMounted(() => store.fetchMarcas());

const editar = (id: number) => router.push(`/marcas/editar/${id}`);
const eliminar = (id: number) => {
  if (confirm('¿Eliminar esta marca?')) store.deleteMarca(id);
};
</script>

<style scoped>
.marca-list {
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