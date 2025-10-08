// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })


const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, '../blog/static'), // where built JS/CSS go
  indexPath: path.resolve(__dirname, '../blog/templates/index.html'), // where built HTML goes
  publicPath: '/static/', // make all asset URLs work with Django’s static handling
  transpileDependencies: true,
};
