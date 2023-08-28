import pygame
from pygame.locals import *
import sys
from settings import *
from menu import*
        
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, pygame.FULLSCREEN if config.getint('GRAPHIC', 'SCREEN_CODE') == 0 else 0)
        self.title = pygame.display.set_caption('Idle Rich')
        self.icon = pygame.image.load('assets/tired.png')
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()
            
    def run(self):
        self.main_menu.main_menu()
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()