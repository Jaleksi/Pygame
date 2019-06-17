import pygame
import math
from random import randint
from numpy import interp

#
# INPUT: SPACE = NEW TREE
#

pygame.init()
leveys = 800
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Puu")
clock = pygame.time.Clock()
oksat = []
kirsikat = []


class Oksa:
    def __init__(self, x, y, kulma, koko, vaihto, dead):
        self.x = x
        self.y = y
        self.kulma = kulma
        self.koko = koko
        self.sij = []
        self.vaihto = vaihto
        self.dead = dead

    def piirto(self):
        if(self.dead == 0):
            if(self.koko <= 1):
                self.dead = 1
                kirsikat.append(Kirsikka(self.x, self.y, 1, randint(1, 6), [255, 150, randint(155,255)]))

            elif(self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600):
                self.dead = 1

        for sijainti in self.sij:
            pygame.draw.circle(display, (0), sijainti, int(self.koko), 0)

    def halkaisu(self):
        for i in range(2):
            oksat.append(Oksa(self.x, self.y, self.kulma, int(self.koko * 0.8), 0, 0))
        self.dead = 1

    def liiku(self):
        if([self.x, self.y] not in self.sij):
            self.sij.append([self.x, self.y])

        self.x = int(self.x + (3 * math.sin(self.kulma)))
        self.y = int(self.y + (3 * math.cos(self.kulma)))

        if(randint(0, 5) == 1):
            self.vaihto = math.pi/72
        elif(randint(0, 5) == 1):
            self.vaihto = -(math.pi/72)

        self.kulma += self.vaihto


class Kirsikka:
    def __init__(self, x, y, koko, maxkoko, vari):
        self.x = x
        self.y = y
        self.koko = koko
        self.maxkoko = maxkoko
        self.vari = vari

    def piirto(self):
        pygame.draw.circle(display, self.vari, [self.x, self.y], self.koko, 0)

    def kasvu(self):
        if(self.koko <= self.maxkoko):
            self.koko += 1


def inbut():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                oksat.clear()
                kirsikat.clear()
                alku()


def alku():
    oksat.append(Oksa(400, 600, math.pi, 25, 0, 0))


def growTree(seed, berry):
    for oksa in seed:
        if(oksa.dead == 0):
            oksa.liiku()
            if(randint(0, 100) <= 3):
                oksa.halkaisu()
        oksa.piirto()
    for kirsikka in berry:
        kirsikka.piirto()
        kirsikka.kasvu()



def main():
    alku()
    while(True):
        inbut()
        display.fill(pygame.Color("white"))
        growTree(oksat, kirsikat)
        clock.tick(30)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
