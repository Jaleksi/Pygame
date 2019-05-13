import pygame
import random
from numpy import interp

pygame.init()
pygame.font.init()
leveys = 600
korkeus = 600

display = pygame.display.set_mode((korkeus, leveys))
pygame.display.set_caption("ZzzZzz")
clock = pygame.time.Clock()

class Viiva:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.suunta = 0
        self.color = pygame.Color("black")

    def piirto(self):
        self.pos = [int(self.x), int(self.y)]
        self.pos2 = [int(300+self.vali), int(self.y)]
        pygame.draw.circle(display, self.color, self.pos, 3, 0)
        pygame.draw.circle(display, self.color, self.pos2, 3, 0)
        pygame.draw.line(display, self.color, self.pos, self.pos2, 1)

    def varivaihto(self):
        if(self.color == pygame.Color("black")):
            self.color = pygame.Color("red")
        else:
            self.color = pygame.Color("black")
    def heilu(self):
        self.vali = 300-self.x
        self.vauhti = interp(self.vali, [0, 100], [5, 1])

        if(self.vali > 99 and self.suunta == 0):
            self.suunta = 1
        elif(self.vali < 1 and self.suunta == 1):
            self.suunta = 0
            self.varivaihto()

        if(self.suunta == 0):
            self.x -= self.vauhti
        else:
            self.x += self.vauhti

def inputt():
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()


def main():
    maara = 41
    y = int(korkeus/maara)
    x = 300
    viivat = []
    for i in range(1, maara):
        viivat.append(Viiva(x, y))
        y += int(korkeus/maara)
        x += 20
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        for viiva in viivat:
            viiva.heilu()
            viiva.piirto()
        pygame.display.update()
        clock.tick(30)

if(__name__ == "__main__"):
    main()
