print("-----GEOGRAFIA COM PYTHON-----")

pergunta = str(input("vc quer saber a densidade demografica de algum pais: ")).lower()

if pergunta == "não":
    print("ok, estou aqui se precisar")

elif pergunta == "sim":
    print("Que bom, agr preciso de algumas informações")

    hab = float(input("quantos habitantes tem nesse pais? "))
    at = float(input("qual a área territorial? "))

    dd = at / hab

    print("a densidade demografica do seu pais é", dd)


else:
    print ("digite uma resposta valida seu burro")
