import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Types
export interface Client {
  id: number;
  name: string;
  contact_info: string;
  address: string;
  email: string;
  phone: string;
  status: boolean;
}

export interface Project {
  id: number;
  client_id: number;
  name: string;
  description: string;
  start_date: string;
  end_date: string;
  status: 'planned' | 'in_progress' | 'completed' | 'on_hold';
  location: string;
  total_area: number;
  project_type: string;
  budget: number;
}

// API functions
export const clients = {
  getAll: () => api.get<Client[]>('/api/v1/clients'),
  getById: (id: number) => api.get<Client>(`/api/v1/clients/${id}`),
  create: (data: Omit<Client, 'id'>) => api.post<Client>('/api/v1/clients', data),
  update: (id: number, data: Partial<Client>) => api.put<Client>(`/api/v1/clients/${id}`, data),
  delete: (id: number) => api.delete(`/api/v1/clients/${id}`),
};

export const projects = {
  getAll: () => api.get<Project[]>('/api/v1/projects'),
  getById: (id: number) => api.get<Project>(`/api/v1/projects/${id}`),
  create: (data: Omit<Project, 'id'>) => api.post<Project>('/api/v1/projects', data),
  update: (id: number, data: Partial<Project>) => api.put<Project>(`/api/v1/projects/${id}`, data),
  delete: (id: number) => api.delete(`/api/v1/projects/${id}`),
};

export default api; 