const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  res.json({ status: 'Watchlist service is running' });
});

app.listen(3002, () => {
  console.log('Watchlist service running on port 3002');
});
