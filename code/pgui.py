import pygame
from pygame import gfxdraw

class Label:
    def __init__(self, text, font:str=None, font_size:int=30, color:str|tuple='#FFFFFF', x:int=0, y:int=0):
        self.surface = pygame.display.get_surface()
        self.text = text
        self.font = font
        self.color = color
        self.pos_x = x
        self.pos_y = y
        
        self.pressed = False
        
        self.font_size = font_size
        if font == None:
            self.font = pygame.font.SysFont('Arial', 30)
        else:
            self.font = pygame.font.Font(font, font_size)
    
    def rect(self):
        textobj = self.font.render(self.text, 1, self.color)
        textrect = textobj.get_rect()
        textrect.topleft = (self.pos_x, self.pos_y)
        return textobj, textrect
    
    def draw(self):
        textobj, textrect = self.rect()
        self.surface.blit(textobj, textrect)
    
    def is_collided(self):
        textobj, textrect = self.rect()
        if textrect.collidepoint(pygame.mouse.get_pos()):
            return True
        
    def clicked(self) -> bool:
        if self.is_collided() and pygame.mouse.get_pressed()[0] and not self.pressed:
            self.pressed = True
        else:
            self.pressed = False
        return self.pressed

class Button():
    def __init__(self, text, font:str=None, font_size:int=30, width:int=250, height:int=50, x:int=0, y:int=0,  border: int=12):
        self.surface = pygame.display.get_surface()
        
        # self.pressed = False

        self.rect = pygame.Rect(x, y, width, height)
        self.top_rect = self.rect.copy()
        self.bottom_rect = self.rect.copy()
        
        self.border = border
        self.elevation = 0
        self.dynamic_elevation = 0
        
        self.top_color = '#475F77'
        self.top_color_hover = '#D74B4B'
        self.t_color_state = self.top_color
        self.bottom_color = '#354B5E'
        
        self.text = text
        self.font_size = font_size
        if font == None:
            self.font = pygame.font.SysFont('Arial', 30)
        else:
            self.font = pygame.font.Font(font, font_size)
        self.text_surf = self.font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    def draw(self):
        self.top_rect.y = self.rect.y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(self.surface, self.bottom_color, self.bottom_rect, border_radius=self.border)
        pygame.draw.rect(self.surface, self.t_color_state, self.top_rect, border_radius=self.border)
        
        self.surface.blit(self.text_surf, self.text_rect)
    
    def is_collided(self) -> bool:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    def clicked(self) -> bool:
        mouse_press = pygame.mouse.get_pressed()[0]
        pressed = False
        if self.is_collided() and mouse_press and not pressed:
            pressed = True
        else:
            pressed = False
        return pressed
    
    def set_hover(self, color: str | tuple = '#D74B4B'):
        self.top_color_hover = color
        if self.is_collided():
            self.t_color_state = self.top_color_hover
        else:
            self.t_color_state = self.top_color
    
    def set_elevate(self, elevation: int = 5):
        self.elevation = elevation
        if self.clicked():
            self.dynamic_elevation = 0
        else:
            self.dynamic_elevation = self.elevation

