import pygame
import os
import time

# Inicia o mixer de áudio
pygame.mixer.init()

# Descobre a pasta onde este arquivo .py está
pasta = os.path.dirname(os.path.abspath(__file__))

# Caminho completo da música
musica = os.path.join(pasta, "tetris.mp3")

# Carrega a música
pygame.mixer.music.load(musica)

# Volume (0.0 a 1.0)
pygame.mixer.music.set_volume(0.5)

# Toca em loop infinito
pygame.mixer.music.play(-1)

print("Música tocando!")
print("Arquivo encontrado em:")
print(musica)

# Mantém o programa aberto
while True:
    time.sleep(1)