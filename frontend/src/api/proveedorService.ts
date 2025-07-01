import apiService from './apiService';

export default {
  async getAll() {
    return await apiService.get('/proveedores');
  },

  async getById(id: number) {
    return await apiService.getById('/proveedores', id);
  },

  async create(proveedorData: any) {
    return await apiService.post('/proveedores', proveedorData);
  },

  async update(id: number, proveedorData: any) {
    return await apiService.put('/proveedores', id, proveedorData);
  },

  async delete(id: number) {
    return await apiService.delete('/proveedores', id);
  }
};