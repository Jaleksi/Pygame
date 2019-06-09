import pygame
from random import randint
from numpy import interp

pygame.init()
leveys = 600
korkeus = 300
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Title")
clock = pygame.time.Clock()
palkit = []

class Palkki:
    def __init__(self, x, y, speed, suunta, raja):
        self.x = x
        self.y = y
        self.leveys = 5
        self.speed = speed
        self.suunta = suunta
        self.raja = raja

    def piirto(self):
        self.korkeus = 150-self.y
        self.pos = [self.x, self.y, self.leveys, self.korkeus]
        self.color1 = interp(abs(self.korkeus), [0, 150], [235, 20])
        self.color2 = interp(self.x, [0, 600], [20, 235])
        pygame.draw.rect(display, [self.color1, self.color1, self.color2] , self.pos, 0)

    def suuntavaihto(self):
        if(self.suunta == 1):
            self.suunta = 0
        else:
            self.suunta = 1

    def heilu(self):
        if(self.suunta == 1):
            if(self.y < self.raja):
                self.suuntavaihto()
                self.speed = randint(1, 2)
                self.raja = randint(150, 250)
            else:
                self.y -= self.speed
        else:
            if(self.y > self.raja):
                self.suuntavaihto()
                self.speed = randint(1, 2)
                self.raja = randint(50, 150)
            else:
                self.y += self.speed

def luopalkki(maara):
    x = int(leveys/maara)
    y = int(korkeus/2)

    for i in range(maara):
        palkit.append(Palkki(x, randint(0,150), randint(1, 2), 0, randint(50, 150)))
        x += int(leveys/maara)

def inputt():
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()


def main():
    luopalkki(98)
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        for palkki in palkit:
            palkki.piirto()
            palkki.heilu()
        pygame.display.update()
        clock.tick(30)

if(__name__ == "__main__"):
    main()
