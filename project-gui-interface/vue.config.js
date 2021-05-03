module.exports = {
	devServer: {
		proxy: 'http://localhost:8888',
		overlay: false,
	},
	transpileDependencies: ['vuetify'],
};
