import { useState } from 'react';
import {
  Container, Typography, Paper, IconButton, useTheme, useMediaQuery
} from '@mui/material';
import { Brightness4, Brightness7 } from '@mui/icons-material';
import AddHabitForm from '../components/AddHabitForm';
import HabitList from '../components/HabitList';

interface Props {
  darkMode: boolean;
  setDarkMode: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function HomePage({ darkMode, setDarkMode }: Props) {
  const [reloadTrigger, setReloadTrigger] = useState(false);

  const refreshHabits = () => {
    setReloadTrigger(prev => !prev);
  };

  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  return (
    <Container maxWidth="sm" sx={{ mt: 5 }}>
      <Paper elevation={3} sx={{ p: 4, borderRadius: 3 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography variant={isMobile ? 'h5' : 'h4'} gutterBottom>
            Habit Tracker
          </Typography>
          <IconButton onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? <Brightness7 /> : <Brightness4 />}
          </IconButton>
        </div>
        <AddHabitForm onAdd={refreshHabits} />
        <HabitList reloadTrigger={reloadTrigger} />
      </Paper>
    </Container>
  );
}
