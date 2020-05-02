module.exports = {
    devServer: {
        compress: true,
        disableHostCheck: true,
        // proxy: 'http://192.168.88.23:8000/'
        proxy: 'https://covid19.bitofdata.ro/'

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