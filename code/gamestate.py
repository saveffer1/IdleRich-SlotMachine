import pygame #line:1
from pygame .locals import *#line:2
from pygame import mixer #line:3
import sys #line:4
import math #line:5
import random #line:6
import time #line:7
from settings import *#line:8
from pgui import *#line:9
from system import *#line:10
class GameState :#line:12
    def __init__ (OO0OO00000O0O0O0O ,OO0000OO00OO000O0 ):#line:13
        OO0OO00000O0O0O0O .game =OO0000OO00OO000O0 #line:14
        OO0OO00000O0O0O0O .surface =pygame .display .get_surface ()#line:15
        OO0OO00000O0O0O0O .display_info =pygame .display .Info ()#line:16
        OO0OO00000O0O0O0O .surf_width =OO0OO00000O0O0O0O .display_info .current_w #line:17
        OO0OO00000O0O0O0O .surf_height =OO0OO00000O0O0O0O .display_info .current_h #line:18
        OO0OO00000O0O0O0O .clock =pygame .time .Clock ()#line:19
        OO0OO00000O0O0O0O .fps =60 #line:20
        OO0OO00000O0O0O0O .mouse_clicked =False #line:21
    def draw_btn (O0O00000OO00O000O ,O0O0000000OO0OOO0 ,font :str =None ,font_size :int =35 ,width :int =250 ,height :int =50 ,x :int =0 ,y :int =0 ,border :int =12 ):#line:23
            if font ==None :#line:24
                font =FONT #line:25
            else :#line:26
                font =font #line:27
            O0O00OO0OOOOO0000 =Button (text =O0O0000000OO0OOO0 ,font =font ,font_size =font_size ,width =width ,height =height ,x =x ,y =y ,border =border )#line:35
            O0O00OO0OOOOO0000 .top_color ="#475F77"#line:36
            O0O00OO0OOOOO0000 .bottom_color ="#354B5E"#line:37
            return O0O00OO0OOOOO0000 #line:38
    def handle_events (OO0OOOO00OO00O000 ,OO0O000000OOO0OOO ):#line:40
        pass #line:41
    def update (O000O0OOO00000OO0 ):#line:43
        O000O0OOO00000OO0 .display_info =pygame .display .Info ()#line:44
        O000O0OOO00000OO0 .surf_width =O000O0OOO00000OO0 .display_info .current_w #line:45
        O000O0OOO00000OO0 .surf_height =O000O0OOO00000OO0 .display_info .current_h #line:46
        O000O0OOO00000OO0 .mouse_clicked =False #line:47
    def render (O00O00O000O0OO0OO ):#line:49
        pass #line:50
    def play_sound (O00OO000OO0OOOOOO ,OO0O0O0OOOO00O0O0 :str ,O0OOOOO000000000O :str ):#line:52
        try :#line:53
            mixer .music .load (OO0O0O0OOOO00O0O0 )#line:54
            if O0OOOOO000000000O .lower ()=="music":#line:55
                mixer .music .set_volume (config .getint ("AUDIO","MUSIC_VOLUME")*0.01 )#line:56
            elif O0OOOOO000000000O .lower ()=="sfx":#line:57
                mixer .music .set_volume (config .getint ("AUDIO","SFX_VOLUME")*0.01 )#line:58
            else :#line:59
                raise ValueError ("Invalid sound type only 'music' or 'sfx'")#line:60
        except :#line:61
            raise FileNotFoundError ("Sound file not found or invalid file type")#line:62
        mixer .music .play ()#line:63
