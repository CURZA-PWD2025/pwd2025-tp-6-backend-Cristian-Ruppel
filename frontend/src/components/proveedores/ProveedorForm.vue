<template>
  <div class="proveedor-form">
    <h2>{{ esEdicion ? '✏️ Editar Proveedor' : '➕ Nuevo Proveedor' }}</h2>
    
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
        <label>Teléfono:</label>
        <input 
          v-model="form.telefono" 
          type="tel" 
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label>Email (opcional):</label>
        <input 
          v-model="form.email" 
          type="email" 
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
import { useProveedorStore } from '@/stores/useProveedorStore';

const route = useRoute();
const router = useRouter();
const store = useProveedorStore();

const esEdicion = ref(false);
const form = ref({
  nombre: '',
  telefono: '',
  email: ''
});

onMounted(() => {
  if (route.params.id) {
    esEdicion.value = true;
    cargarProveedor(Number(route.params.id));
  }
});

const cargarProveedor = async (id: number) => {
  await store.fetchProveedorById(id);
  if (store.currentProveedor) form.value = { ...store.currentProveedor };
};

const guardar = async () => {
  if (esEdicion.value) {
    await store.updateProveedor(Number(route.params.id), form.value);
  } else {
    await store.createProveedor(form.value);
  }
  router.push('/proveedores');
};

const cancelar = () => router.push('/proveedores');
</script>

<style scoped>
.proveedor-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

</style>