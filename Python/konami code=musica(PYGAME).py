import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

# ---------------- CONFIGURAÇÕES ----------------

LARGURA = 640
ALTURA = 480
GRID = 32

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("?")

clock = pygame.time.Clock()

# ---------------- MÚSICA ----------------

pasta = os.path.dirname(os.path.abspath(__file__))
musica = os.path.join(pasta, "MUSICA(konami code=musica).mp3")

# ---------------- JOGADOR ----------------

x = LARGURA // 2
y = ALTURA // 2

# Alinha o jogador ao grid
x = (x // GRID) * GRID
y = (y // GRID) * GRID

# ---------------- KONAMI CODE ----------------

konami = [
    pygame.K_UP,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_DOWN,
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_b,
    pygame.K_a
]

digitado = []
musica_tocando = False

# ---------------- LOOP PRINCIPAL ----------------

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            # ---------------- MOVIMENTO ----------------

            if evento.key == pygame.K_LEFT:
                x -= GRID

            elif evento.key == pygame.K_RIGHT:
                x += GRID

            elif evento.key == pygame.K_UP:
                y -= GRID

            elif evento.key == pygame.K_DOWN:
                y += GRID

            # Limites da tela
            if x < 0:
                x = 0
            if y < 0:
                y = 0
            if x > LARGURA - GRID:
                x = LARGURA - GRID
            if y > ALTURA - GRID:
                y = ALTURA - GRID

            # ---------------- KONAMI CODE ----------------

            digitado.append(evento.key)

            if len(digitado) > len(konami):
                digitado.pop(0)

            if digitado == konami:

                if not musica_tocando:
                    pygame.mixer.music.load(musica)
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()

                    musica_tocando = True

                    print("KONAMI CODE ATIVADO!")

    # ---------------- DESENHO ----------------

    tela.fill((25, 25, 25))

    # Grid
    for i in range(0, LARGURA, GRID):
        pygame.draw.line(tela, (50, 50, 50), (i, 0), (i, ALTURA))

    for j in range(0, ALTURA, GRID):
        pygame.draw.line(tela, (50, 50, 50), (0, j), (LARGURA, j))

    # Jogador
    pygame.draw.rect(
        tela,
        (255, 255, 255),
        (x, y, GRID, GRID)
    )

    pygame.display.flip()
    clock.tick(60)