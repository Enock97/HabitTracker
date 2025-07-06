import { useState } from 'react';
import { Container, Typography } from '@mui/material';
import AddHabitForm from '../components/AddHabitForm';
import HabitList from '../components/HabitList';

export default function HomePage() {
  const [reloadTrigger, setReloadTrigger] = useState(false);

  const refreshHabits = () => {
    setReloadTrigger(prev => !prev);
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>Habit Tracker</Typography>
      <AddHabitForm onAdd={refreshHabits} />
      <HabitList reloadTrigger={reloadTrigger} />
    </Container>
  );
}