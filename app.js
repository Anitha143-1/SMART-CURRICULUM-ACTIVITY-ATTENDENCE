const express = require('express');
const cors = require('cors');
const app = express();
const port = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

// Dummy routes
app.get('/api/attendance', (req, res) => {
  res.json({message: 'Attendance API Endpoint v2'});
});

app.get('/api/scheduler', (req, res) => {
  res.json({message: 'Scheduler API Endpoint v2'});
});

app.get('/api/analytics', (req, res) => {
  res.json({message: 'Analytics API Endpoint v2'});
});

app.get('/api/notifications', (req, res) => {
  res.json({message: 'Notifications API Endpoint v2'});
});

app.get('/api/login', (req, res) => {
  res.json({message: 'Login API Endpoint v2'});
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
