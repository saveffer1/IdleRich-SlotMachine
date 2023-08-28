import pygame
from pygame.locals import *
import sys
from settings import *
from pgui import *
from game import *

class OptionMenu: #TODO: Work in progress
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.display_info = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.mouse_clicked = False
        
    def set_sfx_volume(self, value):
        value = int(value)
        config.set('AUDIO', 'SFX_VOLUME', str(value))
        print('[DEBUG] set sfx volume to ', value)
        MainGame.save_config()
    
    def set_music_volume(self, value):
        value = int(value)
        config.set('AUDIO', 'SFX_VOLUME', str(value))
        print('[DEBUG] set music volume to ', value)
        MainGame.save_config()
    
    def draw_option_btn(self, text, font:str=None, width:int=250, height:int=50, x:int=0, y:int=0, border:int=12):
            if font == None:
                font = FONT
            else:
                font = font
            btn = Button(
                    text=text, 
                    font=font,
                    font_size=35,
                    width=width, height=height, 
                    x=x, y=y, 
                    border=border
                )
            btn.top_color = "#83502E"
            btn.bottom_color = "#342012"
            btn.set_hover(color='#D74B4B')
            btn.set_elevate(elevation=5)
            btn.draw()
            return btn
    
    def open(self):
        rt_width = pygame.display.Info().current_w
        rt_height = pygame.display.Info().current_h
        
        music_slider = RangeSlider(min_value=0, max_value=100, start_value=config.getint('AUDIO', 'MUSIC_VOLUME'), x=rt_width//2, y=rt_height//2-130, button_color=(255, 255, 255), range_width=200, font_color="#FFFFFF", show_min_max=False, call_func=self.set_music_volume)
        sfx_slider = RangeSlider(min_value=0, max_value=100, start_value=config.getint('AUDIO', 'SFX_VOLUME'), x=rt_width//2, y=rt_height//2-70, button_color=(255, 255, 255), range_width=200, font_color="#FFFFFF", show_min_max=False, call_func=self.set_sfx_volume)
        while True:
            rt_height = pygame.display.Info().current_h
            rt_width = pygame.display.Info().current_w
            
            self.surface.fill((217,189,165))
            option_rect = pygame.Rect(rt_width//4, rt_height//4, rt_width//2, rt_height//2)            
            option_surf = pygame.Surface(option_rect.size, pygame.SRCALPHA)
            pygame.draw.rect(option_surf, (0, 0, 0, 128), option_surf.get_rect())
            self.surface.blit(option_surf, option_rect)
            
            option_label = Label('Options', font=FONT, font_size=60, color=(0, 0, 0), x=rt_width//2-100, y=rt_height//2-300)
            option_label.draw()
            music_label = Label('Music Volume', font=FONT, font_size=30, color=(255, 255, 255), x=rt_width//2-250, y=rt_height//2-160)
            music_label.draw()
            sfx_label = Label('SFX Volume', font=FONT, font_size=30, color=(255, 255, 255), x=rt_width//2-250, y=rt_height//2-100)
            sfx_label.draw()
            
            btn_back = self.draw_option_btn('Back', x=50, y=rt_height//2-300, width=150, height=50)
            btn_delsave = self.draw_option_btn('\uf2ed', font=FONT_AWSOME, x=50, y=rt_height//2-200, width=150, height=50)
            
            self.mouse_clicked = False
            for event in pygame.event.get():
                MainGame.handle_pygame_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_clicked = True
                    if btn_delsave.clicked():
                        pass
                    if btn_back.clicked():
                        return
                # Call the handle_event method for each event
                sfx_slider.handle_event(event)
                music_slider.handle_event(event)
    
            # Update the slider appearance
            music_slider.draw()
            sfx_slider.draw()
        
            # pygame.display.update()
            pygame.display.flip()
            # self.clock.tick(self.fps)
       
class PauseMenu:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.display_info = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.mouse_clicked = False
    
    def open(self):
        def draw_pause_btn(text, width:int=250, height:int=50, x:int=0, y:int=0, border:int=12):
            btn = Button(
                    text=text, 
                    font=FONT,
                    font_size=35,
                    width=width, height=height, 
                    x=x, y=y, 
                    border=border
                )
            btn.top_color = "#475F77"
            btn.bottom_color = "#354B5E"
            btn.set_hover(color='#D74B4B')
            btn.set_elevate(elevation=5)
            btn.draw()
            return btn
        while True:
            rt_width = pygame.display.Info().current_w
            rt_height = pygame.display.Info().current_h
            
            self.screen.fill((0,0,0))
            menutext = Label('pause menu', font=FONT, font_size=60, 
                             color=(255, 255, 255), x=20, y=20
                        )
            menutext.draw()
            
            btn_resume = draw_pause_btn('Resume', x=rt_width//2, y=rt_height//2, width=250, height=50)
            btn_option = draw_pause_btn('Options', x=rt_width//2, y=rt_height//2+100, width=250, height=50)
            btn_main_menu = draw_pause_btn('Main Menu', x=rt_width//2, y=rt_height//2+200, width=250, height=50)
            
            self.mouse_clicked = False
            for event in pygame.event.get():
                MainGame.handle_pygame_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_clicked = True
                        if btn_resume.clicked():
                            return
                        if btn_option.clicked():
                            self.option_menu()
                        if btn_main_menu.clicked():
                            self.main_menu()
        
            pygame.display.update()
            # self.clock.tick(self.fps)

class CreditMenu: #TODO: Work in progress
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.display_info = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.mouse_clicked = False
    
    def open(self):
        while True:
            self.surface.fill((0,0,0))
            menutext = Label('Credit', font=FONT, font_size=60, 
                             color=(255, 255, 255), x=20, y=20
                        )
            if menutext.clicked():
                menutext.text = 'saveffer join!'
            menutext.draw()
            
            self.mouse_clicked = False
            for event in pygame.event.get():
                MainGame.handle_pygame_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_clicked = True
        
            pygame.display.update()
            # self.clock.tick(self.fps)
    
class MainMenu:
    def __init__(self, fps: int = 60):
        self.display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, pygame.FULLSCREEN if config.getint('GRAPHIC', 'SCREEN_CODE') == 0 else 0)
        self.game_logo = pygame.image.load('assets/logo.png')
        self.background = pygame.image.load('assets/background.png')
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.mouse_clicked = False
        self.game = MainGame()
        self.option_menu = OptionMenu()
        self.pause_menu = PauseMenu()
        self.credit_menu = CreditMenu()
    
    def pause(self):
        self.pause_menu.open()
    
    def option(self):
        self.option_menu.open()
    
    def credit(self):
        self.credit_menu.open()
    
    def main_menu(self): #TODO: Add new background, decorate menu
        def draw_menu_btn(text, width:int=250, height:int=50, x:int=0, y:int=0, border:int=12):
            btn = Button(
                    text=text, 
                    font=FONT,
                    font_size=35,
                    width=width, height=height, 
                    x=x, y=y, 
                    border=border
                )
            btn.top_color = "#475F77"
            btn.bottom_color = "#354B5E"
            btn.set_hover(color='#D74B4B')
            btn.set_elevate(elevation=5)
            btn.draw()
            return btn
            
        while True:
            rt_width = pygame.display.Info().current_w
            rt_height = pygame.display.Info().current_h
            
            self.screen.fill((0,0,0))
            self.screen.blit(pygame.transform.scale(self.background, (rt_width, rt_height)), (0, 0))
            menutext = Label('main menu', font=FONT, font_size=60, 
                             color=(255, 255, 255), x=20, y=20
                        )
            menutext.draw()

            btn_play = draw_menu_btn('Play', x=rt_width-400, y=200, width=250, height=50)
            btn_option = draw_menu_btn('Options', x=rt_width-400, y=300, width=250, height=50)
            btn_credit = draw_menu_btn('Credit', x=rt_width-400, y=400, width=250, height=50)
            btn_exit = draw_menu_btn('Exit', x=rt_width-400, y=500, width=250, height=50)
            
            self.mouse_clicked = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pass
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_clicked = True
                        if btn_play.clicked():
                            self.main_game()
                        if btn_option.clicked():
                            self.option()
                        if btn_credit.clicked():
                            self.credit()
                        if btn_exit.clicked():
                            pygame.quit()
                            sys.exit()
            
            pygame.display.update()
            self.clock.tick(self.fps)
    
    def main_game(self):
        self.game.start(self.clock)
