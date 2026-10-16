import time

bolinhas = int(input("Quantas bolinhas você quer colocar em uma caixa?: "))
caixa = 1

# Usamos <= para que a última bolinha também entre na caixa
while caixa <= bolinhas:
    time.sleep(1)
    print(f"A bolinha {caixa} está dentro da caixa")
    caixa += 1  # Agora sim, incrementando o valor corretamente!