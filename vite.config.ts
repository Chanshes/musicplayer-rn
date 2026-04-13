import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    // 启用生产环境优化
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    },
    // 启用代码分割
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router', 'vuex'],
          common: ['@vue/runtime-core']
        }
      }
    },
    // 启用sourcemap（可选）
    sourcemap: false
  },
  // 开发服务器配置
  server: {
    port: 3000,
    open: true
  }
});