# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys

import pygame as pg
from Screens import *
from dev_tools import *
from items import *
from campaign import *
from skills import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")
pg.display.set_icon(pg.image.load(DATA_ROOT + "/data/textures/icons/money_icon.png"))

on__screen.active_screen = main_menu
on__screen.active_table = "Close"

dev_shortcut = None
devmode = False

click_acc = True
bt_acc = True
tt_acc = True
pt_acc = True
sg_acc = True
gg_acc = True

def blit_background():
    if not on__screen.active_screen.backbackground == None:
        screen.blit(on__screen.active_screen.backbackground,(0,0))

def blit_screen():
    screen.blit(on__screen.active_screen.background,(0,0))
    if on__screen.active_screen.name == "Profile":
        stat_bg = pg.surface.Surface((440,440),pg.SRCALPHA)
        stat_bg.fill((30,30,30,180))
        screen.blit(stat_bg, (680,150))
    for o in on__screen.blit_objects:
        o.blit_self(screen, on__screen)
    if not on__screen.active_table == "Close":
        table = pg.Surface(on__screen.active_table.size)
        table.set_alpha(on__screen.active_table.alpha)
        screen.blit(table, (on__screen.active_table.position))
        
def blit_shop_items():
    for t in tooltip_class.tooltips:
            if "Item" in t.table_name:
                t.show = False
    if not item_class.weapons == []:
        for weapon in item_class.weapons:
            tooltip_class.tooltips = weapon.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen, tooltip_class)
    if not item_class.armors == []:
        for armor in item_class.armors:
            tooltip_class.tooltips = armor.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen, tooltip_class)
    if not item_class.misc_items == []:
        for misc_item in item_class.misc_items:
            tooltip_class.tooltips = misc_item.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen, tooltip_class)
    
def blit_skills():
    if not skill_class.skills == []:
        for skill in skill_class.skills:
            skill.draw_skill(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen)
            
def blit_debuffs():
    if not debuff_class.debuffs == []:
        for debuff in debuff_class.debuffs:
            debuff.draw_debuff(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen)
    
    
def stop_multi_click(devmode, m_pressed, click_acc):
    if not devmode:
        if click_acc and m_pressed[0]:
            click_acc = False
            return click_acc
        elif not click_acc and m_pressed[0]:
            m_pressed[0] = False
            return click_acc
        elif not click_acc and not m_pressed[0]:
            click_acc = True
            return click_acc
        else:
            return click_acc
        
def work_buttons_and_texts():
    if not on__screen.active_screen == "Exit" or not on__screen.active_screen == None:
        for button in button_class.buttons:
            button.blit_self(screen, on__screen)
            if on__screen.button_activity:
                button.check(m_pressed, on__screen)
                
    if not on__screen.button_activity:
        on__screen.button_activity = not on__screen.button_activity
        
    for t in text_class.all:
        t.blit_self(screen, on__screen)
        
    for b in on__screen.bought_icons:
        b.blit_self(screen, on__screen)
        
def blit_tooltips():
    if not tooltip_class.tooltips == []:
        for tooltip in tooltip_class.tooltips:
            tooltip.draw_tooltip(m_pos, screen, on__screen)
            
def blit_xp_bar():
    if not on__screen.active_screen == "Exit" and on__screen.active_table == "Close":
        if on__screen.active_screen.name == "Profile":
            xp_bar.draw_bar(screen, player.xp, player.level, player.xp_req)
        if not on__screen.active_table == "Close":
            if on__screen.active_table.name == "Win table":
                small_xp_bar.draw_bar(screen, player.xp, player.level, player.xp_req)
                
def blit_stat_bar():
    if not on__screen.active_screen == "Exit" and on__screen.active_table == "Close":
        if on__screen.active_screen.name == "Profile":
               health_stat_bar.draw_stat_bar(screen, player.hp_stat, 0)
               mana_stat_bar.draw_stat_bar(screen, player.mana_stat, 1)
               int_stat_bar.draw_stat_bar(screen, player.int_stat, 2)
               luck_stat_bar.draw_stat_bar(screen, player.luck_stat, 3)
                
def update_tooltips():
    on_fire_tooltip.update_tooltip(fireball.shown)
    wet_tooltip.update_tooltip(water_blast.shown)
    shocked_tooltip.update_tooltip(lightning_bolt.shown)
    poisoned_tooltip.update_tooltip(poison_dart.shown)
    frozen_tooltip.update_tooltip(ice_storm.shown)
    
