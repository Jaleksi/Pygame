import pygame
from random import randint


pygame.init()
leveys = 500
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Mato")
clock = pygame.time.Clock()
gameon = False

def inbut():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            for valinta in valinnat:
                if(valinta.valittu == True and valinta.msg == "Uusi peli"):
                    gameon = True
                    peli()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                pass

class Teksti:
    def __init__(self, msg, koko, x, y, vari):
        self.msg = msg
        self.koko = koko
        self.x = x
        self.y = y
        self.vari = vari
        self.valittu = False

    def piirto(self):
        self.teksti = pygame.font.SysFont("Arial", self.koko)
        self.rend = self.teksti.render(self.msg, True, self.vari)

        self.rect = self.rend.get_rect(center=(leveys/2, self.y))
        display.blit(self.rend, self.rect)

    def klik(self):
        mx, my = pygame.mouse.get_pos()
        self.x2, self.y2, self.w, self.h = self.rend.get_rect()
        if(self.y-self.h/2 < my < self.y+self.h/2 and 200<mx<400):
            self.vari = (0, 255, 0)
            self.valittu = True
        else:
            self.vari = (0, 0, 0)
            self.valittu = False

valinnat = [Teksti("Uusi peli", 24, 0, 350, (0, 0, 0)),
            Teksti("Hiscores", 24, 0, 400, (0, 0, 0)),
            Teksti("Lopeta", 24, 0, 450, (0, 0, 0))]

def main():
    while(True):
        display.fill(pygame.Color("white"))
        inbut()
        otsikko = Teksti("Matopeli", 36, 0, 100, (0, 0, 0))
        otsikko.piirto()
        for valinta in valinnat:
            valinta.piirto()
            valinta.klik()

        clock.tick(10)
        pygame.display.update()

class Mato:
    def __init__(self, x, y):
        self.xnopeus = 0
        self.ynopeus = 10
        self.kokomato = []
        self.paa = pygame.Rect(x, y, 10, 10)
        self.kokomato.append(self.paa)

    def matopiirto(self):
        for osa in self.kokomato:
            pygame.draw.rect(display, (0, 255, 0), osa, 2)

    def matoliiku(self):
        uusipaa = pygame.Rect(self.paa.x + self.xnopeus,
                              self.paa.y + self.ynopeus,
                              10, 10)
        if(uusipaa.x > 500):
            uusipaa.x = 0
        elif(uusipaa.x < 0):
            uusipaa.x = 500
        if(uusipaa.y > 500):
            uusipaa.y = 100
        elif(uusipaa.y < 100):
            uusipaa.y = 500

        self.kokomato.insert(0, uusipaa)
        self.paa = uusipaa
        self.kokomato.pop()


def peli():
    mato = Mato(0, 100)
    while(True):
        inbut()
        display.fill(pygame.Color("white"))
        mato.matoliiku()
        mato.matopiirto()
        clock.tick(10)
        pygame.display.update()



if(__name__ == "__main__"):
    main()
