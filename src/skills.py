import pygame as pg
import sys
import random
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
class skill_cl():
    def __init__(self):
        self.skills = []

skill_class = skill_cl()

class debuff_cl():
    def __init__(self):
        self.debuffs = []
        self.player_debuffs = []
        self.enemy_debuffs = []
        
debuff_class = debuff_cl()
    
class debuff():
    def __init__(self, icon, name, desc, stat_desc, duration, belonging, order):
        self.icon = icon
        self.name = name
        self.desc = desc
        self.stat_desc = stat_desc
        self.active = False
        # duration in seconds
        self.duration = duration
        self.duration_e = 0
        self.duration_p = 0
        self.belonging = belonging
        self.name_size = 75
        self.desc_size = 35
        self.stat_desc_size = 25
        self.debuff_order = order
        self.space = 135
        
    ## Toto spustit každé kolo, i když není žádný debuff aktivní
    def debuff_tick(self, target, target_hp):
        if target.id == "player":
            self.duration_p -= 1
        elif target.id == "enemy":
            self.duration_e -= 1
            
        if self.duration_p = 0:
            debuff_class.player_debuffs.remove(self)
        elif self.duration_e = 0:
            debuff_class.enemy_debuffs.remove(self)
        
        if self.name == "On Fire!":
            if target.id == "player":
                if not target.armor.armor == None:
                    damage = 1 * ((100 - target.armor.armor) / 100)
                    damage = round(damage)
                else:
                    damage = 1
            elif target.id == "enemy":
                if not target.armor == None:
                    damage = 1 * ((100 - target.armor.armor) / 100)
                    damage = round(damage)
                else:
                    damage = 1
            target_hp -= damage # Toto číslo se dá pozměnit
            
        if self.name == "Frozen!":
            stun_chance = random.randint(0, 4) # tyto čísla jdou poupravit pro zvednutí šance na stun
            if stun_chance == 4:
                if target.id == "player":
                    battle_info.player_turn = False
                elif target.id == "enemy":
                    battle_info.player_turn = True
            
        if self.name == "Poisoned!":
            player.hp -= 1 # Toto číslo se dá pozměnit
            
        if self.name == "Wet!":
            # Zranitelnost se udává v %
            if target.id == "player":
                battle_info.player_effects["defense_ef"] = 10
            elif target.id == "enemy":
                battle_info.enemy_effects["defense_ef"] = 10
            
        if self.name == "Shocked!":
            # Oslabení se udává v %
            if target.id == "player":
                battle_info.player_effects["damage_ef"] = 10
            elif target.id == "enemy":
                battle_info.enemy_effects["damage_ef"] = 10
        
    def draw_debuff(self, font, screen, on_screen):
        if on_screen.active_screen.name in self.belonging:
            
            icon_scaled = pg.transform.scale(self.icon, (125,125))
            
            self.name_font = pg.font.Font(font, self.name_size)
            self.desc_font = pg.font.Font(font, self.desc_size)
            self.desc_stat_font = pg.font.Font(font,self.stat_desc_size)
            
            name_text = self.name_font.render(self.name, True, (0,0,0))
            name_text_rect = name_text.get_rect()
            name_text_rect.topleft = 230,80 + (self.debuff_order * self.space)
            
            desc_text_list = []
            desc_pos_list = []
            desc_i = 0
            
            for desc_line in self.desc.split('\n'):
                desc_text_line = self.desc_font.render(desc_line, True, (75,75,75))
                desc_text_list.append(desc_text_line)
                desc_pos = desc_text_line.get_rect(topleft=(230, 80 + (self.name_size / 1.2) + (self.desc_size * desc_i) + (self.debuff_order * self.space)))
                desc_pos_list.append(desc_pos)
                desc_i = desc_i + 1
            
            for desc_j in range(desc_i):
                screen.blit(desc_text_list[desc_j], desc_pos_list[desc_j])
                
            stat_desc_text_list = []
            stat_desc_pos_list = []
            stat_desc_i = 0
            
            for stat_desc_line in self.stat_desc.split('\n'):
                stat_desc_text_line = self.desc_stat_font.render(stat_desc_line, True, (150,100,100))
                stat_desc_text_list.append(stat_desc_text_line)
                stat_desc_pos = stat_desc_text_line.get_rect(topleft=(230, 80 + (self.name_size / 1.2) + (self.desc_size * len(desc_pos_list)) + (self.stat_desc_size * stat_desc_i) + (self.debuff_order * self.space)))
                stat_desc_pos_list.append(stat_desc_pos)
                stat_desc_i = stat_desc_i + 1
            
            for stat_desc_j in range(stat_desc_i):
                screen.blit(stat_desc_text_list[stat_desc_j], stat_desc_pos_list[stat_desc_j])

            screen.blit(icon_scaled, (100,80 + (self.debuff_order * self.space)))
            screen.blit(name_text, name_text_rect)

