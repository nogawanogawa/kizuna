module.exports = {
  configureWebpack: {
    devServer: {
      watchOptions: {
        poll: true
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}