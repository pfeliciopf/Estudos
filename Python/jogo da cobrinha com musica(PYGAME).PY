#configurações iniciais
import pygame
import random
import os
import time

#inicia jogo
pygame.init()

#música

time.sleep(5) #tempo para sincronizar a musica e o jogo

pygame.mixer.init() #inicia o mixer

pasta = os.path.dirname(os.path.abspath(__file__)) #descobre onde esta o arquivo
musica = os.path.join(pasta, "MUSICA(jogo da cobrinha com música).mp3") #caminho completo até a música

pygame.mixer.music.load(musica) #carrega a música
pygame.mixer.music.set_volume(0.5) #volume de 0 a 1 
pygame.mixer.music.play(-1) #toca em loop

#nome da janela
pygame.display.set_caption("jogo snake")

#tamanho da tela
largura, altura= 600, 400
tela=pygame.display.set_mode((largura, altura))

relogio= pygame.time.Clock()

#cores
cor_preta=(0,0,0)
cor_branca=(255,255,255)
cor_vermelha=(255, 0, 0)
cor_verde=(0, 255, 0)

#tamanho dos elementos
tamanho_quadrado=10

#parametros da cobrinha
velocidade_jogo=15

#gerar comida
def gerar_comida():
    
    comida_x= round(random.randrange(0, largura-tamanho_quadrado) /10) *10
    comida_y= round(random.randrange(0, altura-tamanho_quadrado) /10) *10
    return comida_x, comida_y

#desenhar comida
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, cor_vermelha, [comida_x, comida_y, tamanho, tamanho])

#desenhar cobra
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cor_verde, [pixel[0], pixel[1], tamanho, tamanho])

#desenhar ponto
def desenhar_pontuação(pontuação):
    fonte=pygame.font.SysFont("Helvetica", 15)
    texto=fonte.render(f"Pontos: {pontuação}", True, cor_branca)
    tela.blit(texto, [1,1])

#selecionar velocidade
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x=0
        velocidade_y=tamanho_quadrado
    
    elif tecla == pygame.K_UP:
        velocidade_x=0
        velocidade_y=-tamanho_quadrado
    
    elif tecla == pygame.K_RIGHT:
        velocidade_x=tamanho_quadrado
        velocidade_y=0

    elif tecla == pygame.K_LEFT:
        velocidade_x=-tamanho_quadrado
        velocidade_y=0
            
    return velocidade_x, velocidade_y


#rodar jogo
def rodar_jogo():
    fim_jogo=False
    
    #posição cobrinha
    x=largura/2
    y=altura/2

    #velocidade da cobra para x e y
    velocidade_x=0
    velocidade_y=0

    #tamanho cobra
    tamanho_cobra=1
    pixels=[]

    #comida
    comida_x, comida_y=gerar_comida()

    #loop infinito
    while not fim_jogo:

        tela.fill(cor_preta)

        #interações usuario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo=True

            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #atualizar posição da cobra
        x += velocidade_x
        y += velocidade_y
        
        #desenhar cobra
        pixels.append([x, y])

        if len(pixels) > tamanho_cobra:
            del pixels[0]
            
        #se a cobra bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo=True

        desenhar_cobra(tamanho_quadrado, pixels)

        #desenhar pontos
        desenhar_pontuação(tamanho_cobra-1)

        #atualização da tela
        pygame.display.update()
        relogio.tick(velocidade_jogo)

        #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()


rodar_jogo()