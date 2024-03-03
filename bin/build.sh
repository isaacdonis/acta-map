echo "build.sh --- bundling vite files"
(cd mainmap/static_src && npm install && npm run build)
echo "build.sh -- done!"
