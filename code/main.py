import pygame
import sys
from settings import *
from gamestate import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN if config.getint('GRAPHIC', 'SCREEN_CODE') == 0 else 0)
        self.title = pygame.display.set_caption('Idle Rich')
        self.icon = pygame.image.load('assets/tired.png')
        pygame.display.set_icon(self.icon)

        self.states = {
            'main_menu': MainMenu(self),
            'pause_menu': PauseMenu(self),
            'option_menu': OptionMenu(self),
            'game_play': GamePlay(self)
        }
        self.current_state = 'main_menu'
        self.prev_state = None

    def change_state(self, new_state):
        if new_state in self.states:
            self.prev_state = self.current_state
            self.current_state = new_state
            
    def run(self):
        while True:
            events = pygame.event.get()
            
            # Handle events and update/render the current state
            self.states[self.current_state].handle_events(events)
            self.states[self.current_state].update()
            self.states[self.current_state].render()
            
if __name__ == '__main__':
    game = Game()
    game.run()