const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 4000;

app.use(express.json());

app.post('/deploy', (req, res) => {
  console.log('Received webhook request');
  exec('cd /home/ec2-user/myflixSystem && docker-compose down && docker-compose up -d', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send('Deployment failed');
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    res.send('Deployment triggered');
  });
});

app.listen(port, () => {
  console.log(`Webhook server listening at http://localhost:${port}`);
});
