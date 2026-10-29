import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  server: { host: true },
  output: 'static',

  vite: {
    plugins: [tailwindcss()],
  },
});