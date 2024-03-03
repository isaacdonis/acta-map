SCRIPT_DIRECTORY="$(dirname "$0")"

npx tailwindcss -c $SCRIPT_DIRECTORY/../tailwind.config.js \
  -i $SCRIPT_DIRECTORY/../mainmap/static/mainmap/css/base.css \
  -o $SCRIPT_DIRECTORY/../mainmap/static/mainmap/css/tailwind-out.css --watch
