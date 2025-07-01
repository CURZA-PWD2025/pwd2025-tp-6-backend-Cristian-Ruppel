<template>
  <div class="articulo-form">
    <h2>{{ esEdicion ? '✏️ Editar Artículo' : '➕ Nuevo Artículo' }}</h2>
    
    <form @submit.prevent="guardar">
      <div class="form-group">
        <label>Descripción:</label>
        <input 
          v-model="form.descripcion" 
          type="text" 
          required
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label>Precio:</label>
        <input 
          v-model.number="form.precio" 
          type="number" 
          step="0.01" 
          min="0"
          required
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label>Stock:</label>
        <input 
          v-model.number="form.stock" 
          type="number" 
          min="0"
          required
          class="form-input"
        >
      </div>

      <div class="form-actions">
        <button type="submit" class="save-btn">
          {{ esEdicion ? 'Actualizar' : 'Guardar' }}
        </button>
        <button type="button" @click="cancelar" class="cancel-btn">
          Cancelar
        </button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticuloStore } from '@/stores/useArticuloStore';

const route = useRoute();
const router = useRouter();
const store = useArticuloStore();

const esEdicion = ref(false);
const form = ref({
  descripcion: '',
  precio: 0,
  stock: 0
});

onMounted(() => {
  if (route.params.id) {
    esEdicion.value = true;
    cargarArticulo(Number(route.params.id));
  }
});

const cargarArticulo = async (id: number) => {
  await store.fetchArticuloById(id);
  if (store.currentArticulo) form.value = { ...store.currentArticulo };
};

const guardar = async () => {
  if (esEdicion.value) {
    await store.updateArticulo(Number(route.params.id), form.value);
  } else {
    await store.createArticulo(form.value);
  }
  router.push('/articulos');
};

const cancelar = () => router.push('/articulos');
</script>

<style scoped>
.articulo-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-weight: 500;
}

.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

.form-input {
  width: 100%;
  padding: 0.6rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-actions {
  display: flex;
  gap: 0.8rem;
  margin-top: 1.5rem;
}

.save-btn {
  background-color: #42b983;
  color: white;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #2c3e50;
  padding: 0.6rem 1.2rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
}
</style>