import pygame
from pygame.locals import *
import sys
import pickle
import threading
from settings import *
from slot import *
from powerup import *
from pgui import *
from balance import *

class Options:
    @staticmethod
    def save_config():
        with open(os.path.join('data', 'config.ini'), 'w') as configfile:
            config.write(configfile)
            # config.close()
            
    @staticmethod
    def toggle_fullscreen(state: bool):
        res_code = state
        config.set('GRAPHIC', 'SCREEN_CODE', str(res_code))
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN if config.getboolean("GRAPHIC", "SCREEN_CODE") else 0)
        print('[DEBUG] set fullscreen to ', state)
        Options.save_config()
    
    @staticmethod
    def set_resolution(width, height, code): #FIXME: screen size change but resolution not change
        res_code = code
        config.set('GRAPHIC', 'SCREEN_WIDTH', str(width))
        config.set('GRAPHIC', 'SCREEN_HEIGHT', str(height))
        config.set('GRAPHIC', 'SCREEN_CODE', str(res_code))
        
        pygame.display.set_mode((width, height), pygame.FULLSCREEN if config.getboolean("GRAPHIC", "SCREEN_CODE") else 0)
        
        print(f'[404] set resolution to {width}x{height} with {res_code} mode')
        Options.save_config()
        
    @staticmethod
    def set_sfx_volume(value):
        value = int(value)
        config.set('AUDIO', 'SFX_VOLUME', str(value))
        print('[DEBUG] set sfx volume to ', value)
        Options.save_config()
        
    @staticmethod
    def set_music_volume(value):
        value = int(value)
        config.set('AUDIO', 'MUSIC_VOLUME', str(value))
        print('[DEBUG] set music volume to ', value)
        Options.save_config()
    
    @staticmethod
    def save_ingame_music(obj_index: int, obj: pygame.mixer.Sound):
        config.set('AUDIO', 'MUSIC_INGAME', str(obj_index))
        print('[DEBUG] set ingame music to ', msc_ingame.path(obj_index))
        Options.save_config()
    
    @staticmethod
    def save_menu_music(obj_index: int, obj: pygame.mixer.Sound):
        config.set('AUDIO', 'MUSIC_MENU', str(obj_index))
        print('[DEBUG] set menu music to ', msc_ingame.path(obj_index))
        Options.save_config()
    
    @staticmethod
    def handle_pygame_event(event):
        if event.type == QUIT:
            Options.save_config()
            pygame.quit()
            sys.exit()

class SaveData:   
    @staticmethod
    def save_game(game_data:dict):
        data = {
            "name": "saveffer",
            "balance": game_data["balance"],
            "transactions": {
                "clicked_balance": game_data["clicked_balance"],
                "transactions_history": game_data["transactions_history"],
            },
            "powerup":{
                "hit": game_data.get("hit", 1),
                "income": game_data.get("income", 0),
                "randomincome": game_data.get("randomincome", 0),
                "fastcombo": game_data.get("fastcombo", 0),
                "fastlevel": game_data.get("fastlevel", 0),
                "moneypower": game_data.get("moneypower", 0),
                "incomepower": game_data.get("incomepower", 0),
                "hitpower": game_data.get("hitpower", 0),
                "autolevel": game_data.get("autolevel", 0)
            },
            "slot": {
                "time": game_data.get("time", 0),
                "autospin": game_data.get("autospin", 0),
                "spincost": game_data.get("spincost", 1),
                "slotgain": game_data.get("slotgain", 1)
            }
        }
        
        with open(SAVEPATH, "wb") as save:
            pickle.dump(data, save)    
            save.close()
    
    @staticmethod
    def load_game():
        data = {}
        with open(SAVEPATH, "rb") as save:
            data = pickle.load(save)
            save.close()
        return data

    @staticmethod
    def reset_game():
        data = {
            "name": "saveffer",
            "balance": 0,
            "transactions": {
                "clicked_balance": 0,
                "transactions_history": [],
            },
            "powerup":{
                "hit": 1,
                "income": 0,
                "randomincome": 0,
                "fastcombo": 0,
                "fastlevel": 0,
                "moneypower": 0,
                "incomepower": 0,
                "hitpower": 0,
                "autolevel": 0
            },
            "slot": {
                "time": 0,
                "autospin": 0,
                "spincost": 1,
                "slotgain": 1
            }
        }
        
        with open(SAVEPATH, "wb") as save:
            pickle.dump(data, save)
            save.close()
        
class PlayerSystem:
    def __init__(self):
        self.save_data = SaveData.load_game()
        self.balance = Balance(self.save_data["balance"]) 
        self.clicked_amount = self.save_data["transactions"]["clicked_balance"]
        self.balance.add_balance_by_click(self.clicked_amount)
        self.transactions_history = self.save_data["transactions"]["transactions_history"]
        self.powerup = {
            "hit": Hit(name="hit", type="cost", max_level=80, 
                       description="Increase money per click", cost=1500, 
                       level=self.save_data["powerup"]["hit"]), 
            "income": Income(name="income", type="cost", 
                        description="Auto produce money per second", 
                        cost=3500, level=self.save_data["powerup"]["income"]), 
            "randomincome": RandomIncome(name="randomincome", type="cost", 
                        description="Produce random money per second", cost=50000, 
                        level=self.save_data["powerup"]["randomincome"])            
        }

        self.slot = self.save_data["slot"]

        self.update_save()
    
        if len(self.transactions_history) > 0:
            for transaction in self.transactions_history:
                self.balance.add_transaction(transaction["amount"], transaction["detail"], transaction["date"])
        else:
            print("[DEBUG] No transaction history found pass this stage")
        
        self.transactions_history = self.balance.transactions.all_transactions
        
    def update_save(self):
        self.clicked_amount = self.balance.clicked_balance
        self.save = {
                "balance": self.balance.get_balance(),
                "clicked_balance": self.clicked_amount,
                "transactions_history": self.transactions_history,
                "hit": self.powerup["hit"].level,
                "income": self.powerup["income"].level,
                "randomincome": self.powerup["randomincome"].level,
                "fastcombo": self.powerup.get("fastcombo", 0),
                "fastlevel": self.powerup.get("fastlevel", 0),
                "moneypower": self.powerup.get("moneypower", 0),
                "incomepower": self.powerup.get("incomepower", 0),
                "hitpower": self.powerup.get("hitpower", 0),
                "autolevel": self.powerup.get("autolevel", 0),
                "time": self.slot.get("time", 0),
                "autospin": self.slot.get("autospin", 0),
                "spincost": self.slot.get("spincost", 1),
                "slotgain": self.slot.get("slotgain", 1)
        }
        
        savegame_args = (self.save,) 
        savegame_th = threading.Thread(target=SaveData.save_game, args=savegame_args)
        # savegame_th.daemon = True
        savegame_th.start()
        savegame_th.join()

if __name__ == "__main__":
    raise Exception('This is not a standalone file, please run main.py instead')
    