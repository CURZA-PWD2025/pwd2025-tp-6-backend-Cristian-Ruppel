import apiService from './apiService';

export default {
  async getAll() {
    return await apiService.get('/articulos');
  },

  async getById(id: number) {
    return await apiService.getById('/articulos', id);
  },

  async create(articuloData: any) {
    return await apiService.post('/articulos', articuloData);
  },

  async update(id: number, articuloData: any) {
    return await apiService.put('/articulos', id, articuloData);
  },

  async delete(id: number) {
    return await apiService.delete('/articulos', id);
  }
};