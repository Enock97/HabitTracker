import { useEffect, useState } from 'react';
import { List, ListItem, Checkbox, IconButton, ListItemText } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import { getHabits, deleteHabit, updateHabit } from '../api/habits';
import { Habit } from '../types';

interface Props {
  reloadTrigger: boolean;
}

export default function HabitList({ reloadTrigger }: Props) {
  const [habits, setHabits] = useState<Habit[]>([]);

  const fetchHabits = async () => {
    const data = await getHabits();
    setHabits(data);
  };

  useEffect(() => {
    fetchHabits();
  }, [reloadTrigger]);

  const toggleCompleted = async (habit: Habit) => {
    await updateHabit(habit.id, { completed: !habit.completed });
    fetchHabits();
  };

  const handleDelete = async (id: number) => {
    await deleteHabit(id);
    fetchHabits();
  };

  return (
    <List>
      {habits.map((habit) => (
        <ListItem key={habit.id} secondaryAction={
          <IconButton edge="end" onClick={() => handleDelete(habit.id)}>
            <DeleteIcon />
          </IconButton>
        }>
          <Checkbox
            checked={habit.completed}
            onChange={() => toggleCompleted(habit)}
          />
          <ListItemText primary={habit.name} />
        </ListItem>
      ))}
    </List>
  );
}