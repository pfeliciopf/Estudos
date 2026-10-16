import pygame

pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Movimento Top Down")

# Cores
cor_preto = (0, 0, 0)
cor_azul = (50, 100, 255)

# Jogador
x = 400
y = 300
tamanho = 40
velocidade = 5

clock = pygame.time.Clock()

rodando = True
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Captura as teclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        y -= velocidade

    if teclas[pygame.K_DOWN]:
        y += velocidade

    if teclas[pygame.K_LEFT]:
        x -= velocidade

    if teclas[pygame.K_RIGHT]:
        x += velocidade

    # Desenha
    tela.fill(cor_preto)

    pygame.draw.rect(
        tela,
        cor_azul,
        (x, y, tamanho, tamanho)
    )

    pygame.display.update()

    # Mantém 60 FPS
    clock.tick(60)

pygame.quit()