// server2.js

const express = require('express');
const app = express();
const port = 2929;

// FIX: The path must be './routers/StudentRoutes' to match your folder name exactly.
const studentRoutes = require('./routers/StudentRoutes');

// This line correctly mounts the routes.
app.use('/api/student', studentRoutes);

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});