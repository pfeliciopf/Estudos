import os

# Pasta onde este arquivo .py está
pasta = os.path.dirname(os.path.abspath(__file__))

contador = 0

for item in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, item)):
        contador += 1

print("Quantidade de arquivos:", contador)