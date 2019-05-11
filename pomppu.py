import pygame
import random

pygame.init()
leveys = 300
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Juttu")
clock = pygame.time.Clock()


class bal:
    palloleveys = 150
    pallokorkeus = 100
    suunta = 0
    vauhti = 0
    sivusuunta = random.randint(0,1)
    sivuvauhti = 5


def pallo(x ,y):
    if(bal.suunta == 0):
        bal.vauhti += 1
    elif(bal.suunta == 1):
        bal.vauhti -=1
    if(bal.palloleveys > 250):
        bal.palloleveys = 250
        bal.sivusuunta = 1
        bal.sivuvauhti = int(bal.sivuvauhti * 0.8)
    if(bal.palloleveys < 50):
        bal.palloleveys = 50
        bal.sivusuunta = 0
        bal.sivuvauhti = int(bal.sivuvauhti * 0.8)
    pygame.draw.circle(display, (0, 0, 255), (x, y), 50, 0)

def liikutus():
    if(bal.pallokorkeus > 549):
        bal.pallokorkeus = 550
        if(bal.sivuvauhti > 0):
            bal.sivuvauhti -= 1
    if(bal.suunta == 0):  # alas
        bal.pallokorkeus += bal.vauhti
    if(bal.suunta == 1):  # ylös
        bal.pallokorkeus -= bal.vauhti
    if(bal.sivusuunta == 0):  # oikea
        bal.palloleveys += bal.sivuvauhti
    if(bal.sivusuunta == 1):  # vasen
        bal.palloleveys -= bal.sivuvauhti

def main():
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    bal.pallokorkeus = 100
                    bal.suunta = 0
                    bal.vauhti = 0
                    bal.sivusuunta = random.randint(0,1)
                    bal.sivuvauhti = random.randint(5,30)
        display.fill(pygame.Color("white"))
        if(bal.pallokorkeus > 549):
            bal.suunta = 1
            bal.vauhti = int(bal.vauhti * 0.7)
        if(bal.vauhti < 1):
            bal.suunta = 0
        pallo(bal.palloleveys, bal.pallokorkeus)
        liikutus()
        clock.tick(40)
        pygame.display.update()
if(__name__ == "__main__"):
    main()
