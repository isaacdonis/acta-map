from .base import *

# re-state it again because you can never be too sure.
DEBUG = False

LOGGING["handlers"]["console"] = {
    "class": "logging.StreamHandler",
}

DJANGO_VITE_DEV_MODE = False
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
DJANGO_VITE_ASSETS_PATH = BASE_DIR / ".." / "mainmap" / "static" / "js" / "dist"
STATICFILES_DIRS = [BASE_DIR.parent / "mainmap/static/mainmap", DJANGO_VITE_ASSETS_PATH]
DJANGO_VITE = {
    "default": {
        "manifest_path": DJANGO_VITE_ASSETS_PATH / "manifest.json",
    }
}

# enforce https
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
