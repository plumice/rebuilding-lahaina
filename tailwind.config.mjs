/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#ffffff',
        surface: '#f7f7f5',
        'surface-hover': '#eeeeec',
        border: '#e0e0de',
        text: '#1a1a1a',
        'text-muted': '#555555',
        accent: '#6d5344',
        'accent-dim': 'rgba(109,83,68,0.08)',
      },
      fontFamily: {
        serif: ['"EB Garamond"', 'Georgia', 'serif'],
        sans: ['Inter', '-apple-system', 'sans-serif'],
      },
      fontSize: {
        'min': '0.8rem',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
