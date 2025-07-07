import { useEffect, useState } from 'react';
import {
  List, ListItem, Checkbox, IconButton, ListItemText,
  Dialog, DialogTitle, DialogContent, DialogActions,
  Button, TextField, Typography, ToggleButton, ToggleButtonGroup,
  LinearProgress, Box
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { getHabits, deleteHabit, updateHabit } from '../api/habits';
import { Habit } from '../types';

interface Props {
  reloadTrigger: boolean;
}

type Filter = 'all' | 'active' | 'completed';

export default function HabitList({ reloadTrigger }: Props) {
  const [habits, setHabits] = useState<Habit[]>([]);
  const [editingHabit, setEditingHabit] = useState<Habit | null>(null);
  const [editedName, setEditedName] = useState('');
  const [filter, setFilter] = useState<Filter>('all');

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

    const handleDelete = async (id: string) => {
    await deleteHabit(id);
    fetchHabits();
    };

  const handleEditClick = (habit: Habit) => {
    setEditingHabit(habit);
    setEditedName(habit.name);
  };

  const handleEditSave = async () => {
    if (!editingHabit) return;
    if (!editedName.trim() || editedName === editingHabit.name) {
        setEditingHabit(null);
        return;
    }
    await updateHabit(editingHabit.id, { name: editedName });
    setEditingHabit(null);
    fetchHabits();
  };

  const filteredHabits = habits.filter((habit) => {
    if (filter === 'completed') return habit.completed;
    if (filter === 'active') return !habit.completed;
    return true;
  });

  const completedCount = habits.filter(h => h.completed).length;
  const progress = habits.length > 0 ? (completedCount / habits.length) * 100 : 0;

  return (
    <>
      <Box sx={{ mb: 2 }}>
        <Typography variant="subtitle1">{completedCount} of {habits.length} completed</Typography>
        <LinearProgress variant="determinate" value={progress} sx={{ height: 8, borderRadius: 5 }} />
      </Box>

      <ToggleButtonGroup
        value={filter}
        exclusive
        onChange={(e, val) => val && setFilter(val)}
        sx={{ mb: 2 }}
      >
        <ToggleButton value="all">All</ToggleButton>
        <ToggleButton value="active">Active</ToggleButton>
        <ToggleButton value="completed">Completed</ToggleButton>
      </ToggleButtonGroup>

      {filteredHabits.length === 0 ? (
        <Typography variant="body1" color="text.secondary">
          No habits to show.
        </Typography>
      ) : (
        <List>
          {filteredHabits.map((habit) => (
            <ListItem
              key={habit.id}
              secondaryAction={
                <>
                  <IconButton edge="end" onClick={() => handleEditClick(habit)}>
                    <EditIcon />
                  </IconButton>
                  <IconButton edge="end" onClick={() => handleDelete(habit.id)}>
                    <DeleteIcon />
                  </IconButton>
                </>
              }
            >
              <Checkbox
                checked={habit.completed}
                onChange={() => toggleCompleted(habit)}
              />
              <ListItemText primary={habit.name} />
            </ListItem>
          ))}
        </List>
      )}

      <Dialog open={!!editingHabit} onClose={() => setEditingHabit(null)}>
        <DialogTitle>Edit Habit</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Habit Name"
            fullWidth
            value={editedName}
            onChange={(e) => setEditedName(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditingHabit(null)}>Cancel</Button>
          <Button onClick={handleEditSave} variant="contained">Save</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}