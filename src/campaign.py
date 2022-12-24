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
        self.texture = pg.transform.scale(texture, (width * 9, height * 9))
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
        
    def blit_enemy(self, screen):
        if not self.active_enemy == None:
            screen.blit(self.active_enemy.texture, (1020 - self.active_enemy.width, 663 - self.active_enemy.height))
        
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
            else:
                self.pause_battle()
                for table in on__screen.tables:
                    if table.name == "Win table":
                        on__screen.active_table = table
                button_class, small_xp_bar = self.rewards(button_class, small_xp_bar)
        
        for s in player.equipped_skills:
            if not s == None:
                if s.momental_cooldown > 0:
                    s.momental_cooldown -= 1
        
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
            gold_gain = int(levels[counter.number - 1].gold_reward * (1 + (player.luck_stat / (25 - 40))))
            player.gold += gold_gain
            xp_gain = int(levels[counter.number - 1].xp_reward * (1 + (player.int_stat / (25 - 60))))
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
        # HP a mana bar hráče
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
zombie = Enemy("Zombie", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/zombie.png"), 50, 5, 30)
slime = Enemy("Slime", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/slime.png"), 20, 2, 0)
# Mini bossové
water_lord = Mini_boss("Water lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/gnome.png"), 100, 10, 35, skill_class.skills[1])
stone_lord = Mini_boss("Stone lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/gnome.png"), 100, 10, 35, skill_class.skills[2])
ice_lord = Mini_boss("Ice lord", pg.image.load(DATA_ROOT + "/data/textures/characters/enemy/gnome.png"), 100, 10, 35, skill_class.skills[3])
# Zařazení nepřátel do levelu
levels[0].get_enemies([slime])
levels[1].get_enemies([zombie])
levels[2].get_enemies([zombie])
levels[3].get_enemies([zombie])
levels[4].get_enemies([zombie])
levels[5].get_enemies([zombie])
levels[6].get_enemies([zombie])
levels[7].get_enemies([zombie])
levels[8].get_enemies([zombie])
levels[9].get_enemies([zombie])
levels[10].get_enemies([zombie])
levels[11].get_enemies([zombie])
levels[12].get_enemies([zombie])
levels[13].get_enemies([zombie])
levels[14].get_enemies([zombie])
levels[15].get_enemies([zombie])
levels[16].get_enemies([zombie])
levels[17].get_enemies([zombie])
levels[18].get_enemies([zombie])
levels[19].get_enemies([zombie])

levels[0].get_rewards(10,50)
levels[1].get_rewards(10,50)
levels[2].get_rewards(10,50)
levels[3].get_rewards(10,50)
levels[4].get_rewards(10,50)
levels[5].get_rewards(10,50)
levels[6].get_rewards(10,50)
levels[7].get_rewards(10,50)
levels[8].get_rewards(10,50)
levels[9].get_rewards(10,50)
levels[10].get_rewards(10,50)
levels[11].get_rewards(10,50)
levels[12].get_rewards(10,50)
levels[13].get_rewards(10,50)
levels[14].get_rewards(10,50)
levels[15].get_rewards(10,50)
levels[16].get_rewards(10,50)
levels[17].get_rewards(10,50)
levels[18].get_rewards(10,50)
levels[19].get_rewards(10,50)
