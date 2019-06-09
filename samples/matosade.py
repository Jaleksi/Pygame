import pygame
from random import *

#
#MADOT VÄISTÄÄ HIIRTÄ
#

pygame.init()
leveys = 800
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("JauZa")
clock = pygame.time.Clock()
madot = []

class Mato:
    def __init__(self, x, y, vari):
        self.x = x
        self.y = y
        self.vari = pygame.Color(vari)
        self.sij = [[self.x, self.y]]
    def luoMato(x):
        for i in range(x):
            madot.append(Mato(randint(50, leveys-50), randint(-korkeus, -50), "black"))

    def luiker(self, mx, my):
        if(self.y > korkeus+len(self.sij)*5):
            self.x = randint(50, leveys-50)
            self.y = randint(-korkeus, -50)
        else:
            self.y += 3
            if(self.x-50<mx<self.x+50 and self.y+50>my>self.y-20):
                if(self.x >= mx):
                    self.x += randint(1, 3)
                elif(self.x < mx):
                    self.x -= randint(1, 3)
            else:
                self.x += randint(-1, 1)
            self.sij.append([self.x, self.y])
            if(len(self.sij) > 10):
                self.sij.pop(0)

    def piirto(self):
        for i in self.sij:
            x = i[0]
            y = i[1]
            pygame.draw.circle(display, self.vari, [x, y], self.sij.index(i), 0)

def main():
    Mato.luoMato(30)
    while(True):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
        display.fill(pygame.Color("white"))
        for mato in madot:
            mato.luiker(mx, my)
            mato.piirto()
        clock.tick(30)
        pygame.display.update()
if(__name__ == "__main__"):
    main()
