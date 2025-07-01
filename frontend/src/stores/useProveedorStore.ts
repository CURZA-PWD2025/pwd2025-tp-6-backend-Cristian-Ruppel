import { defineStore } from 'pinia';
import proveedorService from '@/api/proveedorService';

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({
    proveedores: [] as any[],
    currentProveedor: null as any,
    loading: false,
    error: null as string | null
  }),

  actions: {
    async fetchProveedores() {
      this.loading = true;
      this.error = null;
      try {
        this.proveedores = await proveedorService.getAll();
      } catch (error: any) {
        this.error = error.message || 'Error al cargar proveedores';
      } finally {
        this.loading = false;
      }
    },

    async fetchProveedorById(id: number) {
      this.loading = true;
      this.error = null;
      try {
        this.currentProveedor = await proveedorService.getById(id);
      } catch (error: any) {
        this.error = error.message || 'Error al cargar el proveedor';
      } finally {
        this.loading = false;
      }
    },

    async createProveedor(proveedorData: any) {
      this.loading = true;
      this.error = null;
      try {
        await proveedorService.create(proveedorData);
        await this.fetchProveedores();
      } catch (error: any) {
        this.error = error.message || 'Error al crear proveedor';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateProveedor(id: number, proveedorData: any) {
      this.loading = true;
      this.error = null;
      try {
        await proveedorService.update(id, proveedorData);
        await this.fetchProveedores();
      } catch (error: any) {
        this.error = error.message || 'Error al actualizar proveedor';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteProveedor(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await proveedorService.delete(id);
        await this.fetchProveedores();
      } catch (error: any) {
        this.error = error.message || 'Error al eliminar proveedor';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});