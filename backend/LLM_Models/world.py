import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
config.read(config_path)

GOOGLE_API_KEY = config.get('API_KEYS', 'GOOGLE_API_KEY')