class RangeSlider:
    def __init__(self, min_value: int=0, max_value: int=100,
                 start_value:int=None, x: int=10, y: int=10, 
                 range_width: int=700, range_height: int=20,
                 range_color: str | tuple = '#000000',
                 button_size: int=20, button_color: str | tuple = '#FF0000',
                 font: str=None, font_size: int=30, font_color: str | tuple='#000000',
                 show_min_max: bool=True, callback=None
        ):
        self.surface = pygame.display.get_surface()
        self.callback = callback
        
        self.dragging = False
        
        self.min_value = min_value
        self.max_value = max_value
        
        self.x = x
        self.y = y
        
        self.range_width = range_width
        self.range_height = range_height
        self.range_color = range_color
        
        self.button_size = button_size
        self.button_color = button_color
        
        self.font_size = font_size
        self.font_color = font_color
        if font is None:
            self.font = pygame.font.SysFont('Arial', font_size)
        else:
            self.font = pygame.font.Font(font, font_size)
        
        self.show_min_max = show_min_max
        
        # Calculate initial thumb position based on start_value
        if start_value is not None:
            self.value = start_value
            self.thumb_position = self.x + int((start_value - min_value) / (max_value - min_value) * range_width)
        else:
            self.value = min_value
            self.thumb_position = x

    def draw(self):
        pygame.draw.rect(self.surface, self.range_color, (self.x, self.y - self.range_height // 2, self.range_width, self.range_height))
        pygame.draw.circle(self.surface, self.button_color, (self.thumb_position, self.y), self.button_size // 2)

        if self.show_min_max:
            min_label = self.font.render(str(self.min_value), True, self.font_color)
            max_label = self.font.render(str(self.max_value), True, self.font_color)
            min_label_width = min_label.get_width()
            max_label_width = max_label.get_width()
            self.surface.blit(min_label, (self.x - min_label_width // 2, self.y + 20))
            self.surface.blit(max_label, (self.x + self.range_width - max_label_width // 2, self.y + 20))
        
        if self.dragging:
            value_label = self.font.render(str(self.value), True, self.font_color)
            value_label_width = value_label.get_width()
            value_label_height = value_label.get_height()

            label_y = self.y - self.range_height // 2 - value_label_height - 5
            self.surface.blit(value_label, (self.thumb_position - value_label_width // 2, label_y))

    def update(self):
        if self.dragging:
            self.thumb_position = min(max(pygame.mouse.get_pos()[0], self.x), self.x + self.range_width)
            self.value = int((self.thumb_position - self.x) / self.range_width * (self.max_value - self.min_value) + self.min_value)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.thumb_position - self.button_size // 2 <= mouse_x <= self.thumb_position + self.button_size // 2 and self.y - self.button_size // 2 <= mouse_y <= self.y + self.button_size // 2:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = False
            if self.callback:
                self.callback(self.value)

class ToggleSwitch:
    def __init__(self, x, y, width, height, start_state:bool=False, state_text:bool=False, font: str=None, font_size: int=30, callback=None):
        self.surface = pygame.display.get_surface()
        self.rect = pygame.Rect(x, y, width, height)
        
        self.text_color = "#000000"
        self.text_on_color = "#000000"
        self.text_off_color = "#000000"
        self.on_color = "#00FF00"
        self.off_color = "#FF0000"
        self.circle_color = "#FFFFFF"
        self.text_on = "ON"
        self.text_off = "OFF"
        self.state_text = state_text
        
        self.circle_direction = 25

        self.is_on = start_state
        if self.is_on:
            self.circle_x = self.rect.x + self.rect.width - self.circle_direction
        else:
            self.circle_x = self.rect.x + self.circle_direction
        
        self.callback = callback
        
        if font is None:
            self.font = pygame.font.SysFont('Arial', font_size)
        else:
            self.font = pygame.font.Font(font, font_size)

    def draw(self):
        # draw on off centered on the switch
        if self.state_text:
            state_label = self.text_on if self.is_on else self.text_off
            state_surface = self.font.render(state_label, True, self.text_on_color if self.is_on else self.text_off_color)
            state_rect = state_surface.get_rect(center=self.rect.center)
            self.surface.blit(state_surface, state_rect)
        
        # Draw the switch background
        pygame.draw.rect(self.surface, self.on_color if self.is_on else self.off_color, self.rect, border_radius=self.rect.height // 2)
        
        # Draw the circle indicator
        # pygame.draw.circle(self.surface, self.circle_color, (self.circle_x, self.rect.y + self.rect.height // 2), self.rect.height // 2 - 2)
        gfxdraw.filled_circle(self.surface, self.circle_x, self.rect.y + self.rect.height // 2, self.rect.height // 2 - 2, pygame.Color(self.circle_color))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_on = not self.is_on
                if self.callback:
                    self.callback(self.is_on)
                self.circle_x = self.rect.x + self.rect.width - self.circle_direction if self.is_on else self.rect.x + self.circle_direction