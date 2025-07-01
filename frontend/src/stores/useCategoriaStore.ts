import { defineStore } from 'pinia';
import categoriaService from '@/api/categoriaService';

export const useCategoriaStore = defineStore('categoria', {
  state: () => ({
    categorias: [] as any[],
    currentCategoria: null as any,
    loading: false,
    error: null as string | null
  }),

  actions: {
    async fetchCategorias() {
      this.loading = true;
      this.error = null;
      try {
        this.categorias = await categoriaService.getAll();
      } catch (error: any) {
        this.error = error.message || 'Error al cargar categorías';
      } finally {
        this.loading = false;
      }
    },

    async fetchCategoriaById(id: number) {
      this.loading = true;
      this.error = null;
      try {
        this.currentCategoria = await categoriaService.getById(id);
      } catch (error: any) {
        this.error = error.message || 'Error al cargar la categoría';
      } finally {
        this.loading = false;
      }
    },

    async createCategoria(categoriaData: any) {
      this.loading = true;
      this.error = null;
      try {
        await categoriaService.create(categoriaData);
        await this.fetchCategorias();
      } catch (error: any) {
        this.error = error.message || 'Error al crear categoría';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateCategoria(id: number, categoriaData: any) {
      this.loading = true;
      this.error = null;
      try {
        await categoriaService.update(id, categoriaData);
        await this.fetchCategorias();
      } catch (error: any) {
        this.error = error.message || 'Error al actualizar categoría';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteCategoria(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await categoriaService.delete(id);
        await this.fetchCategorias();
      } catch (error: any) {
        this.error = error.message || 'Error al eliminar categoría';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});