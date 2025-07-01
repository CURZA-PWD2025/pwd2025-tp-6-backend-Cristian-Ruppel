<template>
  <BaseLayout>
    <template #logo>
      <h2>Categorías</h2>
    </template>

    <template #menu-nav>
      <nav class="menu-nav">
        <ul>
          <li @click="goToHome">Inicio</li>
          <li @click="goTo('articulos')">Artículos</li>
          <li class="active">Categorías</li>
        </ul>
      </nav>
    </template>

    <template #main>
      <RouterView />
    </template>

    <template #aside>
      <nav class="menu-lateral">
        <ul>
          <li @click="goTo('marcas')">Marcas</li>
          <li @click="goTo('proveedores')">Proveedores</li>
          <li @click="goBack">Volver</li>
        </ul>
      </nav>
    </template>
  </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/layouts/BaseLayout.vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/useCategoriaStore';

const router = useRouter();
const store = useCategoriaStore();

onMounted(() => {
  store.fetchCategorias();
});

const goTo = (routeName: string) => {
  router.push({ name: routeName });
};

const goToHome = () => {
  router.push({ name: 'Home' });
};

const goBack = () => {
  router.go(-1);
};
</script>

<style scoped>

</style>