class MainMenu (GameState ):#line:65
    def __init__ (O0O00O0OO0OOO0O00 ,OO000O000O0000O0O ):#line:66
        super ().__init__ (OO000O000O0000O0O )#line:67
        O0O00O0OO0OOO0O00 .background =pygame .image .load ('assets/background.png')#line:70
        O0O00O0OO0OOO0O00 .menutext =Label ('Idle Rich',font =FONT ,font_size =60 ,text_color =(255 ,255 ,255 ),x =O0O00O0OO0OOO0O00 .surf_width -420 ,y =80 )#line:73
        O0O00O0OO0OOO0O00 .btn_play =O0O00O0OO0OOO0O00 .draw_btn ('Play',x =O0O00O0OO0OOO0O00 .surf_width -410 ,y =200 ,width =250 ,height =50 )#line:76
        O0O00O0OO0OOO0O00 .btn_option =O0O00O0OO0OOO0O00 .draw_btn ('Options',x =O0O00O0OO0OOO0O00 .surf_width -410 ,y =300 ,width =250 ,height =50 )#line:77
        O0O00O0OO0OOO0O00 .btn_credit =O0O00O0OO0OOO0O00 .draw_btn ('Credit',x =O0O00O0OO0OOO0O00 .surf_width -410 ,y =400 ,width =250 ,height =50 )#line:78
        O0O00O0OO0OOO0O00 .btn_exit =O0O00O0OO0OOO0O00 .draw_btn ('Exit',x =O0O00O0OO0OOO0O00 .surf_width -410 ,y =500 ,width =250 ,height =50 )#line:79
        O0O00O0OO0OOO0O00 .all_btn =(O0O00O0OO0OOO0O00 .btn_play ,O0O00O0OO0OOO0O00 .btn_option ,O0O00O0OO0OOO0O00 .btn_credit ,O0O00O0OO0OOO0O00 .btn_exit )#line:81
    def handle_events (O00OOO0O00O000OOO ,O0OO0O00OO0000000 ):#line:83
        O00OOO0O00O000OOO .menutext =Label ('Idle Rich',font =FONT ,font_size =60 ,text_color =(255 ,255 ,255 ),x =O00OOO0O00O000OOO .surf_width -420 ,y =80 )#line:84
        if O00OOO0O00O000OOO .menutext .clicked ():#line:86
            O00OOO0O00O000OOO .menutext .text ="Let's Play"#line:87
            O00OOO0O00O000OOO .menutext .pos_x =random .randint (20 ,1200 )#line:88
            O00OOO0O00O000OOO .menutext .pos_y =random .randint (20 ,700 )#line:89
        for OOOOO00O0000OO000 in O0OO0O00OO0000000 :#line:91
            Options .handle_pygame_event (OOOOO00O0000OO000 )#line:92
            if OOOOO00O0000OO000 .type ==KEYDOWN :#line:93
                if OOOOO00O0000OO000 .key ==K_ESCAPE :#line:94
                    pass #line:95
            if OOOOO00O0000OO000 .type ==MOUSEBUTTONDOWN :#line:96
                if OOOOO00O0000OO000 .button ==1 :#line:97
                    O00OOO0O00O000OOO .mouse_clicked =True #line:98
                if O00OOO0O00O000OOO .btn_play .clicked ():#line:99
                    Button .clicked_sound (SOUND_START ,addition_vol =0.3 )#line:100
                    time .sleep (0.25 )#line:101
                    O00OOO0O00O000OOO .game .menu_music .stop ()#line:102
                    O00OOO0O00O000OOO .game .game_music .play (-1 )#line:103
                    O00OOO0O00O000OOO .game .change_state ("game_play")#line:104
                if O00OOO0O00O000OOO .btn_option .clicked ():#line:105
                    Button .clicked_sound (SOUND_BTNCLICK )#line:106
                    O00OOO0O00O000OOO .game .change_state ("option_menu")#line:107
                if O00OOO0O00O000OOO .btn_credit .clicked ():#line:108
                    Button .clicked_sound (SOUND_BTNCLICK )#line:109
                    O00OOO0O00O000OOO .game .change_state ("credit_menu")#line:110
                if O00OOO0O00O000OOO .btn_exit .clicked ():#line:111
                    Button .clicked_sound (SOUND_BTNCLICK )#line:112
                    time .sleep (0.25 )#line:113
                    pygame .quit ()#line:114
                    sys .exit ()#line:115
    def update (O0OOOO000O0O00O00 ):#line:117
        O0OOOO000O0O00O00 .display_info =pygame .display .Info ()#line:118
        O0OOOO000O0O00O00 .surf_width =O0OOOO000O0O00O00 .display_info .current_w #line:119
        O0OOOO000O0O00O00 .surf_height =O0OOOO000O0O00O00 .display_info .current_h #line:120
        O0OOOO000O0O00O00 .mouse_clicked =False #line:121
        for OO0OOOO0OOO000000 in O0OOOO000O0O00O00 .all_btn :#line:123
            OO0OOOO0OOO000000 .collide_sound (SOUND_UISELECT )#line:124
            OO0OOOO0OOO000000 .set_hover ()#line:125
            OO0OOOO0OOO000000 .set_elevate ()#line:126
    def render (O0O000000OO0O0OOO ):#line:130
        O0O000000OO0O0OOO .surface .fill ((0 ,0 ,0 ))#line:131
        O0O000000OO0O0OOO .surface .blit (pygame .transform .scale (O0O000000OO0O0OOO .background ,(O0O000000OO0O0OOO .surf_width ,O0O000000OO0O0OOO .surf_height )),(0 ,0 ))#line:132
        O0O000000OO0O0OOO .menutext .draw ()#line:134
        for OOOO000OO0O00OO0O in O0O000000OO0O0OOO .all_btn :#line:136
            OOOO000OO0O00OO0O .draw ()#line:137
        pygame .display .update ()#line:139
        O0O000000OO0O0OOO .clock .tick (O0O000000OO0O0OOO .fps )#line:140
