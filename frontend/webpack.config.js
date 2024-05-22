// webpack.config.js
module.exports = {
    devServer: {
      host: '0.0.0.0',
      port: 9000, // hoặc cổng mà bạn muốn sử dụng
    },
    rules: [
      {
        test: /\.module\.css$/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: true
            }
          }
        ]
      },
      // Cấu hình khác...
    ]
  }
  