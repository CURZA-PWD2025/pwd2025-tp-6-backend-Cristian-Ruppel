<template>
  <div class="marca-form">
    <h2>{{ esEdicion ? '✏️ Editar Marca' : '➕ Nueva Marca' }}</h2>
    
    <form @submit.prevent="guardar">
      <div class="form-group">
        <label>Nombre:</label>
        <input 
          v-model="form.nombre" 
          type="text" 
          required
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label>Origen (opcional):</label>
        <input 
          v-model="form.origen" 
          type="text" 
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label>Sitio web (opcional):</label>
        <input 
          v-model="form.sitio_web" 
          type="url" 
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
import { useMarcaStore } from '@/stores/useMarcaStore';

const route = useRoute();
const router = useRouter();
const store = useMarcaStore();

const esEdicion = ref(false);
const form = ref({
  nombre: '',
  origen: '',
  sitio_web: ''
});

onMounted(() => {
  if (route.params.id) {
    esEdicion.value = true;
    cargarMarca(Number(route.params.id));
  }
});

const cargarMarca = async (id: number) => {
  await store.fetchMarcaById(id);
  if (store.currentMarca) form.value = { ...store.currentMarca };
};

const guardar = async () => {
  if (esEdicion.value) {
    await store.updateMarca(Number(route.params.id), form.value);
  } else {
    await store.createMarca(form.value);
  }
  router.push('/marcas');
};

const cancelar = () => router.push('/marcas');
</script>

<style scoped>
.marca-form {
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