class PauseMenu (GameState ):#line:142
    def __init__ (O00O00OOOO0O0O00O ,O0OOOOOO0O00OO0OO ):#line:143
        super ().__init__ (O0OOOOOO0O00OO0OO )#line:144
        O00O00OOOO0O0O00O .menutext =Label ('pause',font =FONT ,font_size =60 ,text_color =(255 ,255 ,255 ),x =20 ,y =20 )#line:147
        O00O00OOOO0O0O00O .btn_resume =O00O00OOOO0O0O00O .draw_btn ('Resume',x =O00O00OOOO0O0O00O .surf_width //2 -125 ,y =O00O00OOOO0O0O00O .surf_height //2 -150 ,width =250 ,height =50 )#line:150
        O00O00OOOO0O0O00O .btn_option =O00O00OOOO0O0O00O .draw_btn ('Options',x =O00O00OOOO0O0O00O .surf_width //2 -125 ,y =O00O00OOOO0O0O00O .surf_height //2 -50 ,width =250 ,height =50 )#line:151
        O00O00OOOO0O0O00O .btn_main_menu =O00O00OOOO0O0O00O .draw_btn ('Main Menu',x =O00O00OOOO0O0O00O .surf_width //2 -125 ,y =O00O00OOOO0O0O00O .surf_height //2 -(-50 ),width =250 ,height =50 )#line:152
        O00O00OOOO0O0O00O .all_btn =(O00O00OOOO0O0O00O .btn_resume ,O00O00OOOO0O0O00O .btn_option ,O00O00OOOO0O0O00O .btn_main_menu )#line:154
    def handle_events (O0OO0OO00O0000O00 ,O0000OO0OO0000000 ):#line:156
        for OO000000O000OOOO0 in O0000OO0OO0000000 :#line:157
            Options .handle_pygame_event (OO000000O000OOOO0 )#line:158
            if OO000000O000OOOO0 .type ==KEYDOWN :#line:159
                if OO000000O000OOOO0 .key ==K_ESCAPE :#line:160
                    O0OO0OO00O0000O00 .game .change_state ("game_play")#line:161
            if OO000000O000OOOO0 .type ==MOUSEBUTTONDOWN :#line:162
                if OO000000O000OOOO0 .button ==1 :#line:163
                    O0OO0OO00O0000O00 .mouse_clicked =True #line:164
                    if O0OO0OO00O0000O00 .btn_resume .clicked ():#line:165
                        Button .clicked_sound (SOUND_BTNCLICK )#line:166
                        O0OO0OO00O0000O00 .game .game_music .play (-1 )#line:167
                        O0OO0OO00O0000O00 .game .change_state ("game_play")#line:168
                    if O0OO0OO00O0000O00 .btn_option .clicked ():#line:169
                        Button .clicked_sound (SOUND_BTNCLICK )#line:170
                        O0OO0OO00O0000O00 .game .menu_music .play (-1 )#line:171
                        O0OO0OO00O0000O00 .game .change_state ("option_menu")#line:172
                    if O0OO0OO00O0000O00 .btn_main_menu .clicked ():#line:173
                        Button .clicked_sound (SOUND_BTNCLICK )#line:174
                        O0OO0OO00O0000O00 .game .menu_music .play (-1 )#line:175
                        O0OO0OO00O0000O00 .game .change_state ("main_menu")#line:176
    def update (OOO0000O0000OO0OO ):#line:178
        OOO0000O0000OO0OO .display_info =pygame .display .Info ()#line:179
        OOO0000O0000OO0OO .surf_width =OOO0000O0000OO0OO .display_info .current_w #line:180
        OOO0000O0000OO0OO .surf_height =OOO0000O0000OO0OO .display_info .current_h #line:181
        OOO0000O0000OO0OO .mouse_clicked =False #line:182
        OOO0000O0000OO0OO .game .menu_music .stop ()#line:184
        for O000OOOO00O00O0O0 in OOO0000O0000OO0OO .all_btn :#line:186
            O000OOOO00O00O0O0 .collide_sound (SOUND_UISELECT )#line:187
            O000OOOO00O00O0O0 .set_hover ()#line:188
            O000OOOO00O00O0O0 .set_elevate ()#line:189
    def render (O0OO00O0000OOOO0O ):#line:191
        O0OO00O0000OOOO0O .surface .fill ((0 ,0 ,0 ))#line:192
        O0OO00O0000OOOO0O .menutext .draw ()#line:194
        for O0O00O00OOO000000 in O0OO00O0000OOOO0O .all_btn :#line:196
            O0O00O00OOO000000 .draw ()#line:197
        pygame .display .update ()#line:199
        O0OO00O0000OOOO0O .clock .tick (O0OO00O0000OOOO0O .fps )#line:200
class OptionMenu (GameState ):#line:202
    def __init__ (O0O00O0O0000OOOO0 ,O00OOOO000OOO0OO0 ):#line:203
        super ().__init__ (O00OOOO000OOO0OO0 )#line:204
        O0O00O0O0000OOOO0 .option_rect =pygame .Rect (O0O00O0O0000OOOO0 .surf_width //4 ,O0O00O0O0000OOOO0 .surf_height //4 ,O0O00O0O0000OOOO0 .surf_width //2 ,O0O00O0O0000OOOO0 .surf_height //2 +100 )#line:206
        O0O00O0O0000OOOO0 .option_surf =pygame .Surface (O0O00O0O0000OOOO0 .option_rect .size ,pygame .SRCALPHA )#line:207
        O0O00O0O0000OOOO0 .option_label =Label ('Options',font =FONT ,font_size =60 ,text_color =(0 ,0 ,0 ),x =O0O00O0O0000OOOO0 .surf_width //2 -100 ,y =O0O00O0O0000OOOO0 .surf_height //2 -300 )#line:209
        O0O00O0O0000OOOO0 .music_label =Label ('Music Volume',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +20 )#line:210
        O0O00O0O0000OOOO0 .sfx_label =Label ('SFX Volume',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +80 )#line:211
        O0O00O0O0000OOOO0 .fullscreen_label =Label ('Full Screen',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +140 )#line:212
        O0O00O0O0000OOOO0 .del_save_label =Label ('Clear Save',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +210 )#line:213
        O0O00O0O0000OOOO0 .music_menu_label =Label ('Menu Music',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +300 )#line:214
        O0O00O0O0000OOOO0 .music_game_label =Label ('Game Music',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O00O0O0000OOOO0 .surf_width //2 -250 ,y =O0O00O0O0000OOOO0 .option_rect .top +370 )#line:215
        O0O00O0O0000OOOO0 .btn_back =O0O00O0O0000OOOO0 .draw_btn ('Back',x =50 ,y =O0O00O0O0000OOOO0 .surf_height //2 -300 ,width =150 ,height =50 )#line:217
        O0O00O0O0000OOOO0 .btn_back .top_color ="#83502E"#line:218
        O0O00O0O0000OOOO0 .btn_back .bottom_color ="#342012"#line:219
        O0O00O0O0000OOOO0 .btn_delsave =O0O00O0O0000OOOO0 .draw_btn ('\ue92b',font =FONT_ICON ,font_size =50 ,x =O0O00O0O0000OOOO0 .surf_width //2 +50 ,y =O0O00O0O0000OOOO0 .option_rect .top +220 ,width =100 ,height =50 )#line:221
        O0O00O0O0000OOOO0 .btn_delsave .top_color ="#83502E"#line:222
        O0O00O0O0000OOOO0 .btn_delsave .bottom_color ="#342012"#line:223
        O0O00O0O0000OOOO0 .confirm_choice ={"del_save":"Reset the game?"}#line:225
        O0O00O0O0000OOOO0 .confirm_prompt =None #line:226
        O0O00O0O0000OOOO0 .music_slider =RangeSlider (min_value =0 ,max_value =100 ,start_value =config .getint ('AUDIO','MUSIC_VOLUME'),x =O0O00O0O0000OOOO0 .surf_width //2 ,y =O0O00O0O0000OOOO0 .option_rect .top +50 ,button_color =(255 ,255 ,255 ),range_width =200 ,text_color ="#FFFFFF",show_min_max =False ,callback =Options .set_music_volume )#line:228
        O0O00O0O0000OOOO0 .sfx_slider =RangeSlider (min_value =0 ,max_value =100 ,start_value =config .getint ('AUDIO','SFX_VOLUME'),x =O0O00O0O0000OOOO0 .surf_width //2 ,y =O0O00O0O0000OOOO0 .option_rect .top +110 ,button_color =(255 ,255 ,255 ),range_width =200 ,text_color ="#FFFFFF",show_min_max =False ,callback =Options .set_sfx_volume )#line:229
        O0O00O0O0000OOOO0 .sfx_slider .play_sound_after_drag =True #line:230
        O0O00O0O0000OOOO0 .toggle_fullscreen =ToggleSwitch (font =FONT ,font_size =30 ,width =100 ,height =50 ,x =O0O00O0O0000OOOO0 .surf_width //2 +50 ,y =O0O00O0O0000OOOO0 .option_rect .top +150 ,start_state =config .getboolean ('GRAPHIC','SCREEN_CODE'),callback =Options .toggle_fullscreen )#line:232
        O0O00O0O0000OOOO0 .toggle_fullscreen .on_color ="#1C945C"#line:233
        O0O00O0O0000OOOO0 .toggle_fullscreen .off_color ="#D74B4B"#line:234
        O0O00O0O0000OOOO0 .test_music =msc_ingame [0 ]#line:236
        O0O00O0O0000OOOO0 .stop_sound_event =threading .Event ()#line:237
        O0O00O0O0000OOOO0 .music_menu_selector =MusicSelector (msc_menu ,start_index =config .getint ("AUDIO","MUSIC_MENU"),font =FONT ,uifont =FONT_ICON ,x =O0O00O0O0000OOOO0 .surf_width //2 +50 ,y =O0O00O0O0000OOOO0 .option_rect .top +300 ,callback =O0O00O0O0000OOOO0 .setmusic_menu )#line:239
        O0O00O0O0000OOOO0 .music_menu_selector .uileft ="\ue5e0"#line:240
        O0O00O0O0000OOOO0 .music_menu_selector .uiright ="\ue5e1"#line:241
        O0O00O0O0000OOOO0 .music_ingame_selector =MusicSelector (msc_ingame ,start_index =config .getint ("AUDIO","MUSIC_INGAME"),font =FONT ,uifont =FONT_ICON ,x =O0O00O0O0000OOOO0 .surf_width //2 +50 ,y =O0O00O0O0000OOOO0 .option_rect .top +370 ,callback =O0O00O0O0000OOOO0 .setmusic_ingame )#line:243
        O0O00O0O0000OOOO0 .music_ingame_selector .uileft ="\ue5e0"#line:244
        O0O00O0O0000OOOO0 .music_ingame_selector .uiright ="\ue5e1"#line:245
        O0O00O0O0000OOOO0 .all_label =(O0O00O0O0000OOOO0 .option_label ,O0O00O0O0000OOOO0 .music_label ,O0O00O0O0000OOOO0 .sfx_label ,O0O00O0O0000OOOO0 .fullscreen_label ,O0O00O0O0000OOOO0 .del_save_label ,O0O00O0O0000OOOO0 .music_menu_label ,O0O00O0O0000OOOO0 .music_game_label )#line:247
        O0O00O0O0000OOOO0 .all_btn =(O0O00O0O0000OOOO0 .btn_back ,O0O00O0O0000OOOO0 .btn_delsave )#line:248
    def handle_events (O0O0OO00O000O00O0 ,OOOO0OO0O0OOOO0O0 ):#line:250
        for O000O000O000OOO00 in OOOO0OO0O0OOOO0O0 :#line:251
            Options .handle_pygame_event (O000O000O000OOO00 )#line:252
            if O000O000O000OOO00 .type ==KEYDOWN :#line:253
                if O000O000O000OOO00 .key ==K_ESCAPE :#line:254
                    O0O0OO00O000O00O0 .stop_sound_event .set ()#line:255
                    O0O0OO00O000O00O0 .test_music .stop ()#line:256
                    O0O0OO00O000O00O0 .stop_sound_event .clear ()#line:257
                    if O0O0OO00O000O00O0 .game .prev_state =="main_menu":#line:258
                        O0O0OO00O000O00O0 .game .menu_music .stop ()#line:259
                        O0O0OO00O000O00O0 .game .menu_music .play (-1 )#line:260
                    O0O0OO00O000O00O0 .game .change_state (O0O0OO00O000O00O0 .game .prev_state )#line:261
            if O000O000O000OOO00 .type ==MOUSEBUTTONDOWN :#line:262
                if O000O000O000OOO00 .button ==1 :#line:263
                    O0O0OO00O000O00O0 .mouse_clicked =True #line:264
                    if O0O0OO00O000O00O0 .btn_delsave .clicked ():#line:265
                        Button .clicked_sound (SOUND_BTNCLICK )#line:266
                        O0O0OO00O000O00O0 .confirm_prompt =YesNoPopup (O0O0OO00O000O00O0 .confirm_choice ["del_save"],FONT ,width =500 ,height =300 )#line:267
                        O0O0OO00O000O00O0 .confirm_prompt .fill_color ="#83502E"#line:268
                        O0O0OO00O000O00O0 .confirm_prompt .text_color ="#FFFFFF"#line:269
                    if O0O0OO00O000O00O0 .btn_back .clicked ():#line:271
                        O0O0OO00O000O00O0 .stop_sound_event .set ()#line:272
                        O0O0OO00O000O00O0 .test_music .stop ()#line:273
                        O0O0OO00O000O00O0 .stop_sound_event .clear ()#line:274
                        Button .clicked_sound (SOUND_BTNCLICK )#line:275
                        if O0O0OO00O000O00O0 .game .prev_state =="main_menu":#line:276
                            O0O0OO00O000O00O0 .game .menu_music .stop ()#line:277
                            O0O0OO00O000O00O0 .game .menu_music .play (-1 )#line:278
                        O0O0OO00O000O00O0 .game .change_state (O0O0OO00O000O00O0 .game .prev_state )#line:279
            O0O0OO00O000O00O0 .sfx_slider .handle_event (O000O000O000OOO00 )#line:281
            O0O0OO00O000O00O0 .music_slider .handle_event (O000O000O000OOO00 )#line:282
            O0O0OO00O000O00O0 .toggle_fullscreen .handle_event (O000O000O000OOO00 )#line:283
            O0O0OO00O000O00O0 .music_menu_selector .handle_event (O000O000O000OOO00 )#line:284
            O0O0OO00O000O00O0 .music_ingame_selector .handle_event (O000O000O000OOO00 )#line:285
            if isinstance (O0O0OO00O000O00O0 .confirm_prompt ,YesNoPopup ):#line:286
                O0O0OO00O000O00O0 .confirm_prompt .handle_event (O000O000O000OOO00 )#line:287
                if O0O0OO00O000O00O0 .confirm_prompt .result is not None :#line:288
                    if O0O0OO00O000O00O0 .confirm_prompt .result :#line:289
                        Button .clicked_sound (SOUND_START ,addition_vol =0.3 )#line:290
                        SaveData .reset_game ()#line:291
                    else :#line:292
                        Button .clicked_sound (SOUND_BTNCLICK )#line:293
                    O0O0OO00O000O00O0 .confirm_prompt =None #line:294
    def update (O00OO0O0000O0OOO0 ):#line:296
        O00OO0O0000O0OOO0 .display_info =pygame .display .Info ()#line:297
        O00OO0O0000O0OOO0 .surf_width =O00OO0O0000O0OOO0 .display_info .current_w #line:298
        O00OO0O0000O0OOO0 .surf_height =O00OO0O0000O0OOO0 .display_info .current_h #line:299
        O00OO0O0000O0OOO0 .mouse_clicked =False #line:300
        O00OO0O0000O0OOO0 .test_music .set_volume (config .getint ('AUDIO','MUSIC_VOLUME')/100 )#line:302
        for O00000O00OOOOOO0O in O00OO0O0000O0OOO0 .all_btn :#line:304
            O00000O00OOOOOO0O .collide_sound (SOUND_UISELECT )#line:305
            O00000O00OOOOOO0O .set_hover ()#line:306
            O00000O00OOOOOO0O .set_elevate ()#line:307
        O00OO0O0000O0OOO0 .sfx_slider .update ()#line:309
        O00OO0O0000O0OOO0 .music_slider .update ()#line:310
    def render (OO000O00O00000000 ):#line:312
        OO000O00O00000000 .surface .fill ((217 ,189 ,165 ))#line:313
        pygame .draw .rect (OO000O00O00000000 .option_surf ,(0 ,0 ,0 ,128 ),OO000O00O00000000 .option_surf .get_rect ())#line:315
        OO000O00O00000000 .surface .blit (OO000O00O00000000 .option_surf ,OO000O00O00000000 .option_rect )#line:316
        for O0OO0OO0000OOO00O in OO000O00O00000000 .all_label :#line:319
            O0OO0OO0000OOO00O .draw ()#line:320
        for OO00O0OO00OOO000O in OO000O00O00000000 .all_btn :#line:322
            OO00O0OO00OOO000O .draw ()#line:323
        OO000O00O00000000 .toggle_fullscreen .draw ()#line:325
        OO000O00O00000000 .sfx_slider .draw ()#line:327
        OO000O00O00000000 .music_slider .draw ()#line:328
        OO000O00O00000000 .music_ingame_selector .draw ()#line:329
        OO000O00O00000000 .music_menu_selector .draw ()#line:330
        if isinstance (OO000O00O00000000 .confirm_prompt ,YesNoPopup )and OO000O00O00000000 .confirm_prompt .result is None :#line:332
            OO000O00O00000000 .confirm_prompt .draw ()#line:333
        pygame .display .update ()#line:335
        OO000O00O00000000 .clock .tick (OO000O00O00000000 .fps )#line:336
    def play_sound_thread (O0O0OOO0O000OOO00 ,OOO0OOOO0OOO00O00 :int ,OO0OOO000000OOO00 :int ):#line:338
        if O0O0OOO0O000OOO00 .stop_sound_event .is_set ():#line:339
            O0O0OOO0O000OOO00 .test_music .stop ()#line:340
            O0O0OOO0O000OOO00 .stop_sound_event .clear ()#line:341
        O0O0OOO0O000OOO00 .test_music =OOO0OOOO0OOO00O00 #line:342
        O0O0OOO0O000OOO00 .test_music .play (-1 )#line:343
        pygame .time .wait (OO0OOO000000OOO00 *1000 )#line:345
        O0O0OOO0O000OOO00 .test_music .stop ()#line:347
        O0O0OOO0O000OOO00 .game .menu_music .play (-1 )#line:348
    def setmusic_menu (O0O0OOO00OOO000OO ,OOO000OOOOOO0OO0O :int ):#line:350
        O0O0OOO00OOO000OO .stop_sound_event .set ()#line:351
        O0O0OOO00OOO000OO .game .menu_music .stop ()#line:352
        O0O0OOO00OOO000OO .test_music .stop ()#line:353
        OOOOOOO0O000O0OO0 =5 #line:355
        OOO00O000O000OO00 =threading .Thread (target =O0O0OOO00OOO000OO .play_sound_thread ,args =(msc_menu [OOO000OOOOOO0OO0O ],OOOOOOO0O000O0OO0 ))#line:356
        OOO00O000O000OO00 .start ()#line:357
        Options .save_menu_music (OOO000OOOOOO0OO0O ,msc_menu )#line:358
        O0O0OOO00OOO000OO .game .menu_music =msc_menu [config .getint ('AUDIO','MUSIC_MENU')]#line:359
    def setmusic_ingame (O0OO00OO0OO000OOO ,O0O0O0O0O000O0OOO :int ):#line:361
        O0OO00OO0OO000OOO .stop_sound_event .set ()#line:362
        O0OO00OO0OO000OOO .game .menu_music .stop ()#line:363
        O0OO00OO0OO000OOO .test_music .stop ()#line:364
        OO0O00OOOOOOOOO0O =5 #line:366
        O00OO0000O00O0O00 =threading .Thread (target =O0OO00OO0OO000OOO .play_sound_thread ,args =(msc_ingame [O0O0O0O0O000O0OOO ],OO0O00OOOOOOOOO0O ))#line:367
        O00OO0000O00O0O00 .start ()#line:368
        Options .save_ingame_music (O0O0O0O0O000O0OOO ,msc_ingame )#line:369
class CreditMenu (GameState ):#line:371
    def __init__ (O00000OO0O00OOOO0 ,O0O00000OO0O0O0O0 ):#line:372
        super ().__init__ (O0O00000OO0O0O0O0 )#line:373
        O00000OO0O00OOOO0 .credit_music =pygame .mixer .Sound (os .path .join ('audio','music','credit.mp3'))#line:375
        O00000OO0O00OOOO0 .centerx =O00000OO0O00OOOO0 .surface .get_rect ().centerx #line:377
        O00000OO0O00OOOO0 .centery =O00000OO0O00OOOO0 .surface .get_rect ().centery #line:378
        O00000OO0O00OOOO0 .deltaY =O00000OO0O00OOOO0 .centery +50 #line:379
        O00000OO0O00OOOO0 .credit_text ="""
        Project Name: Idle Rich
        
        Concept: Idle clicker & slot machine casino game
        
        
        This game is made by: Wiraphat Prasomphong
        
        Faculty of Engineering, KMITL
        
        Computer Engineering Continue (CEDT), 65015143
        
        01076110 Object Oriented Data Structures Project
        
        """#line:395
        O00000OO0O00OOOO0 .btn_back =O00000OO0O00OOOO0 .draw_btn ('Back',x =50 ,y =O00000OO0O00OOOO0 .surf_height //2 -300 ,width =150 ,height =50 )#line:397
        O00000OO0O00OOOO0 .btn_back .top_color ="#6B728E"#line:398
        O00000OO0O00OOOO0 .btn_back .bottom_color ="#474E68"#line:399
    def handle_events (O0O0OO00OO0000O0O ,O0O0OOO0OO0O0OOOO ):#line:401
        for O00OO0O0O00O00OO0 in O0O0OOO0OO0O0OOOO :#line:402
            Options .handle_pygame_event (O00OO0O0O00O00OO0 )#line:403
            if O00OO0O0O00O00OO0 .type ==KEYDOWN :#line:404
                if O00OO0O0O00O00OO0 .key ==K_ESCAPE :#line:405
                    O0O0OO00OO0000O0O .credit_music .stop ()#line:406
                    O0O0OO00OO0000O0O .game .menu_music .play (-1 )#line:407
                    O0O0OO00OO0000O0O .deltaY =O0O0OO00OO0000O0O .centery +50 #line:408
                    O0O0OO00OO0000O0O .game .change_state (O0O0OO00OO0000O0O .game .prev_state )#line:409
            if O00OO0O0O00O00OO0 .type ==MOUSEBUTTONDOWN :#line:410
                if O00OO0O0O00O00OO0 .button ==1 :#line:411
                    O0O0OO00OO0000O0O .mouse_clicked =True #line:412
                    if O0O0OO00OO0000O0O .btn_back .clicked ():#line:413
                        O0O0OO00OO0000O0O .credit_music .stop ()#line:415
                        O0O0OO00OO0000O0O .game .menu_music .play (-1 )#line:416
                        O0O0OO00OO0000O0O .deltaY =O0O0OO00OO0000O0O .centery +50 #line:417
                        O0O0OO00OO0000O0O .game .change_state (O0O0OO00OO0000O0O .game .prev_state )#line:418
    def update (OO0O000000O00O0OO ):#line:420
        OO0O000000O00O0OO .btn_back .set_hover ()#line:422
        OO0O000000O00O0OO .btn_back .set_elevate ()#line:423
        OO0O000000O00O0OO .credit_music .set_volume ((config .getint ('AUDIO','MUSIC_VOLUME')/100 ))#line:425
        OO0O000000O00O0OO .game .menu_music .stop ()#line:426
        OO0O000000O00O0OO .credit_music .play (-1 )#line:427
    def render (OO00O0OO0OOO00OOO ):#line:429
        OO00O0OO0OOO00OOO .surface .fill ((0 ,0 ,0 ))#line:430
        OO00O0OO0OOO00OOO .btn_back .draw ()#line:432
        OO00O0OO0OOO00OOO .deltaY -=1 #line:434
        O0OOOOOO000000OO0 =0 #line:436
        OOOOO0O0OOO0OOO0O =[]#line:437
        OOO00OO0OO000O00O =[]#line:438
        if OO00O0OO0OOO00OOO .deltaY <-720 :#line:440
            OO00O0OO0OOO00OOO .deltaY =OO00O0OO0OOO00OOO .centery +50 #line:441
        O0O0OO000OO0000O0 =pygame .font .Font (FONT ,35 )#line:443
        for O00OOOO00OOOO0OO0 in OO00O0OO0OOO00OOO .credit_text .split ('\n'):#line:445
            OO00O00O0O0OOO000 =O0O0OO000OO0000O0 .render (O00OOOO00OOOO0OO0 ,True ,"#FFFFFF")#line:446
            OOOOO0O0OOO0OOO0O .append (OO00O00O0O0OOO000 )#line:447
            OO00O0000OO0OOO0O =OO00O00O0O0OOO000 .get_rect (center =(OO00O0OO0OOO00OOO .centerx ,OO00O0OO0OOO00OOO .centery +OO00O0OO0OOO00OOO .deltaY +30 *O0OOOOOO000000OO0 ))#line:448
            OOO00OO0OO000O00O .append (OO00O0000OO0OOO0O )#line:449
            O0OOOOOO000000OO0 =O0OOOOOO000000OO0 +1 #line:450
        for OO000OOOOOO00OO0O in range (len (OOOOO0O0OOO0OOO0O )):#line:452
            OO00O0OO0OOO00OOO .surface .blit (OOOOO0O0OOO0OOO0O [OO000OOOOOO00OO0O ],OOO00OO0OO000O00O [OO000OOOOOO00OO0O ])#line:453
        pygame .display .update ()#line:455
        OO00O0OO0OOO00OOO .clock .tick (OO00O0OO0OOO00OOO .fps )#line:456
class GamePlay (GameState ):#line:458
    def __init__ (O0O0O00OOOOOOO0OO ,OO00OO0O0O000OO00 ):#line:459
        super ().__init__ (OO00OO0O0O000OO00 )#line:460
        O0O0O00OOOOOOO0OO .game_state ="idle"#line:462
        O0O0O00OOOOOOO0OO .game_data =PlayerSystem ()#line:464
        O0O0O00OOOOOOO0OO .powerup_data =O0O0O00OOOOOOO0OO .game_data .powerup #line:465
        O0O0O00OOOOOOO0OO .sound_buy =pygame .mixer .Sound (os .path .join ('audio','sfx','buy.wav'))#line:466
        O0O0O00OOOOOOO0OO .sound_buy .set_volume (config .getint ('AUDIO','SFX_VOLUME')+0.1 )#line:467
        O0O0O00OOOOOOO0OO .sound_err =pygame .mixer .Sound (os .path .join ('audio','sfx','error.mp3'))#line:468
        O0O0O00OOOOOOO0OO .sound_err .set_volume (config .getint ('AUDIO','SFX_VOLUME')+0.1 )#line:469
        O0O0O00OOOOOOO0OO .hit =O0O0O00OOOOOOO0OO .powerup_data ["hit"]#line:471
        O0O0O00OOOOOOO0OO .lbl_money =Label (f'{0}',font =FONT ,font_size =50 ,text_color =(255 ,255 ,255 ),x =O0O0O00OOOOOOO0OO .surf_width //2 -350 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -300 )#line:473
        O0O0O00OOOOOOO0OO .btn_get_rich =O0O0O00OOOOOOO0OO .draw_btn ('฿',font_size =150 ,x =O0O0O00OOOOOOO0OO .surf_width //2 -100 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -100 ,width =200 ,height =200 )#line:475
        O0O0O00OOOOOOO0OO .btn_swstate =O0O0O00OOOOOOO0OO .draw_btn ('\ueb40',font =FONT_ICON ,font_size =50 ,x =50 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -300 ,width =80 ,height =80 )#line:477
        O0O0O00OOOOOOO0OO .lbl_hitpwlbl =Label ('Hit Power: ',font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O0O00OOOOOOO0OO .surf_width //2 +200 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -200 )#line:479
        O0O0O00OOOOOOO0OO .lbl_hitlvl =Label (f"{O0O0O00OOOOOOO0OO.hit.level}",font =FONT ,font_size =30 ,text_color ="#FF0000",x =O0O0O00OOOOOOO0OO .surf_width //2 +370 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -200 )#line:480
        O0O0O00OOOOOOO0OO .lbl_hitcostlbl =Label ("Next Level: ",font =FONT ,font_size =30 ,text_color =(255 ,255 ,255 ),x =O0O0O00OOOOOOO0OO .surf_width //2 +200 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -150 )#line:481
        O0O0O00OOOOOOO0OO .lbl_hitcost =Label (f"{Balance.format_balance(O0O0O00OOOOOOO0OO.hit.cost)}",font =FONT ,font_size =30 ,text_color ="#FF0000",x =O0O0O00OOOOOOO0OO .surf_width //2 +370 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -150 )#line:482
        O0O0O00OOOOOOO0OO .btn_hitpw =O0O0O00OOOOOOO0OO .draw_btn (f'Upgrade: Hit Power',font =FONT ,font_size =25 ,x =O0O0O00OOOOOOO0OO .surf_width //2 +200 ,y =O0O0O00OOOOOOO0OO .surf_height //2 -80 ,width =300 ,height =50 )#line:483
        O0O0O00OOOOOOO0OO .btn_hitpw .text_color ="#FFFFFF"if O0O0O00OOOOOOO0OO .game_data .balance .get_balance ()>=O0O0O00OOOOOOO0OO .hit .cost else "#FF0000"#line:484
        O0O0O00OOOOOOO0OO .bounce_money_text =""#line:485
        O0O0O00OOOOOOO0OO .bounce_money_initx =O0O0O00OOOOOOO0OO .btn_get_rich .top_rect .centerx -100 #line:486
        O0O0O00OOOOOOO0OO .bounce_money_inity =O0O0O00OOOOOOO0OO .btn_get_rich .top_rect .centery #line:487
        O0O0O00OOOOOOO0OO .bounce_money_x =O0O0O00OOOOOOO0OO .bounce_money_initx #line:488
        O0O0O00OOOOOOO0OO .bounce_money_y =O0O0O00OOOOOOO0OO .bounce_money_inity #line:489
        O0O0O00OOOOOOO0OO .bounce_money_anmspd =9 #line:490
        O0O0O00OOOOOOO0OO .bounce_money_anmphs =0 #line:491
        O0O0O00OOOOOOO0OO .bounce_money_direction =random .choice ((-1 ,1 ))#line:492
        O0O0O00OOOOOOO0OO .is_bounce_money_animating =False #line:493
        O0O0O00OOOOOOO0OO .all_btn_idle =(O0O0O00OOOOOOO0OO .btn_get_rich ,O0O0O00OOOOOOO0OO .btn_swstate ,O0O0O00OOOOOOO0OO .btn_hitpw )#line:496
        O0O0O00OOOOOOO0OO .all_lbl_idle =(O0O0O00OOOOOOO0OO .lbl_money ,O0O0O00OOOOOOO0OO .lbl_hitpwlbl ,O0O0O00OOOOOOO0OO .lbl_hitlvl ,O0O0O00OOOOOOO0OO .lbl_hitcost ,O0O0O00OOOOOOO0OO .lbl_hitcostlbl )#line:497
        O0O0O00OOOOOOO0OO .all_btn_slot =[O0O0O00OOOOOOO0OO .btn_swstate ]#line:499
    def money_bounce_gentext (O00000O0O00OOO0O0 ,text :str =""):#line:501
        O00000O0O00OOO0O0 .bounce_money_text =text #line:502
        O00000O0O00OOO0O0 .is_bounce_money_animating =True #line:503
        O00000O0O00OOO0O0 .bounce_money_anmphs =0 #line:504
    def money_bounce_animate (O0O0OO000O0O0000O ):#line:506
        O0O0OO000O0O0000O .bounce_money_anmphs +=O0O0OO000O0O0000O .bounce_money_anmspd #line:507
        O0O0OO000O0O0000O .bounce_money_x =O0O0OO000O0O0000O .bounce_money_initx +O0O0OO000O0O0000O .bounce_money_anmphs *O0O0OO000O0O0000O .bounce_money_direction [0 ]#line:508
        O0O0OO000O0O0000O .bounce_money_y =O0O0OO000O0O0000O .bounce_money_inity -O0O0OO000O0O0000O .bounce_money_anmphs *O0O0OO000O0O0000O .bounce_money_direction [1 ]#line:509
        if O0O0OO000O0O0000O .bounce_money_anmphs >=180 :#line:510
            O0O0OO000O0O0000O .is_bounce_money_animating =False #line:511
    def money_bounce_render (OO0OO0OO0OOO0O000 ):#line:513
        if OO0OO0OO0OOO0O000 .is_bounce_money_animating :#line:514
            O00OOO0OO00000O00 =pygame .font .Font (FONT ,36 )#line:515
            O0OOO00OOOO0O0000 =O00OOO0OO00000O00 .render (OO0OO0OO0OOO0O000 .bounce_money_text ,True ,(255 ,255 ,255 ))#line:516
            O000OO0OOOO00OOO0 =O0OOO00OOOO0O0000 .get_rect ()#line:517
            O000OO0OOOO00OOO0 .topleft =(OO0OO0OO0OOO0O000 .bounce_money_x ,OO0OO0OO0OOO0O000 .bounce_money_y )#line:518
            OO0OO0OO0OOO0O000 .surface .blit (O0OOO00OOOO0O0000 ,O000OO0OOOO00OOO0 )#line:519
    def handle_idle_state (O00000000OOO0O00O ,O000OO000O0OO0O0O ):#line:521
        if O000OO000O0OO0O0O .type ==MOUSEBUTTONDOWN :#line:522
            if O000OO000O0OO0O0O .button ==1 :#line:523
                O00000000OOO0O00O .mouse_clicked =True #line:524
            if O00000000OOO0O00O .btn_get_rich .clicked ():#line:525
                Button .clicked_sound (O00000000OOO0O00O .sound_buy )#line:526
                O00000000OOO0O00O .game_data .balance .add_balance_by_click (O00000000OOO0O00O .hit .power )#line:527
                O00000000OOO0O00O .game_data .update_save ()#line:528
                O00000000OOO0O00O .money_bounce_gentext (f"Your got {Balance.format_balance(O00000000OOO0O00O.hit.power)}")#line:529
            if O00000000OOO0O00O .btn_hitpw .clicked ():#line:530
                if O00000000OOO0O00O .game_data .balance .add_transaction (-O00000000OOO0O00O .powerup_data ["hit"].cost ,"upgrade hit power"):#line:531
                    Button .clicked_sound (O00000000OOO0O00O .sound_buy )#line:532
                    O00000000OOO0O00O .hit .upgrade ()#line:533
                    O00000000OOO0O00O .game_data .update_save ()#line:534
                else :#line:535
                    Button .clicked_sound (O00000000OOO0O00O .sound_err )#line:536
    def handle_slot_state (OOO00OOOO000O0OO0 ,OOOO000OO0OO00OOO ):#line:538
        if OOOO000OO0OO00OOO .type ==MOUSEBUTTONDOWN :#line:539
            if OOOO000OO0OO00OOO .button ==1 :#line:540
                OOO00OOOO000O0OO0 .mouse_clicked =True #line:541
    def handle_events (OOOOOO0O0O0OOOOO0 ,O000000OOO00O0O0O ):#line:543
        for O00000OO0O00O000O in O000000OOO00O0O0O :#line:544
            Options .handle_pygame_event (O00000OO0O00O000O )#line:545
            if O00000OO0O00O000O .type ==KEYDOWN :#line:546
                if O00000OO0O00O000O .key ==K_ESCAPE :#line:547
                    OOOOOO0O0O0OOOOO0 .game .game_music .stop ()#line:548
                    OOOOOO0O0O0OOOOO0 .game_data .update_save ()#line:549
                    OOOOOO0O0O0OOOOO0 .game .change_state ("pause_menu")#line:550
            if OOOOOO0O0O0OOOOO0 .game_state =="idle":#line:551
                OOOOOO0O0O0OOOOO0 .handle_idle_state (O00000OO0O00O000O )#line:552
            elif OOOOOO0O0O0OOOOO0 .game_state =="slot":#line:553
                OOOOOO0O0O0OOOOO0 .handle_slot_state (O00000OO0O00O000O )#line:554
            if OOOOOO0O0O0OOOOO0 .btn_swstate .clicked ():#line:555
                Button .clicked_sound (SOUND_BTNCLICK )#line:556
                if OOOOOO0O0O0OOOOO0 .game_state =="idle":#line:557
                    OOOOOO0O0O0OOOOO0 .game_state ="slot"#line:558
                elif OOOOOO0O0O0OOOOO0 .game_state =="slot":#line:559
                    OOOOOO0O0O0OOOOO0 .game_state ="idle"#line:560
    def update_idle_state (O0OO00OOOOO0O0O0O ):#line:562
        O0OO00OOOOO0O0O0O .powerup_data ["hit"].cast ()#line:563
        O0OO00OOOOO0O0O0O .lbl_money .text =f'{O0OO00OOOOO0O0O0O.game_data.balance}'#line:565
        O0OO00OOOOO0O0O0O .lbl_hitlvl .text =f"{O0OO00OOOOO0O0O0O.hit.level}"#line:567
        O0OO00OOOOO0O0O0O .lbl_hitcost .text =f"{Balance.format_balance(O0OO00OOOOO0O0O0O.hit.cost)}"#line:568
        for O0O0O0O0O0OO0O00O in O0OO00OOOOO0O0O0O .all_btn_idle :#line:571
            O0O0O0O0O0OO0O00O .set_hover ()#line:573
            O0O0O0O0O0OO0O00O .set_elevate ()#line:574
        if O0OO00OOOOO0O0O0O .is_bounce_money_animating :#line:576
            O0OO00OOOOO0O0O0O .money_bounce_animate ()#line:577
            if abs (O0OO00OOOOO0O0O0O .bounce_money_y )<abs (O0OO00OOOOO0O0O0O .bounce_money_inity //2 ):#line:578
                O0OO00OOOOO0O0O0O .bounce_money_y =O0OO00OOOOO0O0O0O .bounce_money_inity #line:579
                O0OO00OOOOO0O0O0O .is_bounce_money_animating =False #line:580
        else :#line:581
            O0OO00OOOOO0O0O0O .bounce_money_y =O0OO00OOOOO0O0O0O .bounce_money_inity #line:582
            O0OO0O0OO000OO0OO =random .uniform (0 ,2 *math .pi )#line:583
            O0OO00OOOOO0O0O0O .bounce_money_direction =(math .cos (O0OO0O0OO000OO0OO ),math .sin (O0OO0O0OO000OO0OO ))#line:584
    def update_slot_state (O000OOO00O00OOO0O ):#line:587
        O000OOO00O00OOO0O .surface .fill ((0 ,0 ,0 ))#line:588
        for OOOO00O00O00OO00O in O000OOO00O00OOO0O .all_btn_slot :#line:590
            OOOO00O00O00OO00O .set_hover ()#line:592
            OOOO00O00O00OO00O .set_elevate ()#line:593
    def update (OOO0O0O000O0OOOOO ):#line:595
        OOO0O0O000O0OOOOO .game .menu_music .stop ()#line:596
        if OOO0O0O000O0OOOOO .game_state =="idle":#line:598
            OOO0O0O000O0OOOOO .update_idle_state ()#line:599
        elif OOO0O0O000O0OOOOO .game_state =="slot":#line:600
            OOO0O0O000O0OOOOO .update_slot_state ()#line:601
    def render_idle_state (O0OOO0OO0OOO00O00 ):#line:603
        O0OOO0OO0OOO00O00 .surface .fill ((217 ,189 ,165 ))#line:604
        for O00O0OOO00O000O00 in O0OOO0OO0OOO00O00 .all_lbl_idle :#line:606
            O00O0OOO00O000O00 .draw ()#line:607
        for O00O000OO00O0OO00 in O0OOO0OO0OOO00O00 .all_btn_idle :#line:609
            O00O000OO00O0OO00 .draw ()#line:610
        O0OOO0OO0OOO00O00 .money_bounce_render ()#line:612
    def render_slot_state (O0OO000O000O00OOO ):#line:614
        for OO00OO000000OO00O in O0OO000O000O00OOO .all_btn_slot :#line:615
            OO00OO000000OO00O .draw ()#line:616
    def render (OO0OOO00O000OO0O0 ):#line:618
        if OO0OOO00O000OO0O0 .game_state =="idle":#line:619
            OO0OOO00O000OO0O0 .render_idle_state ()#line:620
        elif OO0OOO00O000OO0O0 .game_state =="slot":#line:621
            OO0OOO00O000OO0O0 .render_slot_state ()#line:622
        pygame .display .update ()#line:624
        OO0OOO00O000OO0O0 .clock .tick (OO0OOO00O000OO0O0 .fps )#line:625
