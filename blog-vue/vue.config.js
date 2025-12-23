



const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, '../blog/static/vue'), // built files go here
  indexPath: path.resolve(__dirname, '../blog/templates/index.html'), // HTML goes here
  publicPath: '/', 
  transpileDependencies: true,
};