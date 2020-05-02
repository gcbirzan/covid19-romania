module.exports = {
    devServer: {
        compress: true,
        disableHostCheck: true,
        proxy: 'http://192.168.88.23:8000/'

    },

    pluginOptions: {
        webpackBundleAnalyzer: {
            openAnalyzer: false
        }
    },
    configureWebpack: {
        devtool: 'source-map'
    }
}