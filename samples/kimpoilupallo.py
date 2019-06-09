import pygame
import random

pygame.init()
leveys = 400
korkeus = 400
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("[Juttu]")
clock = pygame.time.Clock()

class Ruutu:
    def __init__(self, x, y, vari):
        self.x = x
        self.y = y
        self.vari = vari

    def piirto(self):
        pygame.draw.rect(display, self.vari, [self.x, self.y, 10, 10])

class Pallo(Ruutu):
    def __init__(self, x, y, xsuunta, ysuunta):
        self.x = x
        self.y = y
        self.xsuunta = xsuunta
        self.ysuunta = ysuunta

    def meno(self):
        if(self.xsuunta == 1):
            self.x += 1
        else:
            self.x -= 1
        if(self.ysuunta == 1):
            self.y += 1
        else:
            self.y -= 1

    def pallopiirto(self):
        pygame.draw.circle(display, (0,0,0), [self.x, self.y], 3, 0)

def main():
    ruudut = []
    for i in range(40):
        for j in range(40):
            variz = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
            ruudut.append(Ruutu((korkeus//40*i), (leveys//40*j), variz))

    pallo = Pallo(188, 233, 1, 0)


    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
        display.fill(pygame.Color("white"))
        for ruutu in ruudut:
            ruutu.piirto()
        pallo.meno()
        pallo.pallopiirto()

        for ruutu in ruudut:
            if(pallo.x+3 >= ruutu.x and pallo.y+3 >= ruutu.y):
                if(pallo.x-3 <= ruutu.x+10 and pallo.y-3 <= ruutu.y+10):
                    if(pallo.x+3 == ruutu.x or pallo.x-3 == ruutu.x+10):
                        if(pallo.xsuunta == 1):
                            pallo.xsuunta = 0
                        else:
                            pallo.xsuunta = 1
                    elif(pallo.y+3 == ruutu.y or pallo.y-3 == ruutu.y+10):
                        if(pallo.ysuunta == 1):
                            pallo.ysuunta = 0
                        else:
                            pallo.ysuunta = 1
                    ruudut.remove(ruutu)
                    break
        clock.tick(50)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
