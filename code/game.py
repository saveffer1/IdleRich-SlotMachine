import pygame
from pygame.locals import *
import sys
import pickle
from collections import deque
from settings import *
from slot import *
from powerup import *
from pgui import *
from balance import *

class SaveData:
    def __init__(self):
        with open(SAVEPATH, 'rb') as save:
            self.data = pickle.load(save)
            save.close()
    
    @staticmethod
    def save_game(game_data:dict):
        data = {
            "name": "saveffer",
            "balance": game_data["balance"],
            "clicked_count": game_data["clicked_count"],
            "transactions": {
                "clicked_balance": game_data["clicked_balance"],
                "transactions_history": game_data["transactions_history"],
            }
        }
        
        with open(SAVEPATH, "wb") as save:
            pickle.dump(data, save)    
    
    @staticmethod
    def load_game():
        with open(SAVEPATH, "rb") as save:
            data = pickle.load(save)
            save.close()
        return data
        
class PlayerSystem:
    def __init__(self):
        self.save_data = SaveData()
        self.balance = Balance(self.save_data.data["balance"])
        self.clicked_count = self.save_data.data["clicked_count"]
        self.clicked_amount = self.save_data.data["transactions"]["clicked_balance"]
        self.transactions_history = self.save_data.data["transactions"]["transactions_history"]

        for transaction in self.transactions_history:
            self.balance.add_transaction(transaction["amount"], transaction["detail"], transaction["date"])
            
class MainGame:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.mouse_clicked = False
        self.game_data = None
        self.loading = True
        self.load_game()
    
    def load_game(self):
        self.game_data = PlayerSystem()
        self.loading = False
    
    @staticmethod
    def save_config():
        with open(os.path.join('data', 'config.ini'), 'w') as configfile:
            config.write(configfile)
    
    @staticmethod
    def set_resolution(width, height, code): #FIXME: screen size change but resolution not change
        """save resolution to config.ini
        Args:
            code (_int_): _Set resolution to 'fullscreen' if code is equal 0 else set to 'windowed'_
        """
        res_code = code
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
            if self.loading:
                font = pygame.font.Font(None, 36)
                text = font.render("Loading...", True, (255, 255, 255))
                text_rect = text.get_rect(center=(400, 300))
                self.surface.blit(text, text_rect)
            else:
                font = pygame.font.Font(None, 36)
                text = font.render("Game is ready!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(400, 300))
                self.surface.blit(text, text_rect)

            for event in pygame.event.get():
                self.handle_pygame_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return 1
            pygame.display.update()
