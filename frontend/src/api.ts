import axios from 'axios';
import {apiUrl} from '@/env';
import {IUserProfile, IUserProfileUpdate, IUserProfileCreate, IQuote, IQuoteCreate, IQuoteUpdate, ITag, ITagCreate, ITagUpdate} from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/users/`, data, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/reset-password/`, {
      new_password: password,
      token,
    });
  },
  async getQuotes(token: string) {
    return axios.get<IQuote[]>(`${apiUrl}/api/quotes/`, authHeaders(token));
  },
  async getQuote(token: string, quoteId: number) {
    return axios.get<IQuote>(`${apiUrl}/api/quotes/${quoteId}`, authHeaders(token));
  },
  async updateQuote(token: string, quoteId: number, data: IQuoteUpdate) {
    return axios.put(`${apiUrl}/api/quotes/${quoteId}`, data, authHeaders(token));
  },
  async createQuote(token: string, data: IQuoteCreate) {
    return axios.post(`${apiUrl}/api/quotes/`, data, authHeaders(token));
  },
  async deleteQuote(token: string, quoteId: number) {
    return axios.delete(`${apiUrl}/api/quotes/${quoteId}`, authHeaders(token));
  },
  async getTags(token: string) {
    return axios.get<ITag[]>(`${apiUrl}/api/tags/`, authHeaders(token));
  },
  async getTag(token: string, tagId: number) {
    return axios.get<ITag>(`${apiUrl}/api/tags/${tagId}`, authHeaders(token));
  },
  async updateTag(token: string, tagId: number, data: ITagUpdate) {
    return axios.put(`${apiUrl}/api/tags/${tagId}`, data, authHeaders(token));
  },
  async createTag(token: string, data: ITagCreate) {
    return axios.post(`${apiUrl}/api/tags/`, data, authHeaders(token));
  },
  async deleteTag(token: string, tagId: number) {
    return axios.delete(`${apiUrl}/api/quotes/${tagId}`, authHeaders(token));
  },
};
