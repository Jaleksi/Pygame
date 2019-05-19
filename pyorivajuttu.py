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
        for i in range(1, x):
            pallot.append(Pallo(int(ux), uy, 1))
            ux += leveys/x
            if(us == 1):
                uy += 15
            else:
                uy -= 15
            if(uy == 300):
                us = 0
            elif(uy == 270):
                us = 1

    def piirto(self):
        self.pos = [self.x, self.y]
        pygame.draw.circle(display, (0, 0, 0), self.pos, int(self.koko), 0)

    def tarkistus(self):
        if(self.y >= 330):
            self.suunta = 1
        elif(self.y <= 270):
            self.suunta = 0

    def palloSuunta(self):
        if(self.suunta == 1):
            self.heiluYlos()
        else:
            self.heiluAlas()

    def heiluYlos(self):
        self.y -= 3
        self.koko = int(interp(abs(self.y - 300), [0, 30], [3, 7]))

    def heiluAlas(self):
        self.y += 3
        self.koko = int(interp(abs(self.y - 300), [0, 30], [11, 7]))


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
