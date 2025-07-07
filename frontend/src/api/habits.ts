import axios from 'axios';
import { Habit } from '../types';

const API_URL =
  process.env.REACT_APP_API_URL ??
  'https://pogv79s4w9.execute-api.eu-north-1.amazonaws.com/habits';

export const getHabits = async (): Promise<Habit[]> => {
  const res = await axios.get<Habit[]>(API_URL);
  return res.data;
};

export const addHabit = async (habit: { name: string }) => {
  await axios.post(API_URL, habit);
};

export const deleteHabit = async (id: string) => {
  await axios.delete(`${API_URL}/${id}`);
};

export const updateHabit = async (
  id: string,
  updates: Partial<{ name: string; completed: boolean }>
) => {
  await axios.put(`${API_URL}/${id}`, updates);
};
