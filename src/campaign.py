import sys
import pygame as pg
import random
from skills import *
from text import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
tp_size = (135,378)
    
class Level():
    def __init__(self, number):
        self.number = number
        self.completed = False
        self.unlocked = False
        
    def get_enemies(self, enemies):
        self.enemies = enemies
        
    def get_rewards(self, xp, gold):
        self.gold_reward = gold
        self.xp_reward = xp
        
class Counter():
    def __init__(self):
        self.number = 1
        self.font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", 100)
        texture = pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png")
        self.lock = pg.transform.scale(texture, (80,80))
        
    def blit_self(self, screen, on_screen):
        if on_screen.active_screen.name == "Campaign":
            for l in levels:
                if l.unlocked == False:
                    end_index = l.number
                    break
            if self.number < end_index:
                text = str(self.number)
                if self.number % 5 == 0:
                    surf = self.font.render(text, True, (190,20,20))
                elif levels[self.number - 1].completed:
                    surf = self.font.render(text, True, (40,100,15))
                else:
                    surf = self.font.render(text, True, (30,30,30))
                width = self.font.size(text)[0]
                screen.blit(surf, ((600 - (width / 2)+2),754))
            elif self.number == end_index:
                screen.blit(self.lock, (562, 760))
        
    def up(self):
        for l in levels:
            if l.unlocked == False:
                end_index = l.number
                break
        if not self.number == 20 and self.number < end_index:
            self.number += 1
        
    def down(self):
        if not self.number == 1:
            self.number -= 1
            
class Enemy():
    def __init__(self, name, texture, hp, damage, armor):
        self.name = name
        self.position = (800,450)
        width = texture.get_width()
        height = texture.get_height()
        self.texture = pg.transform.scale(texture, (width * 9, height * 9))
        self.width = self.texture.get_width()
        self.height = self.texture.get_height()
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.id = "enemy"
        
class Mini_boss():
    def __init__(self, name, texture, hp, damage, armor, skill):
        self.name = name
        self.position = (800,450)
        width = texture.get_width()
        height = texture.get_height()
        self.texture = pg.transform.scale(texture, (width * 11, height * 11))
        self.width = self.texture.get_width()
        self.height = self.texture.get_height()
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.skill = skill
        self.id = "mini_boss"
        
