require('dotenv').config();
const dns = require('dns');
const express = require('express');
const cors = require('cors');
const crypto = require('crypto');
const bodyParser = require('body-parser');
require('url'); 
const app = express();

// Basic Configuration
const port = process.env.PORT || 3000;

const url_mapping = {}

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.post('/api/shorturl', function(req, res, next) {
  const urlObject = new URL(req.body.url);
  dns.lookup(urlObject.hostname, function(err, _) {
    if (err) res.json({
      'error': 'invalid url'
    })

    next()
  })}, function(req, res) {
  const short_url = crypto.createHash('md5').update(req.body.url).digest('hex')
  url_mapping[short_url] = req.body.url

  res.json({
    'original_url': req.body.url,
    'short_url': short_url
  })
});

app.get('/api/shorturl/:short_url', function(req, res) {
  if (Object.keys(url_mapping).includes(req.params.short_url)) {
    res.redirect(url_mapping[req.params.short_url])
  } else {
    res.json({
      'error': 'invalid url'
    })
  }
})

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
