import pygame

pygame.init()
leveys = 400
korkeus = 300

display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("WoWzA")
clock = pygame.time.Clock()


class Pallo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vauhti = 3
        self.xsuunta = 1
        self.ysuunta = 0
        self.loc = []

    def piirto(self):
        for sij in self.loc:
            pygame.draw.circle(display, sij[2], [sij[0], sij[1]], 10, 1)
            sij[2][1] += 10
            sij[2][2] += 10

    def liiku(self):
        self.loc.append([self.x, self.y, [250, 0, 0]])

        if(len(self.loc) > 25):
            self.loc.pop(0)

        if(self.xsuunta == 0):
            self.x += self.vauhti
        else:
            self.x -= self.vauhti
        if(self.ysuunta == 0):
            self.y += self.vauhti
        else:
            self.y -= self.vauhti

        if(self.x >= 390 or self.x <= 10):
            self.xsuunta = vaihto(self.xsuunta)

        if(self.y >= 290 or self.y <= 10):
            self.ysuunta = vaihto(self.ysuunta)


def vaihto(x):
    if(x == 0):
        return 1
    else:
        return 0


def inputt():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()


def logic(entity):
    entity.liiku()
    entity.piirto()


def main():
    pallo = Pallo(177, 140)
    while(True):
        inputt()
        display.fill(pygame.Color("white"))
        logic(pallo)
        pygame.display.update()
        clock.tick(30)


if(__name__ == "__main__"):
    main()
