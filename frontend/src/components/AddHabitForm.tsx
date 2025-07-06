import { useState } from 'react';
import { Button, Input, Stack } from '@mui/material';
import { addHabit } from '../api/habits';

interface Props {
  onAdd: () => void;
}

export default function AddHabitForm({ onAdd }: Props) {
  const [name, setName] = useState('');

  const handleSubmit = async () => {
    if (!name.trim()) return;
    await addHabit({ name });
    setName('');
    onAdd();
  };

  return (
    <Stack direction="row" spacing={2} sx={{ mb: 3 }}>
      <Input
        placeholder="New habit"
        value={name}
        onChange={(e) => setName(e.target.value)}
        fullWidth
      />
      <Button variant="contained" onClick={handleSubmit}>Add</Button>
    </Stack>
  );
}
