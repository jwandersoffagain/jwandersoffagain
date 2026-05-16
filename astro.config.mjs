import { defineConfig } from 'astro/config';

import cloudflare from "@astrojs/cloudflare";

export default defineConfig({
  site: 'https://jwandersoffagain.pages.dev',
  output: 'static',
  adapter: cloudflare()
});