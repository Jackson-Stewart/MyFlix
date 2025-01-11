const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  res.json({ status: 'Video streaming service is running' });
});

app.listen(3001, () => {
  console.log('Video streaming service running on port 3001');
});
