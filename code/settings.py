from pygame import mixer
from configparser import ConfigParser
import os
from datakit import *

# main font
FONT = os.path.join("font", "RDChulaJaRuek.ttf")
FONT_AWSOME = os.path.join("font", "FontAwsome.ttf")
FONT_ICON = os.path.join("font", "MaterialIcons-Regular.ttf")

# load config file
config = ConfigParser()
config.read(os.path.join('data', 'config.ini'))

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# TILE_SIZE = config.getint('GRAPHIC', 'TILE_SIZE')

# load save file
SAVEPATH = os.path.join('data', 'savefile.sav')

# load sfx file
mixer.init()
SOUND_UISELECT = mixer.Sound(os.path.join('audio', 'sfx', 'ui-selected.mp3'))
SOUND_BTNCLICK = mixer.Sound(os.path.join('audio', 'sfx', 'btn-clicked.wav'))
SOUND_COLLECT = mixer.Sound(os.path.join('audio', 'sfx', 'collected.wav'))
SOUND_CANTCLICK = mixer.Sound(os.path.join('audio', 'sfx', 'ui-cantclick.mp3'))
SOUND_START = mixer.Sound(os.path.join('audio', 'sfx', 'start.mp3'))

#load sound with doubly circular linked list
msc_ingame = MusicList()
msc_ingame.append(SoundNode(os.path.join('audio', 'music', 'Idle Rich 1.mp3')))
msc_ingame.append(SoundNode(os.path.join('audio', 'music', 'Idle Rich 2.mp3')))
msc_ingame.append(SoundNode(os.path.join('audio', 'music', 'Idle Rich 3.mp3')))
msc_ingame.append(SoundNode(os.path.join('audio', 'music', 'Idle Rich 4.mp3')))

msc_menu = MusicList()
msc_menu.append(SoundNode(os.path.join('audio', 'music', 'menu 1.mp3')))
msc_menu.append(SoundNode(os.path.join('audio', 'music', 'menu 2.mp3')))
msc_menu.append(SoundNode(os.path.join('audio', 'music', 'menu 3.mp3')))

