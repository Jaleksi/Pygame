import pygame
from random import randint

#
# INPUT: MOUSE CLICK FOR NEW THING, C TO CLEAR.
#

pygame.init()
leveys = 600
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Juttu")
clock = pygame.time.Clock()
pallot = []

class Pallo:
    def __init__(self, x, y, vari, koko):
        self.x = x
        self.y = y
        self.vari = vari
        self.koko = koko
        self.koot = []
        self.sij = []

    def piirto(self):
        for i in range(len(self.sij)):
            pygame.draw.circle(display, (0), self.sij[i], int(self.koot[i])+1, 1)
            pygame.draw.circle(display, self.vari, self.sij[i], int(self.koot[i]), 0)

    def liiku(self):
        if(self.koko <= 1):
            return 0
        self.sij.append([self.x, self.y])
        self.koot.append(self.koko)
        self.x += randint(0, 6)
        self.y -= randint(-3, 6)
        self.koko -= 0.5

def uusipallo(hx, hy):
    x = 5
    for i in range(x):
        color = randint(0, 255)
        pallot.append(Pallo(hx, hy, [255, color, color], randint(15, 30)))


def inputt():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mx, my = pygame.mouse.get_pos()
            uusipallo(mx, my)
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_c):
                pallot.clear()


def main():
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        for pallo in pallot:
            pallo.piirto()
            pallo.liiku()
        clock.tick(30)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
