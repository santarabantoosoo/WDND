const proxy = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(proxy('/books', { target: 'http://127.0.0.1:5000/' }));
};