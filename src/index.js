const express = require('express');
const fetch = require('node-fetch');
const minimist = require('minimist');

const args = minimist(process.argv.slice(2));
const app = express();

app.get('/health', (req, res) => {
  res.json({ status: 'ok', port: args.port || 3000 });
});

app.get('/data', async (req, res) => {
  const items = [3, 1, 4, 1, 5, 9];
  const sorted = items.sort((a, b) => a - b);
  const unique = [...new Set(sorted)];
  res.json({ items: unique });
});

const port = args.port || 3000;
console.log("Analytics service ready on port", port);
