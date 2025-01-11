const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  res.json({ status: 'Auth service is running' });
});

app.listen(3000, () => {
  console.log('Auth service running on port 3000');
});
