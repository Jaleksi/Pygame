import pygame
from numpy import interp

pygame.init()
leveys = 800
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("pVVp")
clock = pygame.time.Clock()
pallot = []


class Pallo:
    def __init__(self, x, y, suunta):
        self.x = x
        self.y = y
        self.suunta = suunta
    def luoPallo(x):
        ux = leveys/x
        uy = 300
        us = 1
        for _ in range(1, x):
            pallot.append(Pallo(ux, uy, 1))
            ux += leveys/x
            uy += 30

    def piirto(self):
        self.pos = [int(self.x), int(self.y)]
        pygame.draw.circle(display, (0, 0, 0), self.pos, int(self.koko), 0)

    def tarkistus(self):
        if(self.y >= 360):
            self.suunta = 1
        elif(self.y <= 240):
            self.suunta = 0

    def palloSuunta(self):
        if(self.suunta == 1):
            self.heiluYlos()
        else:
            self.heiluAlas()

    def heiluYlos(self):
        self.y -= 3
        self.koko = int(interp(abs(self.y - 300), [0, 60], [3, 7]))

    def heiluAlas(self):
        self.y += 3
        self.koko = int(interp(abs(self.y - 300), [0, 60], [11, 7]))


def main():
    Pallo.luoPallo(41)
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
        display.fill(pygame.Color("white"))
        for pallo in pallot:
            pallo.tarkistus()
            pallo.palloSuunta()
            pallo.piirto()
        clock.tick(40)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
