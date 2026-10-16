#prova obi n junior fase 2 prova 2015

tamanho=int(input())
lista=list(map(int,input().split()))

contador= 0

#reconhecer quantos 100 tem na lista
for i in range(tamanho-2):
    if lista[i + 0]==1 and lista[i+ 1]==0 and lista[i+ 2]==0:
        contador+=1

print(contador)