import pygame as pg
import sys
import random
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
class debuff():
    def __init__(self, icon, name, desc, stat_desc, duration):
        self.icon = icon
        self.name = name
        self.desc = desc
        self.stat_desc = stat_desc
        self.active = False
        self.duration = duration
        self.active_for = 0
        
    ## Toto spustit každé kolo, i když není žádný debuff aktivní
    def debuff_tick(self):
        if self.name == "On Fire!":
            while self.active == True and active_for <= duration:
                active_for += 1
                player.hp -= 1 # Toto číslo se dá pozměnit
                
            else:
                self.active == False
            
        if self.name == "Frozen!":
            while self.active == True and active_for <= duration:
                active_for += 1
                stun_chance = random.randint(0, 4) # tyto čísla jdou poupravit pro zvednutí šance na stun
                if stun_chance == 4:
                    ### Zde kód na zastavení akcí hráče (stun) ###
                    pass
                
            else:
                self.active == False
            
        if self.name == "Poisoned!":
            while self.active == True and active_for <= duration:
                active_for += 1
                player.hp -= 1 # Toto číslo se dá pozměnit
                ### Nevím jak se kalkuluje damage a defense, takže to je potřeba dodělat
            
        if self.name == "Wet!":
            while self.active == True and active_for <= duration:
                active_for += 1
                ### Opět nevím jak se kalkuluje defense
            
            else:
                self.active == False
            
        if self.name == "Shocked!":
            while self.active == True and active_for <= duration:
                active_for += 1
                ### Zas a znovu nevím jak se kalkuluje damage
            
            else:
                self.active == False
            
        else:
            pass

on_fire_debuff = debuff(None, "On Fire!", "You have been set on fire and are burning!", "Take X damage per second for the duration of this debuff.")
frozen_debuff = debuff(None, "Frozen!", "You have been frozen to the bone and are struggling to move!", "For the duration of this debuff there is an X % chance to freeze completely every round.")
poisoned_debuff = debuff(None, "Poisoned!", "You have been poisoned and thus weakened!", "Take X damage per second and your attack damage and defense are lowered by X % for the duration of this debuff.")
wet_debuff = debuff(None, "Wet!", "You and your armor have been soaked reducing your defense!", "Your defense has been reduced by X % for the duration of this debuff.")
shocked_debuff = debuff(None, "Shocked!", "You have been struck with lightning making it difficult to wield your weapon.", "Your attack damage has been lowered by X % for the duration of this debuff.")

# target -> člověk na koho byl skill použit
# caster -> člověk co skill použil

class skill():
    def __init__(self, icon, name, desc, cooldown):
        self.icon = icon
        self.name = name
        self.desc = desc
        self.cooldown = cooldown
        # cooldown in rounds
    
    ## Toto spustit po aktivaci skillu
    def skill_used(self, caster, target):
        # target = enemy ### Nevím kde jsou data nepřítele
        if self.name == "Fireball" and self.cooldown == 0:
            target.hp -= 15
            on_fire_debuff.active = True
            
        if self.name == "Ice Storm" and self.cooldown == 0:
            target.hp -= 15
            frozen_debuff.active = True
            
        if self.name == "Poison Dart" and self.cooldown == 0:
            poisoned_debuff.active = True
            
        if self.name == "Life Steal" and self.cooldown == 0:
            hp_amount = 15
            caster.hp += hp_amount
            target.hp -= hp_amount
            
        if self.name == "Water Blast" and self.cooldown == 0:
            target.hp -= 15
            wet_debuff.active = True
            
        if self.name == "Lightning Bolt" and self.cooldown == 0:
            target.hp -= 15
            shocked_debuff.active = True
            
        if self.name == "Rock Throw" and self.cooldown == 0:
            target.hp -= 15
            ### Zde kód na zastavení akcí hráče (stun) ###
            
fireball = skill(None, "Fireball", "Cast a fireball and shoot it at your enemy!", 3)
ice_storm = skill(None, "Ice Storm", "Send a shower of sharp icicles down on your enemy!", 3)
poison_dart = skill(None, "Poison Dart", "Blow a poison dart at your enemy!", 3)
life_steal = skill(None, "Life Steal", "Steal health for yourself from your enemy!", 3)
water_blast = skill(None, "Water Blast", "Cast a big wave of water against your enemy!", 3)
lightning_bolt = skill(None, "Lightning Bolt", "Shoot a lightning bolt at your enemy!", 3)
rock_throw = skill(None, "Rock Throw", "Throw a large boulder at your enemy!", 3)