on_fire_debuff = debuff(pg.image.load(DATA_ROOT + "/data/textures/icons/debuffs/onfire2.png"), "On Fire!", "You have been set on fire and are burning!", "Take X damage per second for the duration of this debuff.",3, "Debuff board",0)
frozen_debuff = debuff(pg.image.load(DATA_ROOT + "/data/textures/icons/debuffs/frozen.png"), "Frozen!", "You have been frozen to the bone and are struggling to move!", "For the duration of this debuff there is an X % chance to freeze completely every round.",3, "Debuff board",1)
poisoned_debuff = debuff(pg.image.load(DATA_ROOT + "/data/textures/icons/debuffs/poisoned.png"), "Poisoned!", "You have been poisoned and thus weakened!", "Take X damage per second and your attack damage and defense are lowered by X %\nfor the duration of this debuff.",3, "Debuff board",2)
wet_debuff = debuff(pg.image.load(DATA_ROOT + "/data/textures/icons/debuffs/wet.png"), "Wet!", "You and your armor have been soaked reducing your defense!", "Your defense has been reduced by X % for the duration of this debuff.",3, "Debuff board",3)
shocked_debuff = debuff(pg.image.load(DATA_ROOT + "/data/textures/icons/debuffs/shocked.png"), "Shocked!", "You have been struck with lightning making it\ndifficult to wield your weapon.", "Your attack damage has been lowered by X % for the duration of\nthis debuff.",3, "Debuff board",4)

debuff_class.debuffs = [
    on_fire_debuff,
    frozen_debuff,
    poisoned_debuff,
    wet_debuff,
    shocked_debuff
    ]

# target -> člověk na koho byl skill použit
# caster -> člověk co skill použil

