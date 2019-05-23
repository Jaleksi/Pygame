import pygame
from random import randint
from numpy import interp


pygame.init()
leveys = 600
korkeus = 600

display = pygame.display.set_mode((korkeus, leveys))
pygame.display.set_caption("Title")
clock = pygame.time.Clock()

pisteet = []

class Piste:
    def __init__(self, x, y, nopeus):
        self.x = x
        self.y = y
        self.nopeus = nopeus
        self.pos = [self.x, self.y]

    def piirto(self):
        self.pos = [self.x, self.y]
        pygame.draw.circle(display, (0), self.pos, 2)


    def matka(self):
        self.pos = [self.x, self.y]
        for piste in pisteet:
            eta = abs(self.x - piste.x) + abs(self.y - piste.y)
            if(50 < eta < 150 and self != piste):
                color = int(interp(eta, [0, 150], [0, 255]))
                pygame.draw.line(display, [color, color, color], self.pos, piste.pos, 1)

    def paskatuusiksi(self):
        self.x = randint(30, 570)
        self.y = randint(30, 570)

    def liiku(self):
        self.x += self.nopeus
        if(self.x >= 600 or self.x <= 0):
            self.nopeus *= -1
def luopiste(maara):
    for i in range(maara):
        pisteet.append(Piste(randint(30, 570), randint(30, 570), randint(-2, 2)))






def inputt():
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    for piste in pisteet:
                        piste.paskatuusiksi()


def main():
    luopiste(121)
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        for piste in pisteet:
#            piste.piirto()
            piste.liiku()
            piste.matka()
        pygame.display.update()
        clock.tick(30)

if(__name__ == "__main__"):
    main()
