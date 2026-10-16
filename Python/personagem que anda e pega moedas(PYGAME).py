import pygame
import random
import time

# Inicialização
pygame.init()

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletando Moedas")

# Cores
BRANCO = (255, 255, 255)
AZUL = (50, 100, 255)
AMARELO = (255, 215, 0)
PRETO = (0, 0, 0)

# Relógio
clock = pygame.time.Clock()

# Jogador
jogador = pygame.Rect(100, 100, 40, 40)
velocidade = 5

# Fonte
fonte = pygame.font.SysFont(None, 36)

# Criar moedas
moedas = []
for _ in range(10):
    moeda = pygame.Rect(
        random.randint(20, LARGURA - 40),
        random.randint(20, ALTURA - 40),
        20,
        20
    )
    moedas.append(moeda)

# Pontuação
pontos = 0

# Início do cronômetro
inicio = time.time()

# Loop principal
rodando = True
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # Limitar jogador à tela
    jogador.x = max(0, min(jogador.x, LARGURA - jogador.width))
    jogador.y = max(0, min(jogador.y, ALTURA - jogador.height))

    # Colisão com moedas
    for moeda in moedas:
        if jogador.colliderect(moeda):
            pontos += 1

            # Reposiciona a moeda
            while True:
                moeda.x = random.randint(20, LARGURA - moeda.width - 20)
                moeda.y = random.randint(20, ALTURA - moeda.height - 20)

                # Evita que a moeda apareça em cima do jogador
                if not jogador.colliderect(moeda):
                    break

    # Tempo decorrido
    tempo = time.time() - inicio

    # Desenhar
    tela.fill(PRETO)

    # Jogador
    pygame.draw.rect(tela, AZUL, jogador)

    # Moedas
    for moeda in moedas:
        pygame.draw.ellipse(tela, AMARELO, moeda)

    # Pontuação
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    # Cronômetro
    texto_tempo = fonte.render(f"Tempo: {tempo:.1f}s", True, BRANCO)
    tela.blit(texto_tempo, (10, 50))

    pygame.display.flip()

    # Encerra ao chegar a 100 pontos
    if pontos >= 100:
        tempo_final = time.time() - inicio
        print(f"Você fez 100 pontos em {tempo_final:.2f} segundos!")
        rodando = False

pygame.quit()