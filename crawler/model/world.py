import configparser

config = configparser.ConfigParser()
config.read('config.ini')

GOOGLE_API_KEY = config.get('API_KEYS', 'GOOGLE_API_KEY')