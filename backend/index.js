const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  // Statische Dateien servieren
  if (req.url === '/' || req.url === '/index.html') {
    const indexPath = path.join(__dirname, 'index.html');
    fs.readFile(indexPath, (err, content) => {
      if (err) {
        res.writeHead(500);
        res.end('Error loading index.html');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(content);
      }
    });
  } else if (req.url === '/pokedex.html') {
    const pokedexPath = path.join(__dirname, 'pokedex.html');
    fs.readFile(pokedexPath, (err, content) => {
      if (err) {
        res.writeHead(500);
        res.end('Error loading pokedex.html');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(content);
      }
    });
  } else if (req.url === '/styles.css') {
    const cssPath = path.join(__dirname, 'styles.css');
    fs.readFile(cssPath, (err, content) => {
      if (err) {
        res.writeHead(500);
        res.end('Error loading styles.css');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.end(content);
      }
    });
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

const port = 3000;
server.listen(port, () => {
  console.log(`Backend is running on port ${port}`);
});
