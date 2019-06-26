import pygame
from random import randint

pygame.init()
leveys = 400
korkeus = 400
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Juttu")
clock = pygame.time.Clock()


class Nelio:
    def __init__(self, x, y, koko):
        self.x = x
        self.y = y
        self.koko = koko

    def piirto(self):
        self.rect = pygame.Rect(self.x, self.y, self.koko, self.koko)
        pygame.draw.rect(display, (0), self.rect, 0)

    def move(self):
        if(self.y > 400):
            self.y = -50
            self.x = randint(0, 390)
        else:
            self.y += self.koko//10


def inPut():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()


def logic(rects):
    for rect in rects:
        rect.piirto()
        rect.move()


def main():
    neliot = []
    for _ in range(60):
        neliot.append(Nelio(randint(0, 390), randint(-450, -50),
                            randint(10, 50)))

    while(1):
        display.fill(pygame.Color("white"))
        inPut()
        logic(neliot)
        clock.tick(40)
        pygame.display.update()


if(__name__ == "__main__"):
    main()
