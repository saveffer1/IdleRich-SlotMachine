import pygame
from pygame.locals import *
import sys
from settings import *
from balance import *
from slot import *
from powerup import *
from pgui import *

class MainGame:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.mouse_clicked = False
    
    @staticmethod
    def save_config():
        with open(os.path.join('data', 'config.ini'), 'w') as configfile:
            config.write(configfile)
    
    @staticmethod
    def set_resolution(width, height, code): #FIXME: screen size change but resolution not change
        """save resolution to config.ini

        Args:
            value (_type_): _description_
            width (_type_): _description_
            height (_type_): _description_
        """
        res_code = code #'fullscreen' if code == 0 else 'windowed'
        config.set('GRAPHIC', 'SCREEN_WIDTH', str(width))
        config.set('GRAPHIC', 'SCREEN_HEIGHT', str(height))
        config.set('GRAPHIC', 'SCREEN_CODE', str(res_code))
        
        pygame.display.set_mode((width, height), pygame.RESIZABLE, pygame.FULLSCREEN if config.getint('GRAPHIC', 'SCREEN_CODE') == 0 else 0)
        
        print(f'[404] set resolution to {width}x{height} with {res_code} mode')
        MainGame.save_config()

    @staticmethod
    def handle_pygame_event(event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            width, height = event.size
            if width < 1270 or height < 720:
                width = 1270
                height = 720
            MainGame.set_resolution(width, height, 1)
    
    def start(self, dt):
        while True:
            self.surface.fill((0, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return 1