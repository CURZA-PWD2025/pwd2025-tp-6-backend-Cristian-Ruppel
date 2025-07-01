import apiService from './apiService';

export default {
  async getAll() {
    return await apiService.get('/marcas');
  },

  async getById(id: number) {
    return await apiService.getById('/marcas', id);
  },

  async create(marcaData: any) {
    return await apiService.post('/marcas', marcaData);
  },

  async update(id: number, marcaData: any) {
    return await apiService.put('/marcas', id, marcaData);
  },

  async delete(id: number) {
    return await apiService.delete('/marcas', id);
  }
};