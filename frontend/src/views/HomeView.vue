<template>
  <BaseLayout>
    <template #logo>
      <h2>Dashboard</h2>
    </template>

    <template #menu-nav>
      <nav class="menu-nav">
        <ul>
          <li class="active">Inicio</li>
          <li @click="goTo('articulos')">Artículos</li>
          <li @click="goTo('categorias')">Categorías</li>
        </ul>
      </nav>
    </template>

    <template #main>
      <h2>Bienvenido al Sistema</h2>
      <p>Seleccione una opción del menú para comenzar</p>
    </template>

    <template #aside>
      <nav class="menu-lateral">
        <ul>
          <li @click="goTo('marcas')">Marcas</li>
          <li @click="goTo('proveedores')">Proveedores</li>
        </ul>
      </nav>
    </template>
  </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/layouts/BaseLayout.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const goTo = (routeName: string) => {
  router.push({ name: routeName });
};
</script>

<style scoped>

</style>