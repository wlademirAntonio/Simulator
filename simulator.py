import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1900
altura = 980

centro = (largura/2, altura/2)

corTerra = (0, 0, 255)
raioTerra = 200
massaTerra = 10000

constanteGravitacional = 1

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Simulator')
relogio = pygame.time.Clock()

class Projetil:

    projeteis = []

    def __init__(self):
        
        self.cor = (255, 255, 255)
        self.raio = 7
        self.massa = 1

        self.posicaoX = centro[0]
        self.posicaoY = centro[1] - 250

        self.velocidadeX = 6.1
        self.velocidadeY = 0

    def gerar(self):

        self.projeteis.append([self.posicaoX, self.posicaoY, self.velocidadeX, self.velocidadeY])

    def movimento(self, pX, pY, vX, vY):

        distanciaX = centro[0] - pX
        distanciaY = centro[1] - pY

        distancia = ((distanciaX ** 2) + (distanciaY ** 2)) ** (1/2)

        produtoMassas = self.massa * massaTerra
        produtoDistancia = distancia * distancia

        forcaGravitacional = constanteGravitacional * produtoMassas / produtoDistancia

        cos = distanciaX / distancia
        sen = distanciaY / distancia

        forcaX = forcaGravitacional * cos
        forcaY = forcaGravitacional * sen

        aceleracaoX = forcaX / self.massa
        aceleracaoY = forcaY / self.massa

        vX = vX + aceleracaoX
        vY = vY + aceleracaoY

        if self.colisao(distancia) == 0:

            pX = pX + vX
            pY = pY + vY

        else:

            pass

        return pX, pY, vX, vY
    
    def colisao(self, d):

        somaRaios = self.raio + raioTerra
        
        if d <= somaRaios:

            c = 1

        else:

            c = 0

        return c

    def update(self):
    
        for p in self.projeteis:

            pygame.draw.circle(tela, self.cor, (p[0], p[1]), self.raio)

            self.projeteis[self.projeteis.index(p)] = self.movimento(p[0], p[1], p[2], p[3])


projetil = Projetil()

while True:

    relogio.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == K_SPACE:

                projetil.gerar()

        if event.type == QUIT:

            pygame.quit()

    pygame.draw.circle(tela, corTerra, centro, raioTerra)

    projetil.update()

    pygame.display.update()