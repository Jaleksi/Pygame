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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.leveys = 5
        if(self.y >= 150):
            self.speed = randint(-3, -1)
        else:
            self.speed = randint(1, 3)


    def piirto(self):
        self.korkeus = 150-self.y
        self.pos = [self.x, self.y, self.leveys, self.korkeus]
        self.color1 = interp(abs(self.korkeus), [0, 150], [235, 20])
        self.color2 = interp(self.x, [0, 600], [20, 235])
        pygame.draw.rect(display, [100, self.color1, self.color2] , self.pos, 0)

    def heilu(self):
        if(self.y > randint(200,300)):
            self.speed = randint(-3, -1)
        elif(self.y < randint(0, 100)):
            self.speed = randint(1, 3)

        self.y += self.speed

def luopalkki(maara):
    x = int(leveys/maara)
    y = int(korkeus/2)

    for i in range(maara):
        palkit.append(Palkki(x, randint(0,300)))
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