class Battle_info():
    def start(self):
        self.player_turn = True
        self.pause = False
        self.hp_color = (190,50,50)
        self.hp_background_color = (130,10,10)
        self.mana_color = (80,110,200)
        self.mana_background_color = (20,50,130)
        self.bar_width = 300
        self.cooldown_texts = range(11)
        for s in player.equipped_skills:
            if not s == None:
                s.momental_cooldown = 0
        self.cooldown_tick = True
        
    def get_info(self, level):
        self.level = level
        self.stages = (len(level.enemies) - 1)
        self.stage = 0
        self.active_enemy = level.enemies[self.stage]
        self.enemy_hp_copy = level.enemies[self.stage].hp
        self.enemy_max_hp = self.enemy_hp_copy
        self.enemy_effects = {"damage_ef" : 0, "defense_ef" : 0}
        for d in debuff_class.debuffs:
            d.duration_e = 0
        self.mb_skill_chance = 0
        self.icon_memory_now = self.active_enemy.texture
        if not self.stages == self.stage:
            self.icon_memory_next = level.enemies[self.stage + 1].texture
        else:
            self.icon_memory_next = None
    
    def make_player(self, player):
        self.player_copy = player
        self.player_max_hp = player.max_hp
        self.player_hp_copy = player.max_hp
        self.player_max_mana = player.max_mana
        self.player_mana_copy = player.max_mana
        self.player_texture_copy = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/characters/player/player.png"), tp_size)
        self.awaiting_skill = None
        self.player_effects = {"damage_ef" : 0, "defense_ef" : 0}
        for d in debuff_class.debuffs:
            d.duration_p = 0
        text_class.counter_texts[0].update(str(player.inventory["healing_potion"]), None)
        text_class.counter_texts[1].update(str(player.inventory["mana_potion"]), None)
        
    def blit_player(self, screen):
        screen.blit(self.player_texture_copy, (180, 285))
        
    def blit_player_icon(self, screen):
        icon = pg.transform.scale(self.player_texture_copy, (30,86))
        width, height = icon.get_size()
        screen.blit(icon, (108 - (width / 2), 820 - (height / 2)))
        
    def blit_enemy(self, screen):
        if not self.active_enemy == None:
            screen.blit(self.active_enemy.texture, (1020 - self.active_enemy.width, 663 - self.active_enemy.height))
            
    def blit_enemy_icon(self, screen):
        icon_now = pg.transform.scale(self.icon_memory_now, ((self.icon_memory_now.get_size()[0] / 9) * 2, (self.icon_memory_now.get_size()[1] / 9) * 2))
        width, height = icon_now.get_size()
        screen.blit(icon_now, (1088 - (width / 2), 80 - (height / 2)))
        if not self.icon_memory_next == None:
            icon_next = pg.transform.scale(self.icon_memory_next, ((self.icon_memory_next.get_size()[0] / 9) * 2, (self.icon_memory_next.get_size()[1] / 9) * 2))
            width, height = icon_next.get_size()
            screen.blit(icon_next, (284 - (width / 2), 80 - (height / 2)))
        
    def fight(self):
        # Útok hráče
        if self.player_turn and self.awaiting_skill == None:
            damage = (self.player_copy.weapon.damage * ((100 - self.player_effects["damage_ef"]) / 100)) * ((100 - self.active_enemy.armor + self.enemy_effects["defense_ef"]) / 100)
            damage = round(damage)
            if damage >= 0:
                self.enemy_hp_copy -= damage
            else:
                pass
            self.player_turn = False
        # Použití skillu
        elif self.player_turn and not self.awaiting_skill == None:
            self.player_turn = False
            self.awaiting_skill.skill_used("player", battle_info)
            self.awaiting_skill = None
        # Útok nepřítele
        else:
            if not self.enemy_hp_copy <= 0:
                used_skill = False
                if self.active_enemy.id == "mini_boss":
                    if self.mb_skill_chance > 1:
                        r = random.randint(2, 12)
                        if self.mb_skill_chance > r:
                            self.active_enemy.skill.skill_used("enemy", battle_info)
                            self.mb_skill_chance = 0
                            used_skill = True
                        else:
                            self.mb_skill_chance += 1
                    else:
                        self.mb_skill_chance += 1
                
                if not used_skill:
                    if self.player_copy.armor == None:
                        damage = (self.active_enemy.damage * ((100 - self.enemy_effects["damage_ef"]) / 100)) * ((100 + self.player_effects["defense_ef"]) / 100)
                        damage = round(damage)
                        if damage >= 0:
                            self.player_hp_copy -= damage
                        else:
                            pass
                    else:
                        damage = (self.active_enemy.damage * ((100 - self.enemy_effects["damage_ef"]) / 100)) * ((100 - self.player_copy.armor.armor + self.player_effects["defense_ef"]) / 100)
                        damage = round(damage)
                        if damage >= 0:
                            self.player_hp_copy -= damage
                        else:
                            pass
            self.player_turn = True
            
    def pause_battle(self):
        self.pause = True
        
    def unpause_battle(self):
        self.pause = False
            
    def check_fight(self, on__screen, button_class, small_xp_bar):
        if not self.active_enemy == None:
            self.fight()
        if self.enemy_hp_copy <= 0 and not self.active_enemy == None:
            self.active_enemy = None
            self.player_turn = True
        elif self.player_hp_copy <= 0:
            self.pause_battle()
            for table in on__screen.tables:
                if table.name == "Death table":
                    on__screen.active_table = table
        elif self.active_enemy == None:
            self.stage += 1
            if self.stage <= self.stages:
                self.active_enemy = self.level.enemies[self.stage]
                self.enemy_hp_copy = self.level.enemies[self.stage].hp
                self.enemy_max_hp = self.enemy_hp_copy
                self.enemy_effects = {"damage_ef" : 0, "defense_ef" : 0}
                for d in debuff_class.debuffs:
                    d.duration_e = 0
                self.icon_memory_now = self.active_enemy.texture
                if not self.stages == self.stage:
                    self.icon_memory_next = self.level.enemies[self.stage + 1].texture
                else:
                    self.icon_memory_next = None
            else:
                self.pause_battle()
                if not self.level.number == 20:
                    for table in on__screen.tables:
                        if table.name == "Win table":
                            on__screen.active_table = table
                else:
                    for table in on__screen.tables:
                        if table.name == "Final win table":
                            on__screen.active_table = table
                button_class, small_xp_bar = self.rewards(button_class, small_xp_bar)
        
        if self.cooldown_tick:
            self.cooldown_tick = False
            for s in player.equipped_skills:
                if not s == None:
                    if s.momental_cooldown > 0:
                        s.momental_cooldown -= 1
        else:
            self.cooldown_tick = True
        
        return button_class, small_xp_bar
    
    def rewards(self, button_class, small_xp_bar):
        str_first_gold = str(player.gold)
        str_first_xp = str(player.xp)
        str_first_req = str(player.xp_req)
        
        # Přidání odměn
        if levels[counter.number - 1].completed == False:
            gold_gain = int(levels[counter.number - 1].gold_reward * (1 + (player.luck_stat / 25)))
            player.gold += gold_gain
            xp_gain = int(levels[counter.number - 1].xp_reward * (1 + (player.int_stat / 25)))
            player.xp += xp_gain
        else:
            gold_gain = int(levels[counter.number - 1].gold_reward * (1 + (player.luck_stat / 25) - 0.5))
            player.gold += gold_gain
            xp_gain = int(levels[counter.number - 1].xp_reward * (1 + (player.int_stat / 25) - 0.6))
            player.xp += xp_gain
        next_level = player.calculate_level()
        
        new_skill = False
        for en in self.level.enemies:
            if en.id == "mini_boss":
                if not en.skill in player.skills:
                    player.skills.append(en.skill)
                    new_skill = True
                    index = len(player.skills) - 1
                    button_class.skill_buttons[index].get_texture(en.skill.icon)
        
        # Zpráva na tabulce
        index_new_gold = text_class.texts.index(gold_gained)
        text_class.texts[index_new_gold].update("Your gold: " + str_first_gold + " + " + str(gold_gain), None)
        index_new_xp = text_class.texts.index(xp_gained)
        text_class.texts[index_new_xp].update("Your experience: " + str_first_xp + " + " + str(xp_gain) + "/" + str_first_req, None)
        index_new_lvl = text_class.texts.index(new_level)
        index_new_skill = text_class.texts.index(new_skill_1)
        
        if next_level:
            text_class.texts[index_new_lvl].show = True
            text_class.texts[index_new_lvl + 1].show = True
        else:
            text_class.texts[index_new_lvl].show = False
            text_class.texts[index_new_lvl + 1].show = False
        if new_skill:
            text_class.texts[index_new_skill].show = True
            text_class.texts[index_new_skill + 1].show = True
        else:
            text_class.texts[index_new_skill].show = False
            text_class.texts[index_new_skill + 1].show = False
        
        if next_level:
            pass
        else:
            small_xp_bar.get_xp_difference(xp_gain)
        
        return button_class, small_xp_bar
    
    def show_bars(self, screen):
        if not self.active_enemy == None:
            max_enemy_hp = self.active_enemy.hp
        # HP bar nepřítele
        for t in text_class.texts:
            if t.id == "e_hp":
                t.update(str(self.enemy_hp_copy) + "/" + str(self.enemy_max_hp), None)
        pg.draw.rect(screen, self.hp_background_color, (765, 35, self.bar_width, 44))
        pg.draw.rect(screen, self.hp_color, (765,35,(self.bar_width * (self.enemy_hp_copy / self.enemy_max_hp)),44))
        
        pg.draw.rect(screen, self.mana_background_color, (765, 80, self.bar_width, 44))
        
        # HP a mana bar hráčes
        for t in text_class.texts:
            if t.id == "p_hp":
                t.update(str(self.player_hp_copy) + "/" + str(self.player_max_hp), None)
        pg.draw.rect(screen, self.hp_background_color, (135, 775, self.bar_width, 44))
        pg.draw.rect(screen, self.hp_color, (135,775,(self.bar_width * (self.player_hp_copy / self.player_max_hp)),44))
        for t in text_class.texts:
            if t.id == "p_mana":
                t.update(str(self.player_mana_copy) + "/" + str(self.player_max_mana), None)
        pg.draw.rect(screen, self.mana_background_color, (135, 820, self.bar_width, 44))
        pg.draw.rect(screen, self.mana_color, (135, 820,(self.bar_width * (self.player_mana_copy / self.player_max_mana)),44))
    
    def show_turn(self, screen):
        width = 70
        height = 30
        if self.player_turn:
            pg.draw.polygon(screen, (40,180,40), ( (248,680),((248 - (width / 2)), (680 + height)),((248 + (width / 2)),(680 + height))) )
        else:
            middle = 1020 - (self.active_enemy.width / 2)
            pg.draw.polygon(screen, (40,180,40), ( (middle,680),((middle - (width / 2)), (680 + height)),((middle + (width / 2)),(680 + height))) )
            
    def show_cooldown(self, button_class, screen):
        if self.awaiting_skill == None:
            for b in button_class.buttons:
                if b.tasks[0][0] == "activate_skill":
                    b.draw = False
                if b.tasks[0][0] == "drink_potion":
                    b.draw = False
            for t in text_class.cooldown_texts:
                t.show = False
        for i in range(len(player.equipped_skills)):
            if not player.equipped_skills[i] == None:
                if player.equipped_skills[i].momental_cooldown > 0:
                    for b in button_class.buttons:
                        if b.tasks[0][0] == "activate_skill" and b.tasks[0][1] == i:
                            b.draw = "c"
                            
                    text_class.cooldown_texts[i].text = str(player.equipped_skills[i].momental_cooldown)
                    text_class.cooldown_texts[i].show = True
        
        return button_class.buttons
    
    def show_debuffs(self, screen):
        sort_list = []
        info_list = [[0,0],[0,0],[0,0]]
        index_list = []
        position = 0
        offset = 0
        # Vykreslení debuffů u nepřítele
        for i in range(len(debuff_class.debuffs)):
            if debuff_class.debuffs[i].duration_e > 0:
                sort_list.append(debuff_class.debuffs[i].duration_e)
                info_list[position][0] = debuff_class.debuffs[i].duration_e
                info_list[position][1] = i
                position += 1
        sort_list.sort(reverse=True)
        
        for li in sort_list:
            for l in info_list:
                if li == l[0]:
                    index_list.append(l[1])
                    
        for i in index_list:
            icon = pg.transform.scale(debuff_class.debuffs[i].icon, (64,64))
            icon_size = [icon.get_width(), icon.get_height()]
            screen.blit(icon, (((558 - (icon_size[0] / 2)) + (77 * offset)),(82 - (icon_size[1] / 2))))
            offset += 1
            
        sort_list = []
        info_list = [[0,0],[0,0],[0,0]]
        index_list = []
        position = 0
        offset = 0
        # Vykreslení debuffů u hráče
        for i in range(len(debuff_class.debuffs)):
            if debuff_class.debuffs[i].duration_p > 0:
                sort_list.append(debuff_class.debuffs[i].duration_p)
                info_list[position][0] = debuff_class.debuffs[i].duration_p
                info_list[position][1] = i
                position += 1
        sort_list.sort(reverse=True)
        
        for li in sort_list:
            for l in info_list:
                if li == l[0]:
                    index_list.append(l[1])
                    
        for i in index_list:
            icon = debuff_class.debuffs[i].icon
            icon_size = [icon.get_width(), icon.get_height()]
            screen.blit(icon, (((490 - (icon_size[0] / 2)) + (77 * offset)),(822 - (icon_size[1] / 2))))
            offset += 1
        
    def check_debuffs(self):
        for d in debuff_class.debuffs:
            self.player_hp_copy, self.player_effects, self.enemy_effects, self.player_turn = d.debuff_tick(self.player_copy, self.player_hp_copy, self.player_effects, self.enemy_effects, self.player_turn)
            self.enemy_hp_copy, self.player_effects, self.enemy_effects, self.player_turn = d.debuff_tick(self.active_enemy, self.enemy_hp_copy, self.player_effects, self.enemy_effects, self.player_turn)
        
