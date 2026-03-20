/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#0a0a0a',
        surface: '#141414',
        'surface-hover': '#1a1a1a',
        border: '#222222',
        text: '#e8e8e8',
        'text-muted': '#999999',
        accent: '#c4a265',
        'accent-dim': 'rgba(196,162,101,0.12)',
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
