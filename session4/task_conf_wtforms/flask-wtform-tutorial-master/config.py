"""App configuration."""
from os import environ, path

from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
# TODO load the .env file

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    # TODO add secret key
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
