import React from 'react';
import Attendance from './components/Attendance';
import Scheduler from './components/Scheduler';
import Analytics from './components/Analytics';
import Notifications from './components/Notifications';
import Login from './components/Login';

function App() {
  return (
    <div>
      <h1>Educational Attendance and Scheduler System v2</h1>
      <Login />
      <Attendance />
      <Scheduler />
      <Analytics />
      <Notifications />
    </div>
  );
}

export default App;
