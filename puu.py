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
pygame.display.set_caption("Buu")
clock = pygame.time.Clock()
oksat = []


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
        if(self.koko <= 1 or self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600):
            self.dead = 1

        for sijainti in self.sij:
            pygame.draw.circle(display, (255, 255, 255), sijainti, int(self.koko), 0)

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


def inbut():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                oksat.clear()
                alku()


def alku():
    oksat.append(Oksa(400, 600, math.pi, 25, 0, 0))


def main():
    alku()
    while(True):
        inbut()
        display.fill(pygame.Color("black"))
        for oksa in oksat:
            if(oksa.dead == 0):
                oksa.liiku()
                if(randint(0, 100) <= 3):
                    oksa.halkaisu()
            oksa.piirto()
        clock.tick(30)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