battle_info = Battle_info()
        
counter = Counter()
levels = []

for i in range(1,21):
    levels.append(Level(i))

levels[0].unlocked = True

# Nepřátelé
slime = Enemy("Slime", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/slime.png"), 30, 5, 10)
zombie = Enemy("Zombie", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/zombie.png"), 60, 10, 20)
skeleton = Enemy("Skeleton", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/skeleton.png"), 70, 15, 0)
fire_slime = Enemy("Fire slime", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/fire_slime.png"), 50, 16, 10)
goblin = Enemy("Goblin", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/goblin.png"), 80, 18, 15)
ogre = Enemy("Orge", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/ogre.png"), 300, 18, 10)
# Mini bossové
death_lord = Mini_boss("Death lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/reaper.png"), 500, 10, 20, skill_class.skills[6])
stone_lord = Mini_boss("Stone lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/gnome.png"), 200, 10, 40, skill_class.skills[2])
ice_lord = Mini_boss("Ice lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/gnome.png"), 400, 10, 30, skill_class.skills[3])
# Zařazení nepřátel do levelu
levels[0].get_enemies([slime])
levels[1].get_enemies([zombie, slime])
levels[2].get_enemies([slime, zombie, slime])
levels[3].get_enemies([zombie, skeleton])
levels[4].get_enemies([stone_lord])
levels[5].get_enemies([slime, slime, fire_slime, slime, slime])
levels[6].get_enemies([zombie, fire_slime, skeleton])
levels[7].get_enemies([zombie, goblin])
levels[8].get_enemies([skeleton, goblin, goblin, fire_slime])
levels[9].get_enemies([skeleton, ice_lord])
levels[10].get_enemies([zombie, skeleton, fire_slime, skeleton, goblin])
levels[11].get_enemies([ogre, slime, fire_slime])
levels[12].get_enemies([goblin, skeleton, goblin, fire_slime, zombie])
levels[13].get_enemies([ogre, goblin, ogre])
levels[14].get_enemies([skeleton, skeleton, skeleton, death_lord])
levels[15].get_enemies([ogre, fire_slime, goblin, skeleton, skeleton])
levels[16].get_enemies([ogre, slime, ogre])
levels[17].get_enemies([goblin, zombie, skeleton, ogre, fire_slime, ogre])
levels[18].get_enemies([ogre, ogre, ogre])
levels[19].get_enemies([stone_lord, ice_lord, death_lord])

# XP, pak Goldy
levels[0].get_rewards(50,50)
levels[1].get_rewards(60,80)
levels[2].get_rewards(75,120)
levels[3].get_rewards(90,130)
levels[4].get_rewards(100,140)
levels[5].get_rewards(120,160)
levels[6].get_rewards(170,280)
levels[7].get_rewards(180,300)
levels[8].get_rewards(190,320)
levels[9].get_rewards(200,350)
levels[10].get_rewards(210,375)
levels[11].get_rewards(220,400)
levels[12].get_rewards(240,430)
levels[13].get_rewards(250,460)
levels[14].get_rewards(270,490)
levels[15].get_rewards(280,540)
levels[16].get_rewards(300,560)
levels[17].get_rewards(330,600)
levels[18].get_rewards(360,666)
levels[19].get_rewards(0,0)