class skill():
    def __init__(self, icon, name, desc, stat_desc, cooldown, belonging, shown):
        skill_class.skills.append(self)
        self.icon = icon
        self.name = name
        self.desc = desc
        self.stat_desc = stat_desc
        self.cooldown = cooldown
        # cooldown in rounds
        self.momental_cooldown = 0
        self.name_size = 100
        self.desc_size = 50
        self.stat_desc_size = 40
        self.belonging = belonging
        self.shown = shown
    
    ## Toto spustit po aktivaci skillu
    def skill_used(self, caster):
        # Načtení dat z battle_info pro práci
        if caster == "player":
            target_hp = battle_info.enemy_hp_copy
            caster_hp = battle_info.player_hp_copy
            debuff_list = debuff_class.enemy_debuffs
        elif caster == "enemy":
            target_hp = battle_info.player_hp_copy
            caster_hp = battle_info.enemy_hp_copy
            debuff_list = debuff_class.player_debuffs
        
        if self.name == "Fireball":
            target_hp -= 15
            #on_fire_debuff.active = True
            debuff_list.append(on_fire_debuff)
            if caster == "player":
                on_fire_debuff.duration_p = on_fire_debuff.duration
            elif caster == "enemy":
                on_fire_debuff.duration_e = on_fire_debuff.duration
            
        if self.name == "Ice Storm":
            target_hp -= 15
            #frozen_debuff.active = True
            debuff_list.append(frozen_debuff)
            if caster == "player":
                frozen_debuff.duration_p = frozen_debuff.duration
            elif caster == "enemy":
                frozen_debuff.duration_e = frozen_debuff.duration
            
        if self.name == "Poison Dart":
            #poisoned_debuff.active = True
            debuff_list.append(poisoned_debuff)
            if caster == "player":
                poisoned_debuff.duration_p = poisoned_debuff.duration
            elif caster == "enemy":
                poisoned_debuff.duration_e = poisoned_debuff.duration
            
        if self.name == "Life Steal":
            hp_amount = 15
            caster_hp += hp_amount
            target_hp -= hp_amount
            
        if self.name == "Water Blast":
            target_hp -= 15
            #wet_debuff.active = True
            debuff_list.append(wet_debuff)
            if caster == "player":
                wet_debuff.duration_p = wet_debuff.duration
            elif caster == "enemy":
                wet_debuff.duration_e = wet_debuff.duration
            
        if self.name == "Lightning Bolt":
            target_hp -= 15
            #shocked_debuff.active = True
            debuff_list.append(shocked_debuff)
            if caster == "player":
                shocked_debuff.duration_p = shocked_debuff.duration
            elif caster == "enemy":
                shocked_debuff.duration_e = shocked_debuff.duration
            
        if self.name == "Rock Throw":
            target_hp -= 15
            battle_info.player_turn = True
            
        # Uložení zpracovaných dat zpět do battle_info
        if caster == "player":
            battle_info.enemy_hp_copy = target_hp
            battle_info.player_hp_copy = caster_hp
            debuff_class.enemy_debuffs = debuff_list
        elif caster == "enemy":
            battle_info.player_hp_copy = target_hp
            battle_info.enemy_hp_copy = caster_hp
            debuff_class.player_debuffs = debuff_list
            
    def draw_skill(self, font, screen, on_screen):
        if on_screen.active_screen.name in self.belonging and self.shown:
            
            icon_scaled = pg.transform.scale(self.icon, (250,250))
            
            self.name_font = pg.font.Font(font, self.name_size)
            self.desc_font = pg.font.Font(font, self.desc_size)
            self.desc_stat_font = pg.font.Font(font,self.stat_desc_size)
            
            name_text = self.name_font.render(self.name, True, (0,0,0))
            name_text_rect = name_text.get_rect()
            name_text_rect.topleft = 350,330
            
            text_list = []
            pos_list = []
            i = 0
            
            for line in self.desc.split('\n'):
                text_line = self.desc_font.render(line, True, (75,75,75))
                text_list.append(text_line)
                pos = text_line.get_rect(topleft=(350, 330 + self.name_size + (self.desc_size * i)))
                pos_list.append(pos)
                i = i + 1
            
            for j in range(i):
                screen.blit(text_list[j], pos_list[j])
                
            stat_desc_text_list = []
            stat_desc_pos_list = []
            stat_desc_i = 0
            
            for stat_desc_line in self.stat_desc.split('\n'):
                stat_desc_text_line = self.desc_stat_font.render(stat_desc_line, True, (150,100,100))
                stat_desc_text_list.append(stat_desc_text_line)
                stat_desc_pos = stat_desc_text_line.get_rect(topleft=(350, pos_list[-1][1] + self.desc_size + (self.stat_desc_size * stat_desc_i)))
                stat_desc_pos_list.append(stat_desc_pos)
                stat_desc_i = stat_desc_i + 1
            
            for stat_desc_j in range(stat_desc_i):
                screen.blit(stat_desc_text_list[stat_desc_j], stat_desc_pos_list[stat_desc_j])
            
            screen.blit(icon_scaled, (100,330))
            screen.blit(name_text, name_text_rect)
            
fireball = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/fireball.png"), "Fireball", "Cast a fireball and\nshoot it at your enemy!","Deals X damage to enemy and applies the\nOn Fire! debuff.", 3, "Skill board", True)
water_blast = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/water_blast.png"), "Water Blast", "Cast a big wave of\nwater against your enemy!", "Deals X damage and applies the Wet! debuff.", 3, "Skill board", False)
rock_throw = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/rock_throw.png"), "Rock Throw", "Throw a large boulder at your enemy!", "Deals X damage to enemy and stuns them\nfor X rounds", 3, "Skill board", False)
ice_storm = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/ice_storm.png"), "Ice Storm", "Send a shower of sharp icicles\ndown on your enemy!", "Deals X damage to enemy and applies the\nFrozen! debuff.", 3, "Skill board", False)
poison_dart = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/poison_dart.png"), "Poison Dart", "Blow a poison dart at your enemy!", "Applies the Poisoned! debuff.", 3, "Skill board", False)
lightning_bolt = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/lightning_bolt.png"), "Lightning Bolt", "Shoot a lightning bolt at your enemy!", "Deals X damage to enemy and applies the\nShocked! debuff.", 3, "Skill board", False)
life_steal = skill(pg.image.load(DATA_ROOT + "/data/textures/icons/skills/life_steal.png"), "Life Steal", "Steal health for yourself\nfrom your enemy!", "Steals X health from enemy and gives it to you.", 3, "Skill board", False)

skill_class.skills = [
    fireball,
    water_blast,
    rock_throw,
    ice_storm,
    poison_dart,
    lightning_bolt,
    life_steal
    ]

# Defaultní skill
player.equipped_skills[0] = fireball
