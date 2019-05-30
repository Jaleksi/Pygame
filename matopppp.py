import pygame
from random import choice


pygame.init()
leveys = 500
korkeus = 600
display = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Mato")
clock = pygame.time.Clock()
gameon = False

def inbut():
    global gameon
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            for valinta in valinnat:
                if(valinta.valittu):
                    if(valinta.msg == "Uusi peli"):
                        gameon = True
                        peli()
                    elif(valinta.msg == "Hiscores"):
                        print("tulossa..")
                    elif(valinta.msg == "Lopeta"):
                        pygame.quit()
                        exit()
        if(event.type == pygame.KEYDOWN):
            if(gameon):
                if(event.key == pygame.K_LEFT):
                    mato.xnopeus = -10
                    mato.ynopeus = 0
                if(event.key == pygame.K_RIGHT):
                    mato.xnopeus = 10
                    mato.ynopeus = 0
                if(event.key == pygame.K_UP):
                    mato.ynopeus = -10
                    mato.xnopeus = 0
                if(event.key == pygame.K_DOWN):
                    mato.ynopeus = 10
                    mato.xnopeus = 0
            else:
                main()

class Teksti:
    def __init__(self, msg, koko, x, y, vari):
        self.msg = msg
        self.koko = koko
        self.x = x
        self.y = y
        self.vari = vari
        self.valittu = False

    def piirto(self):
        self.teksti = pygame.font.SysFont("Arial", self.koko)
        self.rend = self.teksti.render(self.msg, True, self.vari)

        self.rect = self.rend.get_rect(center=(leveys/2, self.y))
        display.blit(self.rend, self.rect)

    def klik(self):
        mx, my = pygame.mouse.get_pos()
        self.x2, self.y2, self.w, self.h = self.rend.get_rect()
        if(self.y - self.h/2 < my < self.y + self.h/2 and 200 < mx < 400):
            self.vari = (0, 255, 0)
            self.valittu = True
        else:
            self.vari = (0, 0, 0)
            self.valittu = False


valinnat = [Teksti("Uusi peli", 24, 0, 350, (0, 0, 0)),
            Teksti("Hiscores", 24, 0, 400, (0, 0, 0)),
            Teksti("Lopeta", 24, 0, 450, (0, 0, 0))]


def main():
    global mato
    mato = Mato(0, 100)
    while(True):
        display.fill(pygame.Color("white"))
        inbut()
        otsikko = Teksti("Matopeli", 36, 0, 100, (0, 0, 0))
        otsikko.piirto()
        for valinta in valinnat:
            valinta.piirto()
            valinta.klik()

        clock.tick(30)
        pygame.display.update()


class Mato:
    def __init__(self, x, y):
        self.xnopeus = 0
        self.ynopeus = 0
        self.kokomato = []
        self.paa = pygame.Rect(x, y, 10, 10)
        self.kokomato.append(self.paa)
        self.pituus = 1

    def matopiirto(self):
        for osa in self.kokomato:
            pygame.draw.rect(display, (0, 255, 0), osa, 3)

    def matoliiku(self):
        global gameon
        uusipaa = pygame.Rect(self.paa.x + self.xnopeus,
                              self.paa.y + self.ynopeus,
                              10, 10)
        if(uusipaa in self.kokomato and self.ynopeus + self.xnopeus != 0):
            mato.xnopeus = 0
            mato.ynopeus = 0
            gameon = False
            loppu()
        if(uusipaa.x > 490):
            uusipaa.x = 0
        elif(uusipaa.x < 0):
            uusipaa.x = 490
        if(uusipaa.y > 590):
            uusipaa.y = 100
        elif(uusipaa.y < 100):
            uusipaa.y = 590
        self.kokomato.insert(0, uusipaa)
        omenapaikat.remove([uusipaa.x, uusipaa.y])
        self.paa = uusipaa

        print(len(omenapaikat))
        if(len(self.kokomato) > self.pituus):
            omenapaikat.append([self.kokomato[-1][0], self.kokomato[-1][1]])
            self.kokomato.pop()



    def matosyo(self):
        if(self.paa.x == omena.omppu.x and self.paa.y == omena.omppu.y):
            tmp = choice(omenapaikat)
            omena.omppu = pygame.Rect(tmp[0], tmp[1], 10, 10)
            self.pituus += 1


class Omena:
    def __init__(self, sijainti):
        self.omppu = pygame.Rect(sijainti[0], sijainti[1], 10, 10)

    def omenapiirto(self):
        pygame.draw.rect(display, (255, 0, 0), self.omppu, 3)


omenapaikat = []
ox = 0
oy = 100
for i in range(50):
    for j in range(50):
        omenapaikat.append([ox, oy])
        ox += 10
    oy += 10
    ox = 0
mato = Mato(0, 100)
omena = Omena(choice(omenapaikat))

def tulostaulu():
    pygame.draw.rect(display, (200, 200, 200), [0, 0, 500, 100], 0)
    Teksti("Syödyt omenat: "+str(mato.pituus-1), 18, 0, 10, (0,0,0)).piirto()

def loppu():
    Teksti("PELI LOPPUI", 18, 0, 200, (0,0,0)).piirto()
    Teksti("Paina jotain näppäintä palataksesi valikkoon", 18, 0, 250, (0,0,0)).piirto()
def peli():
    global gameon
    while(True):
        display.fill(pygame.Color("white"))
        inbut()
        if(gameon):
            mato.matoliiku()
            mato.matosyo()
            mato.matopiirto()
            omena.omenapiirto()
        else:
            mato.matopiirto()
            loppu()
        tulostaulu()
        clock.tick(10)
        pygame.display.update()




if(__name__ == "__main__"):
    main()
