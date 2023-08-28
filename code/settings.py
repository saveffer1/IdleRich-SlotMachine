from pygame.math import Vector2
from configparser import ConfigParser
import os

# main font
FONT = "font/RDChulaJaRuek.ttf"
FONT_AWSOME = "font/FontAwsome.ttf"

# load config file
config = ConfigParser()
config.read(os.path.join('data', 'config.ini'))

# screen
SCREEN_WIDTH = config.getint('GRAPHIC', 'SCREEN_WIDTH')
SCREEN_HEIGHT = config.getint('GRAPHIC', 'SCREEN_HEIGHT')
# TILE_SIZE = config.getint('GRAPHIC', 'TILE_SIZE')
