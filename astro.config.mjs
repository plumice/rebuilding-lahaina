import { defineConfig } from 'astro/config';
import tailwindcss from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://rebuilding-lahaina.netlify.app',
  integrations: [tailwindcss(), sitemap()],
  output: 'static',
});
