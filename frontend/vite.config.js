import { sveltekit } from '@sveltejs/kit/vite';
//import { nodeLoaderPlugin } from '@vavite/node-loader/plugin';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	optimizeDeps: { exclude: ["fsevents"] },
	ssr: { noExternal: ['@popperjs/core'] }

});
// /** @type {import('vite').UserConfig} */
// export default defineConfig(({ mode }) => {
//     let plugins = [sveltekit()];
//     if (mode === 'development') {
//         plugins = [nodeLoaderPlugin(), ...plugins];
//     }

//     return {
//         // ... your code ...
//         plugins
//     };
// });