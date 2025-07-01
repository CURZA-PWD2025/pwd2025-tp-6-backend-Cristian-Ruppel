import apiService from './apiService';

export default {
  async getAll() {
    return await apiService.get('/categorias');
  },

  async getById(id: number) {
    return await apiService.getById('/categorias', id);
  },

  async create(categoriaData: any) {
    return await apiService.post('/categorias', categoriaData);
  },

  async update(id: number, categoriaData: any) {
    return await apiService.put('/categorias', id, categoriaData);
  },

  async delete(id: number) {
    return await apiService.delete('/categorias', id);
  }
};