import { defineConfig } from 'astro/config';
import tailwindcss from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://rebuildinglahaina.org',
  integrations: [tailwindcss(), sitemap()],
  output: 'static',
});
