import { defineStore } from 'pinia';
import marcaService from '@/api/marcaService';

export const useMarcaStore = defineStore('marca', {
  state: () => ({
    marcas: [] as any[],
    currentMarca: null as any,
    loading: false,
    error: null as string | null
  }),

  actions: {
    async fetchMarcas() {
      this.loading = true;
      this.error = null;
      try {
        this.marcas = await marcaService.getAll();
      } catch (error: any) {
        this.error = error.message || 'Error al cargar marcas';
      } finally {
        this.loading = false;
      }
    },

    async fetchMarcaById(id: number) {
      this.loading = true;
      this.error = null;
      try {
        this.currentMarca = await marcaService.getById(id);
      } catch (error: any) {
        this.error = error.message || 'Error al cargar la marca';
      } finally {
        this.loading = false;
      }
    },

    async createMarca(marcaData: any) {
      this.loading = true;
      this.error = null;
      try {
        await marcaService.create(marcaData);
        await this.fetchMarcas();
      } catch (error: any) {
        this.error = error.message || 'Error al crear marca';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateMarca(id: number, marcaData: any) {
      this.loading = true;
      this.error = null;
      try {
        await marcaService.update(id, marcaData);
        await this.fetchMarcas();
      } catch (error: any) {
        this.error = error.message || 'Error al actualizar marca';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteMarca(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await marcaService.delete(id);
        await this.fetchMarcas();
      } catch (error: any) {
        this.error = error.message || 'Error al eliminar marca';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});