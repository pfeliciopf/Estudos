import math

a = int(input("Qual o valor de a: "))
b = int(input("Qual o valor de b: "))
c = int(input("Qual o valor de c: "))

delta = (b**2) - (4*a*c)

print("Delta =", delta)

if delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print("A raiz é:", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("x1 =", x1)
    print("x2 =", x2)