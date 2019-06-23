import pygame
pygame.init()
leveys = 800
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("pp")
clock = pygame.time.Clock()

#
# INPUT: hiiri + välilyönti
#


class Palikka:
    palikat = []
    aika = 0
    aaltoilu = False

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.red = 0
        self.alive = 1

    def luo(maara):
        x = 50
        y = korkeus/2
        a = 50
        b = 100
        for _ in range(maara):
            Palikka.palikat.append(Palikka(x, y, a, b))
            x += 60

    def piirto(self):
        self.vari = [self.red, self.red, self.red]
        self.rect = [self.x, self.y, self.a, self.b]
        pygame.draw.rect(display, self.vari, self.rect, 0)

    def veny(self, maara):
        self.y -= maara
        self.b += maara*2
        self.red += maara*2
        if(self.red > 255):
            self.red = 255
        elif(self.red < 0):
            self.red = 0

    def hiiri(self, hx, hy):
        if(self.x < hx < self.x+self.a and self.y < hy < self.y+self.b):
            self.veny(4)
        else:
            if(self.y < korkeus/2):
                self.veny(-1)

    def aalto():
        vuoro = int((pygame.time.get_ticks() - Palikka.aika)*4/1000)
        try:
            Palikka.palikat[vuoro].veny(10)
        except Exception:
            Palikka.aaltoilu = False


def inbut():
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                Palikka.aaltoilu = True
                Palikka.aika = pygame.time.get_ticks()


def main():
    Palikka.luo(12)
    while(True):
        inbut()
        hiirix, hiiriy = pygame.mouse.get_pos()
        display.fill(pygame.Color("white"))
        for palikka in Palikka.palikat:
            palikka.piirto()
            palikka.hiiri(hiirix, hiiriy)
        if(Palikka.aaltoilu):
            Palikka.aalto()
        pygame.display.update()
        clock.tick(40)


if(__name__ == "__main__"):
    main()
