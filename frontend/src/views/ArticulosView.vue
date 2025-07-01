<template>
  <BaseLayout>
    <template #logo>
      <h2>Administración</h2>
    </template>

    <template #menu-nav>
      <nav class="menu-nav">
        <ul>
          <li @click="goToHome">Inicio</li>
          <li @click="goTo('articulos')">Artículos</li>
          <li @click="goTo('categorias')">Categorías</li>
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

    <template #footer>
      <p>&copy; 2025 Programación Web Dinámica</p>
    </template>
  </BaseLayout>
</template>

<script setup lang="ts">
import BaseLayout from '@/layouts/BaseLayout.vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';
import { useArticuloStore } from '@/stores/useArticuloStore';

const router = useRouter();
const store = useArticuloStore();

onMounted(() => {
  store.fetchArticulos();
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
.menu-lateral {
  display: flex;
  justify-content: center;
  align-items: center;

  ul {
    list-style: none;
    padding: 0.5em;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    li {
      width: 100%;
      margin: 0.5em 1em;
      background-color: #c45151;
      color: rgb(245, 163, 163);
      transition: 0.5s ease-in-out all;
      padding: 0.5em;
      text-align: center;
      border-radius: 4px;

      &:hover {
        background-color: #c4c4c4;
        color: #000;
        cursor: pointer;
      }
    }
  }
}

.menu-nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;

  li {
    margin: 0 1em;
    color: #fff;
    transition: 0.5s ease-in-out all;
    padding: 0.5em 1em;
    border-radius: 4px;

    &:hover {
      background-color: rgba(255, 255, 255, 0.1);
      cursor: pointer;
    }
  }
}
</style>