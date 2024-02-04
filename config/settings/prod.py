from .base import *

# re-state it again because you can never be too sure.
DEBUG = False

LOGGING["handlers"]["console"] = {
    "class": "logging.StreamHandler",
}
