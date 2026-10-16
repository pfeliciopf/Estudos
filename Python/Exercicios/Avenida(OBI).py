d = int(input())

resto = d % 400
voltar = 400 - resto

if resto < voltar:
    print(resto)
else:
    print(voltar)
