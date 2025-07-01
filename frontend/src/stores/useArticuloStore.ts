import { defineStore } from 'pinia';
import articuloService from '@/api/articuloService';

export const useArticuloStore = defineStore('articulo', {
  state: () => ({
    articulos: [] as any[],
    currentArticulo: null as any,
    loading: false,
    error: null as string | null
  }),

  actions: {
    async fetchArticulos() {
      this.loading = true;
      this.error = null;
      try {
        this.articulos = await articuloService.getAll();
      } catch (error: any) {
        this.error = error.message || 'Error al cargar artículos';
      } finally {
        this.loading = false;
      }
    },

    async fetchArticuloById(id: number) {
      this.loading = true;
      this.error = null;
      try {
        this.currentArticulo = await articuloService.getById(id);
      } catch (error: any) {
        this.error = error.message || 'Error al cargar el artículo';
      } finally {
        this.loading = false;
      }
    },

    async createArticulo(articuloData: any) {
      this.loading = true;
      this.error = null;
      try {
        await articuloService.create(articuloData);
        await this.fetchArticulos();
      } catch (error: any) {
        this.error = error.message || 'Error al crear artículo';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateArticulo(id: number, articuloData: any) {
      this.loading = true;
      this.error = null;
      try {
        await articuloService.update(id, articuloData);
        await this.fetchArticulos(); 
      } catch (error: any) {
        this.error = error.message || 'Error al actualizar artículo';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteArticulo(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await articuloService.delete(id);
        await this.fetchArticulos(); 
      } catch (error: any) {
        this.error = error.message || 'Error al eliminar artículo';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});