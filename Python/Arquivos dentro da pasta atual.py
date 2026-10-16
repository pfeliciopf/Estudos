import os

print("Pasta atual:")
print(os.getcwd())

print()

print("Arquivos:")
for arquivo in os.listdir():
    print(arquivo)