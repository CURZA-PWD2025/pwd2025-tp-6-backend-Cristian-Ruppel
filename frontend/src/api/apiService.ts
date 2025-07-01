import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000'  // Ajusta si tu backend usa otro puerto
});

export default {
  async get(endpoint: string) {
    const { data } = await api.get(endpoint);
    return data;
  }
};
