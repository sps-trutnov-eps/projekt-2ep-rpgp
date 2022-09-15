# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

rozliseni = 1200, 900

pygame.init()

okno = pygame.display.set_mode(rozliseni)
pygame.display.set_caption("Generická hra")


while True:
    udalosti = pygame.event.get()
    okno.fill((50,200,50))
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()