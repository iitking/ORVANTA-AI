/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./dashboard/**/*.{js,ts,jsx,tsx,mdx}",
    "./ai-chat/**/*.{js,ts,jsx,tsx,mdx}",
    "./integrations/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "hsl(222.2 84% 4.9%)",
        foreground: "hsl(210 40% 98%)",
        card: "hsl(222.2 84% 6.5%)",
        primary: "hsl(217.2 91.2% 59.8%)",
      },
    },
  },
  plugins: [],
}
