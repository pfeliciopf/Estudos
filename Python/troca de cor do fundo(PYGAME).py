import pygame
import random

pygame.init()

janela = pygame.display.set_mode((500, 300))

cores = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
cor = "white"

fonte = pygame.font.Font(None, 30)

cliques = 0

while True:
    janela.fill(cor)

    instrucao = fonte.render("Aperte ESPAÇO para trocar a cor", True, "black")
    contador = fonte.render(f"Cliques: {cliques}", True, "black")

    janela.blit(instrucao, (50, 50))
    janela.blit(contador, (50, 100))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                cor = random.choice(cores)
                cliques += 1

    pygame.display.update()