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
        'text-muted': '#6b6b6b',
        accent: '#8b7355',
        'accent-dim': 'rgba(139,115,85,0.08)',
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