def work_devmode(devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc):
    ### DEVELOPER MODE ###
    if pressed[pg.K_d]:
        dev_shortcut = 1
    
    if pressed[pg.K_e] and dev_shortcut == 1:
        dev_shortcut = 2
    
    if pressed[pg.K_v] and dev_shortcut == 2:
        if devmode == False:
            devmode = True
            dev_shortcut = None
        else:
            devmode = False
            dev_shortcut = None

    ### DEVELOPER MODE ###
    if devmode:
        ### TEXTURE PREVIEW TOOL ###
        # Zde se do podprogramu zadá cesta textury, kterou chceme vidět ve hře
        pt.get_texture(DATA_ROOT + "/data/textures/icons/skills/water_blast.png")
        # Zde se textury zobrazují
        pt.render_preview(screen, resolution)
        
        # Aktivace a deaktivate Texture Preview Toolu
        if pressed[pg.K_r] and pt_acc:
            pt.on_off()
            pt_acc = False
            
        elif pressed[pg.K_r] and not pt_acc:
            pass
        else:
            pt_acc = True
        
        ### BUTTON TOOL ###
        # Práce Button_tool -> třeba aktivovat
        bt.find(m_pressed)
        bt.calculate()
        
        # Vypisování výsledků Button_tool
        bt.list(pressed, screen)
        
        # Aktivace/Deaktivace Button_tool
        if pressed[pg.K_s] and bt_acc:
            bt.on_off()
            bt_acc = False
        elif pressed[pg.K_s] and not bt_acc:
            pass
        else:
            bt_acc = True
            
        ### TEXT TOOL ###
        # Práce Text_tool -> třeba aktivovat
        tt.find(m_pressed)
        tt.change(pressed)
        
        # Vypisování a vykreslení výsledků Text_tool
        tt.show("Slime", pressed, screen, (190,20,20))
        
        # Aktivace/Deaktivace Text_tool
        if pressed[pg.K_t] and tt_acc:
            tt.on_off()
            tt_acc = False
        elif pressed[pg.K_t] and not tt_acc:
            pass
        else:
            tt_acc = True
            
        ### SKILL GIVER ###
        if pressed[pg.K_g] and sg_acc:
            player.skills.append(water_blast)
            player.skills.append(rock_throw)
            player.skills.append(ice_storm)
            player.skills.append(poison_dart)
            player.skills.append(lightning_bolt)
            player.skills.append(life_steal)
        elif pressed[pg.K_g] and not sg_acc:
            pass
        else:
            sg_acc = True
            
        if pressed[pg.K_o]:
            player.gold += 100
            
        if pressed[pg.K_p]:
            player.level += 1
            
        return devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc
    
    else:
        return devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc

while True:
    # Získání infa o akcích
    events = pg.event.get()
    pressed = pg.key.get_pressed()
    m_pressed = [pg.mouse.get_pressed()[0], pg.mouse.get_pressed()[1], pg.mouse.get_pressed()[2]]
    m_pos = pg.mouse.get_pos()
    
    # Možnosti vypnutí
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    if on__screen.active_screen == "Exit":
        pg.quit()
        sys.exit()
    
    # Vykreslení obrazovky/tabulky
    blit_screen()
    
    # Vykreslení barů statů
    blit_stat_bar()
    
    # Vykreslování itemů v obchodě
    blit_shop_items()
    
    # Vykreslování skillů v profilu
    blit_skills()
    
    # Vykreslování debuffů v profilu
    blit_debuffs()
    
    # Vykreslování věcí v kampani
    counter.blit_self(screen, on__screen)
    
    # Zrušení multi-klikání
    click_acc = stop_multi_click(devmode, m_pressed, click_acc)
    
    # Vykreslení tlačítek + kontrola stisku tlačítek
    work_buttons_and_texts()
    
    # Vykreslení xp baru v profilu
    blit_xp_bar()
        
    # Vykreslení tooltipů
    blit_tooltips()
    
    # Aktualizace vybraných tooltipů
    update_tooltips()

    if pressed[pg.K_a]:
        Button.change_table(button_class.buttons[0], "End table", on__screen)
        
    # BITVA
    if on__screen.battle == True:
        round_time = 0
        affects_time = 0
        message_time = 0
        while on__screen.battle == True:
            events = pg.event.get()
            pressed = pg.key.get_pressed()
            m_pressed = [pg.mouse.get_pressed()[0], pg.mouse.get_pressed()[1], pg.mouse.get_pressed()[2]]
            
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            blit_background()
            
            battle_info.blit_player(screen)
            battle_info.blit_enemy(screen)
            battle_info.show_bars(screen)
            battle_info.show_turn(screen)
            
            blit_screen()
            blit_xp_bar()
            
            if on__screen.active_table == "Close":
                button_class.buttons = battle_info.show_cooldown(button_class, screen)
                battle_info.show_debuffs(screen)
                battle_info.blit_player_icon(screen)
                battle_info.blit_enemy_icon(screen)
            
            counter.blit_self(screen, on__screen)
            
            click_acc = stop_multi_click(devmode, m_pressed, click_acc)
            
            work_buttons_and_texts()
            
            if not battle_info.pause:
                if round_time >= 1520:
                    round_time = 0
                    button_class, small_xp_bar = battle_info.check_fight(on__screen, button_class, small_xp_bar)
                if affects_time >= 1000:
                    affects_time = 0
                    battle_info.check_debuffs()
                    if battle_info.player_mana_copy >= battle_info.player_max_mana:
                        battle_info.player_mana_copy = battle_info.player_max_mana
                    elif battle_info.player_mana_copy < battle_info.player_max_mana:
                        battle_info.player_mana_copy += 1
                if message_time >= 1500:
                    message_time = 0
                    text_class.hide_messages()
            else:
                round_time = 0
                affects_time = 0
            
            devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc = work_devmode(devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc)
            
            pg.display.update()
            time = 0
            time += clock.tick(100)
            round_time += time
            affects_time += time
            if text_class.check():
                message_time += time
    
    devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc = work_devmode(devmode, dev_shortcut, bt_acc, tt_acc, pt_acc, sg_acc)
    pg.display.update()
    clock.tick(100)
    