import { resolve } from "path";

export default {
  plugins: [],
  root: resolve("./src"),
  base: "/static/",
  envDir: "../../../",
  resolve: {
    extensions: [".js"]
  },
  build: {
    sourcemap: false,
    outDir: resolve("../static/js/dist"),
    assetsDir: "",
    manifest: "manifest.json",
    emptyOutDir: true,
    target: "es2020",
    rollupOptions: {
      input: {
        map: resolve("./src/map.js"),
      },
      output: {
        chunkFileNames: undefined
      }
    }
  },
};
