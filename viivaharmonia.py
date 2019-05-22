import pygame
from random import randint
from numpy import interp

#
# INPUT: SPACE/VÄLILYÖNTI, uusi kuvio.
#

pygame.init()
leveys = 300
korkeus = 300

display = pygame.display.set_mode((korkeus, leveys))
pygame.display.set_caption("Title")
clock = pygame.time.Clock()

pisteet = []

class Piste:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]

    def piirto(self):
        self.pos = [self.x, self.y]
        pygame.draw.circle(display, (0), self.pos, 2)


    def matka(self):
        self.pos = [self.x, self.y]
        for piste in pisteet:
            eta = abs(self.x - piste.x) + abs(self.y - piste.y)
            color = int(interp(eta, [0, 100], [0, 255]))
            if(eta < 100 and self != piste):
                pygame.draw.line(display, [color, color, color], self.pos, piste.pos, 1)

    def paskatuusiksi(self):
        self.x = randint(30, 270)
        self.y = randint(30, 270)

    def liiku(self):
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)
        if(self.x > 300):
            self.x = 300
        elif(self.x < 0):
            self.x = 0
        if(self.y > 300):
            self.y = 300
        elif(self.y < 0):
            self.y = 0

def luopiste(maara):
    for i in range(maara):
        pisteet.append(Piste(randint(30, 270), randint(30, 270)))






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
    luopiste(41)
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        for piste in pisteet:
#            piste.piirto()
            piste.matka()
            piste.liiku()
        pygame.display.update()
        clock.tick(30)

if(__name__ == "__main__"):
    main()
