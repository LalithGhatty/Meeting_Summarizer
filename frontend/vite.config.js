import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ command }) => ({
  plugins: [react()],
  root: '.',
  server: {
    port: 3000,
    proxy:
      command === 'serve'
        ? {
            '/api': {
              target: 'http://localhost:8000',
              changeOrigin: true,
              rewrite: (path) => path.replace(/^\/api/, ''),
            },
          }
        : undefined, // disable proxy during build on Render
  },
  build: {
    outDir: 'dist',
  },
}))
