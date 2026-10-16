import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# ---------------- TELA ----------------

LARGURA = 640
ALTURA = 480
GRID = 32

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Grid com músicas")

clock = pygame.time.Clock()

# ---------------- CAMINHO DAS MÚSICAS ----------------

PASTA_MUSICAS = os.path.join(os.path.dirname(__file__), "MÚSICAS (mp3 player)")

# ---------------- JOGADOR ----------------

x = 0
y = 0

# ---------------- QUADRADOS ----------------

quadrados = [
    {
        "x": 64,
        "y": 64,
        "cor": (255, 0, 0),
        "musica": os.path.join(PASTA_MUSICAS, "vermelho.mp3")
    },

    {
        "x": 160,
        "y": 64,
        "cor": (0, 255, 0),
        "musica": os.path.join(PASTA_MUSICAS, "verde.mp3")
    },

    {
        "x": 64,
        "y": 160,
        "cor": (0, 0, 255),
        "musica": os.path.join(PASTA_MUSICAS, "azul.mp3")
    },

    {
        "x": 160,
        "y": 160,
        "cor": (255, 255, 0),
        "musica": os.path.join(PASTA_MUSICAS, "amarelo.mp3")
    }
]

musica_atual = ""

# ---------------- LOOP ----------------

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

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

            # Verifica colisão
            for q in quadrados:

                if x == q["x"] and y == q["y"]:

                    if musica_atual != q["musica"]:

                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(q["musica"])
                        pygame.mixer.music.play(-1)

                        musica_atual = q["musica"]

    # ---------------- DESENHO ----------------

    tela.fill((30, 30, 30))

    # Grid
    for i in range(0, LARGURA, GRID):
        pygame.draw.line(tela, (70, 70, 70), (i, 0), (i, ALTURA))

    for j in range(0, ALTURA, GRID):
        pygame.draw.line(tela, (70, 70, 70), (0, j), (LARGURA, j))

    # Quadrados
    for q in quadrados:
        pygame.draw.rect(
            tela,
            q["cor"],
            (q["x"], q["y"], GRID, GRID)
        )

    # Jogador
    pygame.draw.rect(
        tela,
        (255, 255, 255),
        (x, y, GRID, GRID)
    )

    pygame.display.update()
    clock.tick(60)