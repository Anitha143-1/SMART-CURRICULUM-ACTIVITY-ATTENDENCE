import os
import zipfile

# Define new folder and structure
base_dir = 'edu_attendance_web_v2'
folders = [
    'client',
    'client/public',
    'client/src/components',
    'server',
    'server/routes',
    'server/models',
    'config'
]

# Clean old if exists
if os.path.exists(base_dir):
    import shutil
    shutil.rmtree(base_dir)

# Create folders
os.makedirs(base_dir, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# File contents for client React app
files_content = {
    f'{base_dir}/client/public/index.html': """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Edu Attendance Web V2</title>
</head>
<body>
  <div id=\"root\"></div>
</body>
</html>
""",

    f'{base_dir}/client/src/index.js': """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
""",

    f'{base_dir}/client/src/App.js': """import React from 'react';
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
""",

    f'{base_dir}/client/src/components/Attendance.js': """import React from 'react';
export default function Attendance() {
  return <div><h2>Attendance Component Placeholder</h2></div>;
}
""",

    f'{base_dir}/client/src/components/Scheduler.js': """import React from 'react';
export default function Scheduler() {
  return <div><h2>Scheduler Component Placeholder</h2></div>;
}
""",

    f'{base_dir}/client/src/components/Analytics.js': """import React from 'react';
export default function Analytics() {
  return <div><h2>Analytics Dashboard Placeholder</h2></div>;
}
""",

    f'{base_dir}/client/src/components/Notifications.js': """import React from 'react';
export default function Notifications() {
  return <div><h2>Notifications Component Placeholder</h2></div>;
}
""",

    f'{base_dir}/client/src/components/Login.js': """import React from 'react';
export default function Login() {
  return <div><h2>Login Component Placeholder</h2></div>;
}
""",

    f'{base_dir}/server/app.js': """const express = require('express');
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
""",

    f'{base_dir}/package.json': """{
  \"name\": \"edu-attendance-web-v2\",
  \"version\": \"1.0.0\",
  \"main\": \"server/app.js\",
  \"scripts\": {
    \"start\": \"node server/app.js\",
    \"client-start\": \"cd client && npm start\"
  },
  \"dependencies\": {
    \"cors\": \"^2.8.5\",
    \"express\": \"^4.18.2\",
    \"react\": \"^18.2.0\",
    \"react-dom\": \"^18.2.0\"
  }
}
""",

    f'{base_dir}/README.md': """# Educational Attendance and Scheduler Website v2

## Run Backend
- npm install
- npm start

## Run Frontend
- cd client
- npm install
- npm start

## Project Structure
- client/: React frontend
- server/: Express backend
"""
}

# Write files
for path, content in files_content.items():
    with open(path, 'w') as f:
        f.write(content)

# Create zip
zipname = f'{base_dir}.zip'
with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(base_dir):
        for file in files:
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), base_dir))

zipname
